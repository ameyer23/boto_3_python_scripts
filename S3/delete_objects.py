'''
#Deleting single object


import boto3

bucket = 'ameyer-boto3-051423'
key = 'test_text.txt'

s3 = boto3.client('s3')

response = s3.delete_object(
    Bucket=bucket,
    Key=key
)
'''

'''
#Deleting mutiple objects with a fn: ONE WAY

import boto3

def delete_object(client, bucket, key):
    response = s3.delete_object(
        Bucket=bucket,
        Key=key
    )
    
bucket = 'ameyer-boto3-051423'
key = 'test_text.txt'

s3 = boto3.client('s3')

keys = ['test_text_string.txt', 'est_text_upload.txt']

for key in keys:
    delete_object(s3, bucket, key)
'''


'''
#Deleting mutiple objects, ANOTHER way
import boto3

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )
    
    return response

def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    
    return response
    
bucket = 'ameyer-boto3-051423'
key = 'test_text.txt'

s3 = boto3.client('s3')

keys = ['test_text_string.txt', 'test_text_upload.txt']

delete_objects(s3, bucket, keys)

'''

'''
#Deleting Nested Objects, within a folder, recursive folders
#using list_objects fn we had from before
#folder/ is the name of the folder
#also deletes the root folder 

import boto3
from list_objects import list_object_keys

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )
    
    return response

def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    
    return response

if __name__ == '__main__':
    bucket = 'ameyer-boto3-051423'

    s3 = boto3.client('s3')
    
    keys = list_object_keys(s3, bucket, prefix='folder/')
    delete_objects(s3, bucket, keys)    
 '''
 

    
#Deleting single folder, NOT recursive folders
import boto3
from list_objects import list_object_keys

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )
    
    return response

def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    
    return response

if __name__ == '__main__':
    bucket = 'ameyer-boto3-051423'
    prefix = 'folder/foldera/'
    s3 = boto3.client('s3')
    
    keys = list_object_keys(s3, bucket, prefix=prefix)
    print(keys)
    keys = [key for key in keys if '/' in key[len(prefix):]]
    print(keys)
    delete_objects(s3, bucket, keys)   

    
    
