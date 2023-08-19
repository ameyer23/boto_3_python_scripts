"""
List Vpcs, describe them
"""

'''
#list all VPCs

import boto3

ec2= boto3.client('ec2')

response = ec2.describe_vpcs()

#print(response) to see output and write loop

for vpc in response['Vpcs']:
    print(vpc['VpcId'], vpc['CidrBlock'], vpc['IsDefault'])

for vpc in response['Vpcs']:
    if 'Tags' in vpc:
        for tag in vpc['Tags']:
            if 'Name' == tag['Key']:
                print(tag['Value'])
'''

#Filtering for specific vpc, Name here is DefaultVPC

import boto3

def get_vpc_information(client, filter=[]):
    response = ec2.describe_vpcs(Filters = filter)
    for vpc in response['Vpcs']:
        print(vpc['VpcId'], vpc['CidrBlock'], vpc['IsDefault'])
        
def get_vpc_name(client, filter=[]):
    response = ec2.describe_vpcs(Filters= filter)
    for vpc in response['Vpcs']:
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if 'Name' == tag['Key']:
                    print(tag['Value'])

if __name__ == '__main__':
    ec2 = boto3.client('ec2')

    ec2= boto3.client('ec2')
    
    Filters=[{'Name': 'isDefault','Values': ['true',]},]
    
    get_vpc_information('ec2')
    get_vpc_information('ec2', Filters) #just the default VPC