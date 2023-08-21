
import boto3

ec2= boto3.client('ec2')

igw_id = 'igw-0adc877990bffd96d'

ec2.delete_internet_gateway(
    InternetGatewayId=igw_id,
)

