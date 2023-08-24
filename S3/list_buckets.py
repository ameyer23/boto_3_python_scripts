import boto3

s3 = boto3.client('s3') #we set client variable to be s3, the resource.

response = s3.list_buckets()

#contians all info from buckets
#this is not prettyprinted, do so to more easily see details 
buckets = response['Buckets'] 


print(buckets)

