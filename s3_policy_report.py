import boto3
import sys


s3 = boto3.resource('s3',
         aws_access_key_id=sys.argv[1],
         aws_secret_access_key=sys.argv[2])

for bucket in s3.buckets.all():
    bucketTest = ""
    acl = bucket.Acl()
    for grant in acl.grants:
        if (grant['Grantee']['Type']) == 'Group':
            if bucket.name != bucketTest:
                bucketTest = bucket.name
                print("S3 Bucket: " + bucket.name +" has Group Access.  Potential Access Control Concern.")