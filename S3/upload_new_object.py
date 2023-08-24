'''
#Upload new single object

import boto3

s3 = boto3.client('s3') #we set client variable to be s3, the resource.

s3.put_object(Bucket='ameyer-boto3-051423', 
                Key='test_text_string.txt', 
                Body='this is a string', 
                ContentType='text/plain') #no need to read in file, Body is string directly

'''


#Upload object to new folder
#delete contents of foldera, but not folder1
import boto3

s3 = boto3.client('s3') #we set client variable to be s3, the resource.

s3.put_object(Bucket='ameyer-boto3-051423', 
                Key='folder/test_text_string.txt', 
                Body='this is a string', 
                ContentType='text/plain') #no need to read in file, Body is string directly

