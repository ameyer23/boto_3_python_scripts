"""
I used run_instances, which Launches the specified number of instances 
using an AMI for which you have permissions. This method provides
more granular control. We are using a Linux AMI.

This also prints out the instance id.

Note that create_instances is for creating instances in bulk.
"""
import boto3

ami_id = 'ami-051f7e7f6c2f40dc1'
key_pair_name = 'ameyermunoz-kp'
sg_id = 'sg-02bb1ca91368f93e0'

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
    