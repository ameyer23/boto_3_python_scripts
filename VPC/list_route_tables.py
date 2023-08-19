"""
Route tables handle connections between subnets and gateways
"""

import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()
#print(response)

for routetable in response['RouteTables']:
    print(routetable['VpcId'], routetable['RouteTableId'])

    for assoc in routetable['Associations']:
        print(assoc['RouteTableAssociationId']) 
        if 'SubnetId' in assoc: #since it is not autoamatically included, #solved key error
            print(assoc['SubnetId'])
        
    for route in routetable['Routes']:
        if 'GatewayId' in route: #solved key error, PROUD MOMENT 
            print(route['DestinationCidrBlock'], route['GatewayId'])
        
      