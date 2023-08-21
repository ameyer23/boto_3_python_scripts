"""
Creating route from internet gateway to created route table, that way our 
subnet has access to the internet, and vice versa. 

**Response metadata example, no = to response

**no output if all is well. Yields error otherwise.
"""

import boto3

ec2= boto3.client('ec2')

route_table_id = 'rtb-0af283feccf4ec99a'
igw_id = 'igw-0adc877990bffd96d'


ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',  #usually this is the IP for this
    GatewayId=igw_id,
    RouteTableId=route_table_id,
)

