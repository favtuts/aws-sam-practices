# API Gateway HTTP JWT Authoriser with OAuth2 (eg. Auth0)
* https://youtu.be/lrIwPL6JpeI?si=hXT0HitZBW2DV0YS


# Authorization Flow

(1) Client send a message to API Gateway with JWT Token

![Step1-JWT-Token](./images/api-gateway-jwt-auth0-step01.png)

(2) JWT Authorizer ask Auth0 to verify the Token

![Step2-Auth0-Request](./images/api-gateway-jwt-auth0-step02.png)


(3) Auth0 validate the Token

![Step3-Auth0-Response](./images/api-gateway-jwt-auth0-step03.png)


(4) API Gateway invoke Lambda request

![Step4-Invoke-Lambda-Request](./images/api-gateway-jwt-auth0-step04.png)


(5) Lamdbda do something and response

![Step5-Lamda-response](./images/api-gateway-jwt-auth0-step05.png)


(5) API Gateway return 200 HTTP to Client

![Step6-API-200-HTTP](./images/api-gateway-jwt-auth0-step06.png)

# Create project folder structure

```
$ mkdir api-gateway-jwt-auth0
$ cd  api-gateway-jwt-auth0
$ code .
```

# Create SAM template 

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:

  HelloFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: handler.hello
      Runtime: nodejs12.x
      CodeUri: ./hello
      Events:
        HelloAPI:
          Type: HttpApi
          Properties:
            Path: /hello
            Method: GET
```

# Create Lambda function

```js
exports.hello = async (event) => {
    return {
      statusCode: 200,
      body: JSON.stringify(event),
      headers: {}
    }
  }
```

# Setup NodeJS 12

List installed versions
```
$ nvm ls
```

List available remote versions
```
$ nvm ls-remote
```

Install a specific version
```
$ nvm install 12.22.12
```

Switch to version if it is already installed
```
$ nvm use 12.22.12
$ nvm alias default 12.22.12
$ node --version
```

# Deploy the API

First build the SAM app
```
$ sam build
$ sam build --use-container
$ sam build --use-container --build-image amazon/aws-sam-cli-build-image-nodejs12.x
$ sam build --use-container --build-image amazon/aws-sam-cli-build-image-nodejs20.x
```

You may build failed: `Error: Building functions with nodejs12.x is no longer supported`

Now you can deploy the SAM app
```
$ sam deploy --guided --profile tvt_admin

Successfully created/updated stack - api-gateway-jwt-auth0 in us-east-1
```


# Testing the API

```bash
$ curl --location 'https://bgnfoi0nbl.execute-api.us-east-1.amazonaws.com/hello'

{
    "version": "2.0",
    "routeKey": "GET /hello",
    "rawPath": "/hello",
    "rawQueryString": "",
    "headers": {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "content-length": "0",
        "host": "bgnfoi0nbl.execute-api.us-east-1.amazonaws.com",
        "postman-token": "a95aa266-d694-488e-b05a-d8a8cafd2486",
        "user-agent": "PostmanRuntime/7.39.0",
        "x-amzn-trace-id": "Root=1-668b60c2-4d79b12351aad1c52414ee86",
        "x-forwarded-for": "118.70.170.128",
        "x-forwarded-port": "443",
        "x-forwarded-proto": "https"
    },
    "requestContext": {
        "accountId": "475797023758",
        "apiId": "bgnfoi0nbl",
        "domainName": "bgnfoi0nbl.execute-api.us-east-1.amazonaws.com",
        "domainPrefix": "bgnfoi0nbl",
        "http": {
            "method": "GET",
            "path": "/hello",
            "protocol": "HTTP/1.1",
            "sourceIp": "118.70.170.128",
            "userAgent": "PostmanRuntime/7.39.0"
        },
        "requestId": "akwOXg70IAMEYbw=",
        "routeKey": "GET /hello",
        "stage": "$default",
        "time": "08/Jul/2024:03:45:06 +0000",
        "timeEpoch": 1720410306016
    },
    "isBase64Encoded": false
}
```

# Define the JWT Authorizer

Modify the template to define explicit the HTTP API with JWT Authorizer
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

  MyHttpApi:
    Type: AWS::Serverless::HttpApi
    Properties:
      Auth:
        DefaultAuthorizer: JWTTokenExample
        Authorizers:
          JWTTokenExample: 
            JwtConfiguration:
              issuer: XXX
              audience: XXX                
            IdentitySource: "$request.header.Authorization"  

  HelloFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: handler.hello
      Runtime: nodejs12.x
      CodeUri: ./hello
      Events:
        HelloAPI:
          Type: HttpApi
          Properties:
            ApiId: !Ref MyHttpApi
            Path: /hello
            Method: GET
```

# Config Auth0 API Application

![new_API_app](./images/api-gateway-jwt-auth0-new-API-app.png)

In the template replace:
* issuer = Authority = "https://iot-dev.us.auth0.com/"
* audience = "https://auth0-jwt-authorizer"


```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:

  MyHttpApi:
    Type: 'AWS::Serverless::HttpApi'
    Properties:            
      Auth:
        DefaultAuthorizer: GeneralAuth
        Authorizers:
          GeneralAuth:            
            IdentitySource: "$request.header.Authorization" 
            JwtConfiguration:
              issuer: "https://iot-dev.us.auth0.com/"
              audience: 
                - "https://auth0-jwt-authorizer"

  HelloFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: handler.hello
      Runtime: nodejs20.x
      CodeUri: ./hello
      Events:
        HelloAPI:          
          Type: HttpApi
          Properties:
            ApiId: !Ref MyHttpApi
            Path: /hello
            Method: GET

Outputs:
  MyHttpApi:
    Description: API Gateway endpoint URL
    Value: !Sub "https://${MyHttpApi}.execute-api.${AWS::Region}.amazonaws.com/hello/"
  HelloFunction:
    Description: Hello Lambda Function ARN
    Value: !GetAtt HelloFunction.Arn
  HelloFunctionIamRole:
    Description: Implicit IAM Role created for Hello function
    Value: !GetAtt HelloFunctionRole.Arn
```


# Redeploy SAM application

Re-build
```
$ sam build
```

```
$ sam deploy --guided --profile tvt_admin

---------------------------------------------------------------------------------------------------------
Operation                  LogicalResourceId          ResourceType               Replacement
---------------------------------------------------------------------------------------------------------
+ Add                      MyHttpApiApiGatewayDefau   AWS::ApiGatewayV2::Stage   N/A
                           ltStage
+ Add                      MyHttpApi                  AWS::ApiGatewayV2::Api     N/A
* Modify                   HelloFunctionHelloAPIPer   AWS::Lambda::Permission    True
                           mission
- Delete                   ServerlessHttpApiApiGate   AWS::ApiGatewayV2::Stage   N/A
                           wayDefaultStage
- Delete                   ServerlessHttpApi          AWS::ApiGatewayV2::Api     N/A
---------------------------------------------------------------------------------------------------------
```


![deployed_authorizer](./images/api-gateway-jwt-auth0-attached-jwt-authorizer.png)


# Testing 

Get access token

```bash
curl --request POST \
  --url https://iot-dev.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_id":"uLihMYWb9nuVbGg5m4q5A0l5f3Nz5gtx","client_secret":"lZO2vxyEtvM8NNWCwoI_-arUQqIsl3BL7O4wdOo6644u52nbMedtl_4NGeRAGD4D","audience":"https://auth0-jwt-authorizer","grant_type":"client_credentials"}'


{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5rOEo1czVGalNuOEN4MjNaWDVhYiJ9.eyJpc3MiOiJodHRwczovL2lvdC1kZXYudXMuYXV0aDAuY29tLyIsInN1YiI6InVMaWhNWVdiOW51VmJHZzVtNHE1QTBsNWYzTno1Z3R4QGNsaWVudHMiLCJhdWQiOiJodHRwczovL2F1dGgwLWp3dC1hdXRob3JpemVyIiwiaWF0IjoxNzIwNDI5MTY4LCJleHAiOjE3MjA1MTU1NjgsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6InVMaWhNWVdiOW51VmJHZzVtNHE1QTBsNWYzTno1Z3R4In0.rdZNJXhSONfet1Wf5BYeDLxG4eRb03vUTDefvtSJrMA62zUwOwIyNuIQzAayKx747pryCIPV4PusLIjhz6YImKvJx_UCjW9JSbxmu55j6tE45L7ZQZISNX8lX0F7a0u7NV2MNi80u8fGYISycPErlmp4_BgNUmtQXAaNhEUIn0lc7ZqwerS2r3conJBB5tyo2VWWSBSMwiTfMMmoFDGFuYfn6ykWFKswy9JW4RLt0M96D0vhdu19b3oK-F9hcMjJC4HO-hxDeGngFYRSlFxEKml6DGkFOGVr4DARzaAAvvU-6GUjAO7EgJIO5wvVqqm0ie4qoVUxTFCTouzkFRrGPg","expires_in":86400,"token_type":"Bearer"}
```


Execute the API
```bash
curl --location 'https://ve67u7oa2b.execute-api.us-east-1.amazonaws.com/hello' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5rOEo1czVGalNuOEN4MjNaWDVhYiJ9.eyJpc3MiOiJodHRwczovL2lvdC1kZXYudXMuYXV0aDAuY29tLyIsInN1YiI6InVMaWhNWVdiOW51VmJHZzVtNHE1QTBsNWYzTno1Z3R4QGNsaWVudHMiLCJhdWQiOiJodHRwczovL2F1dGgwLWp3dC1hdXRob3JpemVyIiwiaWF0IjoxNzIwNDI5MDcyLCJleHAiOjE3MjA1MTU0NzIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6InVMaWhNWVdiOW51VmJHZzVtNHE1QTBsNWYzTno1Z3R4In0.UXNJs_k0UzjQo9aZWuhssCjklpdBgtjLPAJm8HzcGDt7OdTliec8hkF0W_a7bKaAdWZSGTwVRio_JCg_61t7_ixzdyue0YcehVWyWF0FpuXhO-fxltWZnkydwGJeAgNlZBUHAB7zkNEViNwoC3QdDqmm0M8Peku-XEdShWuwLtAHrCROWS0IwLDc_UBDb7G-vUtQ3XfjT0X2TtbeCArxX3bKFjdCLNYkDo93dGma36wKgct8VthzYYv6gxvJpbqgC4AcexWynUz5ajv0xtjISjZE6vD1nYR47jimcBY9ja4HkLGr2ljVgBl_aNzrehqOtrjsM839VzZrAXahodx_Nw'
```