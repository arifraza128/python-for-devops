import boto3

s3 = boto3.client('s3')

s3.delete_object(
    Bucket='my-bucket-name',
    Key='uploads/test.txt'
)

print("File deleted successfully")
