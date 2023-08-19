'''
Internet gateways are how subnets access the internet thorugh a route table
'''

import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_internet_gateways()

#print(response) #to get json and create our loops

for ig in response['InternetGateways']:
    print(ig['InternetGatewayId'])
    for attachements in ig['Attachments']:
        print(attachements['VpcId'], attachements['State'])