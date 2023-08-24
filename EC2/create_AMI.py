"""
Creating an AMI from an existing instance

"""

import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-091de3d45c4915203',
    Name='new_image')

print(response['ImageId'])
