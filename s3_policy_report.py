import boto3

s3 = boto3.resource('s3',
         aws_access_key_id='AKIAJEZIELFAW45OGCNA',
         aws_secret_access_key='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')

for bucket in s3.buckets.all():
    # print(bucket.name)
    bucketTest = ""
    acl = bucket.Acl()
    for grant in acl.grants:
        if (grant['Grantee']['Type']) == 'Group':
            if bucket.name != bucketTest:
                bucketTest = bucket.name
                print("S3 Bucket: " + bucket.name +" has Group Access.  Potential Access Control Concern.")
