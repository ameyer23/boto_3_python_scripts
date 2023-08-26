#list all running instances
import boto3

#do not stop this cloud9 instance
excluded_instance_id = 'i-0e3ac43d9f97d0a68' 
ec2= boto3.client('ec2')

#response will be parsed to create logic
response = ec2.describe_instances()

#prints out all running instances
for reservation in response['Reservations']: 
    for instance in reservation['Instances']:
        if  instance['State']['Name']=='running': #check for running instances
            if instance['InstanceId'] != excluded_instance_id: #exclude cloud9
                response = ec2.stop_instances(
                InstanceIds=[
                instance['InstanceId'],
                ],
            )
            print(f"Stopping instance {instance['InstanceId']}")

            
            