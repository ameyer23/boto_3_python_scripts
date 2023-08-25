"""
Modify created instance to launch an Apache web server. This is all about
user data and using it to spin up a web server on http.

We will use the create_instance script and add a function.

Our sg allows us to ssh into the new instance by running command below:
ssh -i key_from_boto3.pem ec2-user@18.206.179.12 (public ip of instance)
Note that if using ec2-user is for centos, use ubuntu if using that

Note script has yum since this is a centos distro. use apt if ubuntu.

"""
import boto3

def create_instance(client, ami_id, sg_id, key_pair_name, user_data=None):
    response = client.run_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key_pair_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            sg_id,
        ],
        UserData = user_data
    )
    
    print(response['Instances'][0]['InstanceId'])

ami_id = 'ami-0d382d38d7e58c250'
key_pair_name = 'key_from_boto3'
sg_id = 'sg-029feb50bd6aec827'

#for user data, code depends on the distro
#be sure to include -y
user_data = '''#!/bin/bash 
    sudo yum update -y
    sudo yum install httpd -y
    sudo systemctl start httpd
    sudo systemctl enable httpd'''

ec2= boto3.client('ec2')
create_instance(ec2, ami_id, sg_id, key_pair_name, user_data)


    