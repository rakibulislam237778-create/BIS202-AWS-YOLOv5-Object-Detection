import json

def lambda_handler(event, context):
    print("Event received:", event)

    return {
        'statusCode': 200,
        'body': json.dumps('API is working with Lambda')
    }
