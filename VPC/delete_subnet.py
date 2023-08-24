"""
Your module description
"""
import boto3

ec2= boto3.client('ec2')

subnet_id = 'subnet-012c0f91cf7521526'

ec2.delete_subnet(
    SubnetId=subnet_id,
)

