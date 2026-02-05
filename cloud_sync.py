import boto3
import os.path
import logging

from botocore.exceptions import ClientError


def cloud_upload(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_bucket = boto3.client('s3')
    try:
        response = s3_bucket.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True