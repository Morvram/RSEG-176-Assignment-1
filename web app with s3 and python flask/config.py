import boto
import os

S3 = 's3'
 
 
# creating the aws s3 client
# as a standard practice we are not hard-coding the aws access key id and secret key credentials here
# the credentials are defined in the .credentials file
def create_s3_client():
    os.chdir("C:\\Users\\joshu\\Dropbox\\Data Science Graduate Program\\Brandeis - Master's Strategic Analytics\\RSEG 176\\Assignment 1\\RSEG-176-Assignment-1\\web app with s3 and python flask") #or whatever working directory.
    with open('.credentials.txt') as f:
        lines = f.readlines()
    return boto3.client(S3,
        aws_access_key_id=lines[0],
        aws_secret_access_key=lines[1]
    )