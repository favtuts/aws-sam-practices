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

# Deploy the API

```
$ sam build
$ sam build --use-container
$ sam build --use-container --build-image amazon/aws-sam-cli-build-image-nodejs20.x
$ sam deploy --guided --profile tvt_admin
```