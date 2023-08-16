import boto3

s3 = boto3.client('s3') #we set client variable to be s3, the resource.

with open('test_text.txt', 'rb') as f: #read in bytes
    s3.put_object(Bucket='ameyer-boto3-051423', Key='test_text.txt', Body=f, 
    ContentType='text/plain')


#put_obj added it to inmemory
#use keys, including obj data as Body
#this will add test_text file to the bucket
#be sure to change CWD to correct dir
#Body will need to be loaded in memory, so use with open
#ContentType is the MIME type, determined by file extension


