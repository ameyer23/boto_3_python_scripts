"""
Subnets come with a default rt but but it's best practice to create and use
another. 
"""

import boto3

ec2 = boto3.client('ec2')

vpc_id = 'vpc-06a56934a663a6d4d'

routetable = ec2.create_route_table(VpcId=vpc_id)

print(routetable['RouteTable']['RouteTableId'])

