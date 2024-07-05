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