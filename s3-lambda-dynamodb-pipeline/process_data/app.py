import json
import boto3
import os
import uuid

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    for record in event['Records']:
        s3_object = record['s3']['object']
        bucket = record['s3']['bucket']['name']
        key = s3_object['key']

        # Get the object from S3
        s3_client = boto3.client('s3')
        response = s3_client.get_object(Bucket=bucket, Key=key)
        data = response['Body'].read().decode('utf-8')

        # Process data (example: assume data is in JSON format)
        processed_data = process_data(json.loads(data))

        # Store the result in DynamoDB
        table.put_item(Item=processed_data)

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed S3 event data')
    }

def process_data(data):
    # Implement your data processing logic here
    # Example: adding an id to the data
    data['id'] = str(uuid.uuid4())
    return data