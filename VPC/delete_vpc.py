"""
Your module description
"""
import boto3

ec2= boto3.client('ec2')

vpc_id = 'vpc-06a56934a663a6d4d'

ec2.delete_vpc(
    VpcId=vpc_id,
)

