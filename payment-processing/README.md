# Building A Payment Processing Workflow For A Fintech App Using AWS Step Functions and AWS SAM
* https://tuts.heomi.net/building-a-payment-processing-workflow-for-a-fintech-app-using-aws-step-functions-and-aws-sam/

# Create The SAM Directory Structure

```bash
$ mkdir -p payment-processing/src
```

# Create validate_payment Lambda Functions

```bash
$ touch src/validate_payment.py
```

Python code
```python
import boto3
import json
import os


def lambda_handler(event, context):
    print("received event:", json.dumps(event))
    # Validate the payment details from the event
    payment_details = event['payment_details']
    print("Payment Details:", payment_details)
    if not validate_payment(payment_details):
        raise Exception("Invalid Payment Details")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Payment validation successful. Workflow initiated.'
        })
    }

def validate_payment(details):
    # Add your payment validation logic here
    if not details.get('card_number') or not details.get('expiry_date') or not details.get('cvv'):
        return False
    return True
```

# Create process_payment Lambda Functions

```bash
$ touch src/process_payment.py
```

Python code
```python
import json
import random

def lambda_handler(event, context):
    try:
        # Simulate payment processing logic
        payment_info = event.get('payment_info')
        print(f"Processing payment: {payment_info}")
        
        # Simulate a transient error with 30% probability
        if random.random() < 0.3:
            raise Exception("TransientError")
        
        return {
            'statusCode': 200,
            'body': json.dumps("Payment processed successfully")
        }
    except Exception as e:
        raise e
```


# Create update_payment_status Lambda Functions

```bash
$ touch src/update_payment_status.py
```

Python code
```python
import json
import boto3
import uuid
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    try:
        # Generate a random payment ID using uuid
        payment_id = str(uuid.uuid4())
        
        # Retrieve status from the event
        status = event.get('status', 'Processed')
        
        # Update the order status in DynamoDB with the generated payment_id
        response = table.update_item(
            Key={'PaymentId': payment_id},  # Assuming 'PaymentId' is your primary key
            UpdateExpression='SET PaymentStatus = :val',
            ExpressionAttributeValues={':val': status}
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Payment ID {payment_id} status updated to {status} successfully")
        }
    except ClientError as e:
        print(e.response['Error']['Message'])
        raise e
    except Exception as e:
        print(str(e))
        raise e
```


# Create update_payment_status Lambda Functions

```bash
$ touch src/send_notification.py
```

Python code
```python
import json
import boto3
from botocore.exceptions import ClientError

sns_client = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-1:123456789012:OrderNotifications' #UPDATE YOUR ACCOUNTID

def lambda_handler(event, context):
    try:
        # Retrieve order ID and status from the event
        order_id = event.get('order_id')
        status = event.get('status', 'Processed')
        
        # Create the message to send
        message = f"Order {order_id} status has been updated to {status}."
        
        # Publish the message to the SNS topic
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="Order Status Update"
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Notification sent for order {order_id}")
        }
    except ClientError as e:
        print(e.response['Error']['Message'])
        raise e
    except Exception as e:
        print(str(e))
        raise e
```


# Create send_notification Lambda Functions

```bash
$ touch src/send_notification.py
```

Python code
```python
import json
import boto3
from botocore.exceptions import ClientError

sns_client = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-1:123456789012:OrderNotifications' #UPDATE YOUR ACCOUNTID

def lambda_handler(event, context):
    try:
        # Retrieve order ID and status from the event
        order_id = event.get('order_id')
        status = event.get('status', 'Processed')
        
        # Create the message to send
        message = f"Order {order_id} status has been updated to {status}."
        
        # Publish the message to the SNS topic
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="Order Status Update"
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Notification sent for order {order_id}")
        }
    except ClientError as e:
        print(e.response['Error']['Message'])
        raise e
    except Exception as e:
        print(str(e))
        raise e
```

# Create handle_payment_error Lambda Functions

```bash
$ touch src/handle_payment_error.py
```

Python code
```python
import json

def lambda_handler(event, context):
    try:
        # Log the error and perform error handling
        print("Handling payment error for event:", event)
        
        # Simulate error handling logic
        return {
            'statusCode': 200,
            'body': json.dumps("Payment error handled successfully")
        }
    except Exception as e:
        print(str(e))
        raise e
```

# Define The State Machine Workflow

```json
{
          "Comment": "Payment processing workflow triggered via API Gateway",
          "StartAt": "ValidatePayment",
          "States": {
            "ValidatePayment": {
              "Type": "Task",
              "Resource": "${ValidatePaymentFunction.Arn}",
              "Next": "ProcessPayment"
            },
            "ProcessPayment": {
              "Type": "Task",
              "Resource": "${ProcessPaymentFunction.Arn}",
              "Retry": [
                {
                  "ErrorEquals": ["TransientError"],
                  "IntervalSeconds": 5,
                  "MaxAttempts": 3,
                  "BackoffRate": 2
                }
              ],
              "Catch": [
                {
                  "ErrorEquals": ["States.ALL"],
                  "Next": "HandlePaymentError"
                }
              ],
              "Next": "UpdatePaymentStatus"
            },
            "UpdatePaymentStatus": {
              "Type": "Task",
              "Resource": "${UpdatePaymentStatusFunction.Arn}",
              "Next": "SendNotification"
            },
            "SendNotification": {
              "Type": "Task",
              "Resource": "${SendNotificationFunction.Arn}",
              "End": true
            },
            "HandlePaymentError": {
              "Type": "Task",
              "Resource": "${HandlePaymentErrorFunction.Arn}",
              "Next": "UpdatePaymentStatus"
            }
          }
        }
```


# Create The SAM Template

```bash
$ touch template.yaml
```

# Build and Deploy the Application

Switch Python 3.12.4
```
$ pyenv install -l
$ pyenv install 3.12.4
$ pyenv global 3.12.4
$ pyenv versions
$ python --version
```


Build the App
```bash
$ sam build

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml
```

Deploy the App
```bash
$ sam deploy --guided --profile tvt_admin


CloudFormation stack changeset
---------------------------------------------------------------------------------------------------------
Operation                  LogicalResourceId          ResourceType               Replacement
---------------------------------------------------------------------------------------------------------
+ Add                      HandlePaymentErrorFuncti   AWS::IAM::Role             N/A
                           onRole
+ Add                      HandlePaymentErrorFuncti   AWS::Lambda::Function      N/A
                           on
+ Add                      OrderNotificationsTopic    AWS::SNS::Topic            N/A
+ Add                      OrdersTable                AWS::DynamoDB::Table       N/A
+ Add                      PaymentAPIDeployment6fea   AWS::ApiGateway::Deploym   N/A
                           a71a08                     ent
+ Add                      PaymentAPIGWRole           AWS::IAM::Role             N/A
+ Add                      PaymentAPIProdStage        AWS::ApiGateway::Stage     N/A
+ Add                      PaymentAPI                 AWS::ApiGateway::RestApi   N/A
+ Add                      PaymentProcessingStateMa   AWS::StepFunctions::Stat   N/A
                           chine                      eMachine
+ Add                      ProcessPaymentFunctionRo   AWS::IAM::Role             N/A
                           le
+ Add                      ProcessPaymentFunction     AWS::Lambda::Function      N/A
+ Add                      SendNotificationFunction   AWS::IAM::Role             N/A
                           Role
+ Add                      SendNotificationFunction   AWS::Lambda::Function      N/A
+ Add                      StepFunctionsExecutionRo   AWS::IAM::Role             N/A
                           le
+ Add                      UpdatePaymentStatusFunct   AWS::IAM::Role             N/A
                           ionRole
+ Add                      UpdatePaymentStatusFunct   AWS::Lambda::Function      N/A
                           ion
+ Add                      ValidatePaymentFunctionR   AWS::IAM::Role             N/A
                           ole
+ Add                      ValidatePaymentFunction    AWS::Lambda::Function      N/A
---------------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
-----------------------------------------------------------------------------------------------------------
Outputs
-----------------------------------------------------------------------------------------------------------
Key                 ApiUrl
Description         API Gateway endpoint URL for Prod stage
Value               https://2l56m7hpyd.execute-api.us-east-1.amazonaws.com/Prod/startPayment
-----------------------------------------------------------------------------------------------------------


Successfully created/updated stack - payment-processing in us-east-1
```

# Test the Application

```bash
curl -X POST https://<your-api-id>.execute-api.<region>.amazonaws.com/Prod/startPayment -d '{
  "payment_details": {
    "card_number": "4111111111111111",
    "expiry_date": "12/24",
    "cvv": "123",
    "amount": 100.0
  }
}' -H "Content-Type: application/json"
```

Example:
```bash
$ curl -X POST https://2l56m7hpyd.execute-api.us-east-1.amazonaws.com/Prod/startPayment -d '{
  "payment_details": {
    "card_number": "4111111111111111",
    "expiry_date": "12/24",
    "cvv": "123",
    "amount": 100.0
  }
}' -H "Content-Type: application/json"

{
  "statusCode": 200,
  "body": ""
}
```