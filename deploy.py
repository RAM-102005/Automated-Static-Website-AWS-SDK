import boto3
import os

BUCKET_NAME = "ram-automated-static-website-2026"

s3 = boto3.client("s3")

file_name = "index.html"

print("Uploading website to Amazon S3...")

s3.upload_file(
    file_name,
    BUCKET_NAME,
    "index.html",
    ExtraArgs={"ContentType": "text/html"}
)

print("Website uploaded successfully!")
