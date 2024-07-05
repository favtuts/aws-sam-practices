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