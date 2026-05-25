import boto3


s3 = boto3.client('s3')

# Upload file
s3.upload_file(
    'test.txt',
    'my-bucket-name',
    'uploads/test.txt'
)

print("File uploaded successfully")
