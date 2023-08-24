"""
Note that keypairs have to be saved to a file, so we will use KeyMaterial
from the response.ArithmeticError
We are writing and saving our kp file.
For UNIX systems, we must change permissions of file to 400.
"""
import boto3
import os #for permissions

file_name = 'key_from_boto3.pem' #to save kp file
key_name = 'key_from_boto3'

ec2 = boto3.client('ec2')

response = ec2.create_key_pair(
    KeyName=key_name,
)

#below is to write directly to a file
with open(file_name, 'w') as f:
    f.write(response['KeyMaterial'])
    
os.chmod(file_name, 0o400)
