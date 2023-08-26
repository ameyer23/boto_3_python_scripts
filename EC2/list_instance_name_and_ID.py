#list all running instances
import boto3

ec2= boto3.client('ec2')

#response will be parsed to create logic
response = ec2.describe_instances()

#prints out all running instances
for reservation in response['Reservations']: 
    for instance in reservation['Instances']:
        if  instance['State']['Name']=='running': #check for running instances
            print(instance['InstanceId'], instance['InstanceType'], 
            instance['ImageId'],)
                
            if 'Tags' in instance: #if instance has a name, print that too
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        print(tag['Value'])
            
            