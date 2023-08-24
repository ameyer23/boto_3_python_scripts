import boto3

s3 = boto3.client('s3') #we set client variable to be s3, the resource

#create bucket
response = s3.create_bucket(
    Bucket='ameyer-boto3-051423', #give globally unique bucket name 
)

print(response) #pass this output to a json formatter