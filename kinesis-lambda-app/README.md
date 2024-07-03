# Real-time Stream Processing
* https://tuts.heomi.net/a-practical-introduction-to-aws-sam-a-comprehensive-guide-for-cloud-engineers/

# Step 1: Create a Kinesis Stream

First, create a Kinesis stream using the AWS Management Console or AWS CLI.
```bash
aws kinesis create-stream --stream-name MyKinesisStream --shard-count 1
```

# Step 2: Create an AWS SAM Template

Create a new directory for your project and a SAM template file.
```bash
mkdir kinesis-lambda-app
cd kinesis-lambda-app
touch template.yaml
```

Add the following content to the `template.yaml` file:
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: 'AWS::Serverless-2016-10-31'
Resources:
  KinesisStream:
    Type: AWS::Kinesis::Stream
    Properties:
      ShardCount: 1

  KinesisLambdaFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: app.lambda_handler
      Runtime: python3.9
      CodeUri: .
      Policies:
        - AWSLambdaKinesisExecutionRole
      Environment:
        Variables:
          STREAM_NAME: !Ref KinesisStream
      Events:
        KinesisEvent:
          Type: Kinesis
          Properties:
            Stream: !GetAtt KinesisStream.Arn
            StartingPosition: TRIM_HORIZON

Outputs:
  KinesisStreamName:
    Description: Name of the Kinesis stream
    Value: !Ref KinesisStream
  LambdaFunction:
    Description: ARN of the Lambda function
    Value: !GetAtt KinesisLambdaFunction.Arn
```

# Step 3: Create the Lambda Function

Create a new Python file named `app.py` in the same directory:
```bash
touch app.py
```

Add the following code to `app.py`:
```python
import json
import base64
import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        # Process the data
        print(data)

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed Kinesis stream data')
    }

```

# Step 4: Build and Deploy the SAM Application

Use the AWS SAM CLI to build and deploy your application.
```bash
sam build
sam deploy --guided
```

# Step 5: Test the Application

You can test the setup by putting records into the Kinesis stream.
```bash
aws kinesis put-record --stream-name MyKinesisStream --partition-key "partitionKey" --data '{"key": "value"}'
```
Check the logs of your Lambda function to verify that it has processed the data. You can view the logs in the AWS CloudWatch Logs console.