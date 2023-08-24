"""
Key pairs are necessary for SSHing into instances.

Here, we got the key pair name and ID

"""

import boto3

ec2= boto3.client('ec2')

response = ec2.describe_key_pairs()

#print(response)

for key_pair in response['KeyPairs']:
    print(key_pair['KeyName'], key_pair['KeyPairId'])