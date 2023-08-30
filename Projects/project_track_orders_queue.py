import boto3

#create sqs queue
sqs= boto3.resource('sqs')

response = sqs.create_queue(
    QueueName='orders_queue',
)

print(response.url)