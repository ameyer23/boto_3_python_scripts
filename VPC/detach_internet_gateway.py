"""
Detach igw from VPC.
"""

import boto3

ec2= boto3.client('ec2')

igw_id = 'igw-0adc877990bffd96d'
vpc_id = 'vpc-06a56934a663a6d4d'

ec2.detach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_id,
)

