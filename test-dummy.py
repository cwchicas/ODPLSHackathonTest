import boto3
s3 = boto3.client("s3")          # picks up env vars & region
print(s3.list_buckets())