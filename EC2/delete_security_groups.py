
import boto3

ec2= boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-029feb50bd6aec827',
)

print(response)