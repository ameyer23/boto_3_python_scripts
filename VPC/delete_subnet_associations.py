"""
delete association between subnet and route table.

This requires getting the association id separately using describe_route_tables, 
and its filter
"""
'''
Delete subnet association with a route table
Diassociate subet from created route table, see Main not True
'''
###GO OVER THIS VIDEO AGAIN FOR FIRST BLOCK OF CODE

import boto3

ec2= boto3.client('ec2')

route_table_id ='rtb-0af283feccf4ec99a'

#all of the below creates the association id we need for the dissociate_route
#fn shown in the block after this one
response = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id,
    ],
)

#parse out association from describe_route_tables
for association in response['RouteTables'][0]['Associations']:
    if not association['Main']:
        association_id = association['RouteTableAssociationId']
        print(association_id) #peints out the association id we found 
        ec2.disassociate_route_table(
            AssociationId=association_id,
        )
        
