"""
Listing the AMi and instance type are necessary for launching an instance
"""

import boto3

ec2= boto3.client('ec2')

response = ec2.describe_instance_types()
    
print(response)
        
for instance in response['InstanceType']:
    print(instance['InstanceType'])