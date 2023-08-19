"""
Your module description
"""

import boto3

ec2 = boto3.client('ec2')

vpc  = ec2.create_vpc(CidrBlock='11.0.0.0/16',) #must specify cidr block, this IS the response 

print(vpc['Vpc'], ['VpcId'])