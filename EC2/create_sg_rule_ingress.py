"""
Changes rules for going INTO sg

We are adding ssh and http access
"""


import boto3

security_group_id = 'sg-029feb50bd6aec827'

ec2= boto3.client('ec2')

response = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0', #from anywhere
                },
            ],
            'ToPort': 22,
        },
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0', #from anywhere
                },
            ],
            'ToPort': 80,
        }
    ],
)

print(response)