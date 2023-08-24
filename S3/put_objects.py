import boto3

s3 = boto3.client('s3') #we set client variable to be s3, the resource.

#use 3 keys, including obj data as Body
#Body will need to be loaded in memory, so use with open
with open('test_text.txt', 'rb') as f: #read in bytes
    s3.put_object(Bucket='ameyer-boto3-051423', Key='test_text.txt'), Body='f')

