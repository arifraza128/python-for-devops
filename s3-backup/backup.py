import boto3
import os
from datetime import datetime

# CONFIG
BUCKET_NAME = "your-bucket-name"
FOLDER_TO_BACKUP = "data/"

s3 = boto3.client('s3')

def upload_files():
    for root, dirs, files in os.walk(FOLDER_TO_BACKUP):
        for file in files:
            local_path = os.path.join(root, file)
            s3_path = f"backup/{datetime.now().strftime('%Y-%m-%d')}/{file}"

            try:
                s3.upload_file(local_path, BUCKET_NAME, s3_path)
                print(f"Uploaded {file} to S3")
            except Exception as e:
                print(f"Error uploading {file}: {e}")

if __name__ == "__main__":
    upload_files()
