'''
Functions to start, stop, terminate instances
'''

import boto3

instance_id = 'i-073075cbf96f5bd8b'

def stop_instance(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
           instance_id,
        ],
    )
    
    print(instance_id, 'is stopped.')

#note we kept the client in this response, is better practice
def start_instance(client, instance_id): 
    response = client.start_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print(instance_id, 'is started.')

def start_instance(client, instance_id): 
    response = client.start_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print(instance_id, 'is started.')
    
def terminate_instance(client, instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print(instance_id, 'is terminated.')
    
if __name__ == '__main__':
    instance_id = 'i-073075cbf96f5bd8b'

    ec2= boto3.client('ec2')
    
    #function calls below
    #start_instnace(ec2, instance_id) 
    #stop_instance(ec2, instance_id)
    terminate_instance(ec2, instance_id)
    
    