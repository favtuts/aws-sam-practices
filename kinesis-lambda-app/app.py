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
