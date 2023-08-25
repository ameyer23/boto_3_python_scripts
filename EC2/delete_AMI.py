
import boto3

ec2= boto3.client('ec2')

response = ec2.deregister_image(
    ImageId='ami-0d382d38d7e58c250',
    )