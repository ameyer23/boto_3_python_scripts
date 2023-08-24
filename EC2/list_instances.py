"""
Note that describe is usually used to list various things

Here we find various things about an instance:
imageid, instance id, vpc id, subnetid, state, secruity group id, 
security group name, public IP, key pair name all from
parsing the response. 

We will look for instance profile role (IAM)

#if statements for output that is a string, it might not have one. Helps to 
avoid key error
"""

import boto3

ec2= boto3.client('ec2')

response = ec2.describe_instances()

#print(response) #to build our loop

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance['InstanceType'], 
        instance['ImageId'], instance['VpcId'], instance['SubnetId'],
        instance['State']['Name'])
        
        if 'Tags' in instance: #to avoid key error
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    print(tag['Value'])
        
        for security_group in instance['SecurityGroups']:
            print(security_group['GroupId'], security_group['GroupName'])
        
        if 'PublicIpAddress' in instance:
            print(instance['PublicIpAddress']) #to solve key error, IP
            
        if 'KeyName' in instance:
            print(instance['KeyName'])
        
        if 'IamInstanceProfile' in instance: #this yields the ARN of role
            print(instance['IamInstanceProfile'], 
                instance['IamInstanceProfile']['Id'], 
                instance['IamInstanceProfile']['Arn'])