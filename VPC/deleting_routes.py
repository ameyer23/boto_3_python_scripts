"""
This disconnects internet gateway from route table.

To delete a VPC, first must delete components. See order below

1.  delete routes
"""
import boto3

ec2= boto3.client('ec2')

route_table_id = 'rtb-0af283feccf4ec99a'

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id,
)

