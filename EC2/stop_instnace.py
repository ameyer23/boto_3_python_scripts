"""
This script is for stopping a running instance
"""

import boto3

instance_id = 'i-073075cbf96f5bd8b'
ec2= boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
       instance_id,
    ],
)

print(response)


