"""
Listing the AMi and instance type are necessary for launching an instance

**output of response was messy, so we used the response from the documentation
"""
        
import boto3

ec2= boto3.client('ec2')

response = ec2.describe_instance_types(
    Filters=[
        {
            'Name': 'free-tier-eligible',
            'Values': [
                'true',
            ]
        },
    ]
    
    )
    
#print(response)
        
for instance_type in response['InstanceTypes']:
    print(instance_type['InstanceType'], instance_type['FreeTierEligible'])