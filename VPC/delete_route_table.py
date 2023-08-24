"""
We are deleting the route table we created, leaving the default behind
"""

import boto3

ec2= boto3.client('ec2')

route_table_id = 'rtb-0af283feccf4ec99a' #this is the new RT


ec2.delete_route_table(
    RouteTableId=route_table_id,
)

