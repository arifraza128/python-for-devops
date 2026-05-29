import boto3

s3 = boto3.client('s3')

s3.create_bucket(
    Bucket='my-new-bucket-12345',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket created successfully")
