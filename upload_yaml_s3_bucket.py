import os
import sys
import boto3

# AWS credentials and S3 bucket configuration
aws_access_key = 'A*****************************K'
aws_secret_key = 'U******************A'

if len(sys.argv) != 3:
        print("Usage: upload_yaml_s3_bucket.py script.py <source_directory> <s3_bucket_name>")
        sys.exit(1)
        
# Specify the root directory to start traversing        
root_directory = sys.argv[1]

s3_bucket_name = sys.argv[2]
region_name = 'ap-south-1'  # Change to your desired region

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region_name)

# Function to upload a file to S3
def upload_to_s3(source_path, s3_key):
    try:
        s3.upload_file(source_path, s3_bucket_name, s3_key)
        print(f"Uploaded {source_path} to s3://{s3_bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading {source_path} to S3: {e}")

# Function to traverse directories and upload YAML files to S3
def upload_yaml_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.yaml') or file.lower().endswith('.yml'):
                file_path = os.path.join(root, file)
                s3_key = os.path.relpath(file_path, directory).replace("\\", "/")  # Convert to Unix-style path
                upload_to_s3(file_path, s3_key)

# Call the function to start uploading YAML files
upload_yaml_files(root_directory)
