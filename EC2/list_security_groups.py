"""
Security groups are used to allow traffic into and out of an instance.
They belong to a VPC.

Here, we got security group Id, name, VPC info, routes (permissions) for a 
particular security group (ports), IP protocol, to port (where it's going), 
IP cidr range (where is it coming from)
"""

import boto3

ec2= boto3.client('ec2')

response = ec2.describe_security_groups()

#print(security_groups) # this is the response

for sg in response['SecurityGroups']:
    print(sg['GroupId'], sg['VpcId'], sg['GroupName'], sg['Description'])
    
    for permission in sg['IpPermissions']:
        if 'FromPort' in permission: #to fix NameError
            print(permission['FromPort'])
        
        if 'IpProtocol' in permission:
            print(permission['IpProtocol'])
            
        if 'ToPort' in permission:
            print(permission['ToPort'])
        
        if 'IpRanges' in permission:
            for iprange in permission['IpRanges']:
                print(iprange['CidrIp'])