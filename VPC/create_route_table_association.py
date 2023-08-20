"""
subnet we created is originally associated with default route table. 
We must now associate it with the new route table.
"""
import boto3

ec2= boto3.client('ec2')

routetable_id = 'rtb-0af283feccf4ec99a'
subnet_id = 'subnet-012c0f91cf7521526'


association = ec2.associate_route_table(
    RouteTableId=routetable_id,
    SubnetId=subnet_id
)

print(association['AssociationId'])