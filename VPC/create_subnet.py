"""
Your module description
"""

import boto3

ec2 = boto3.client('ec2')

cidr_block = '11.0.1.0/24'
vpc_id='vpc-06a56934a663a6d4d'

#below is reponse called subnet
subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

print(subnet['Subnet']['SubnetId']) #use to parse out response