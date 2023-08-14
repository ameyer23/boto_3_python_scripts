import boto3

s3 = boto3.client('s3') #we set client variable to be s3, the resource

response = s3.list_buckets()

buckets = response['Buckets'] #contians all info from buckets

for bucket in buckets: #lists bucket names and creation data from our account
    print (bucket['Name'], bucket['CreationDate'])

