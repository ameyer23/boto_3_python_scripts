import boto3
import json
import random


def lambda_handler(event, context):
    
    random_number = (random.randint(0,9))
    
    sqs = boto3.client('sqs')
    sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/763912099305/orders_queue',
    MessageBody=str(random_number),
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(random_number)