"""
I used run_instances, which Launches the specified number of instances 
using an AMI for which you have permissions. This method provides
more granular control.

This also prints out the instance id.

Note that create_instances is for creating instances in bulk.
"""
import boto3

ami_id = 'ami-0d382d38d7e58c250'
key_pair_name = 'key_from_boto3'
sg_id = 'sg-029feb50bd6aec827'

ec2= boto3.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        sg_id,
    ],
)

#print(response) #parse this out to get instance id
print(response['Instances'][0]['InstanceId'])
    