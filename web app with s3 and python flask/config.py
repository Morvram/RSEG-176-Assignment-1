import boto

S3 = 's3'
 
 
# creating the aws s3 client
# as a standard practice we are not hard-coding the aws access key id and secret key credentials here
# the credentials are defined in the .credentials file
def create_s3_client():
    return boto3.client(S3)