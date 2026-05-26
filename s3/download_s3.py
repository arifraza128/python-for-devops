import boto3

s3 = boto3.client('s3')

s3.download_file(
    'my-bucket-name',
    'uploads/test.txt',
    'downloaded.txt'
)

print("File downloaded successfully")
