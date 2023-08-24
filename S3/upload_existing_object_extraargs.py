import boto3

s3 = boto3.client('s3') #we set client variable to be s3, the resource.

s3.upload_file('test_text.txt', 'ameyer-boto3-051423', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})

