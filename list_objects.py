import boto3

def filter_objects_on_extension(client, bucket, extension):
    keys=[]
    response = client.list_objects_v2(Bucket=bucket)
    for content in response['Contents']:
        if (extension in content['Key'][(-len(extension)):]):
            keys.append(content['Key'])
    
    return keys

def list_object_keys(client, bucket, prefix=''):
    keys=[]
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response['Contents']:
        keys.append(content['Key'])
    
    return keys


if __name__ == '__main__':
    s3 = boto3.client('s3')

    response = list_object_keys(s3, 'ameyer-boto3-051423', 'folder/')
    print(response)
    
    response = filter_objects_on_extension(s3, 'ameyer-boto3-051423', '/')
    print(response)


'''
import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket='ameyer-boto3-051423')

extension = '.txt'

for content in response['Contents']:
    if (extension in content['Key'][(-len(extension)):]):
        print(content['Key'])
'''




'''
import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket='ameyer-boto3-051423')

for content in response['Contents']:
    if ('.txt' in content['Key'][-4:]):
        print(content['Key'])
'''




'''
import boto3

s3 = boto3.client('s3')xs

response = s3.list_objects_v2(Bucket='ameyer-boto3-051423')
#to add filters and search specific folders, see below
#response = s3.list_objects_v2(Bucket='ameyer-boto3-051423', Prefix='folder/folder_a/')

#print(response) #use json formatter with this outpiut

#we will need to parse response based on contents key (has what we need)
#lists out all contents of the bucket, recursively
#shows forlder and allll its contents
for content in response['Contents']:
    print(content['Key'])
'''






