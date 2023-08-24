"""
Passing in the permissions to allow traffic into ec2.

We will create the sg. NO rules here. 
"""
import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='SG from boto',
    GroupName='boto-security-group',
    VpcId='vpc-002f5af18e65786d0',
)

print(response['GroupId']) #to print groupid of new group

