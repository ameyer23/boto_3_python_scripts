"""
lists AMIs created by amazon and their ID and creation date, name

#self would show those created by you
"""

import boto3

ec2= boto3.client('ec2')

response = ec2.describe_images(Owners = ['self'])

#print(response)


for image in response['Images']:
    print(image['ImageId'], image['CreationDate'], image['Name'])