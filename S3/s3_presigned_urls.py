'''
Presigned URLS grant temp access/authentication to objects in s3 buckets
-useful for when you don't want a pub bucket but you need to share object
for temporary access.

'''

import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket':'ameyer-boto3-051423', 'Key': 'test_text_upload.txt'}, ExpiresIn=360)

print(response)