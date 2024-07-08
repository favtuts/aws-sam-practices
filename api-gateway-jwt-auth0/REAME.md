# API Gateway HTTP JWT Authoriser with OAuth2 (eg. Auth0)

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
