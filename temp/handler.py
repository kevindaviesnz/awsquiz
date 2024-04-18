import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus

import pydantic as py

from PIL import Image
import PIL.Image

s3_client = boto3.client("s3")


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        print(f"original image size {image.size}")
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(resized_path)
        print(f"thumbnail image size {image.size}")


def create_thumbnail(event, context):
    try:
        for record in event["Records"]:
            bucket_name = record["s3"]["bucket"]["name"]
            original_s3_path = unquote_plus(record["s3"]["object"]["key"])

            print(f"The image name is s3://{bucket_name}/{original_s3_path}")
            destination_s3_path = original_s3_path.replace("uploads", "thumbnails", 1)
            # original = uploads/kitty-cat-kitten-pet-45201.jpg
            # destination = thumbnails/kitty-cat-kitten-pet-45201.jpg
            print(f"The thumbnail name is s3://{bucket_name}/{destination_s3_path}")

            tmpkey = original_s3_path.replace("/", "")
            # adding uuid4 to make sure we process an unique object locally to Lambda
            local_download_path = "/tmp/{}{}".format(uuid.uuid4(), tmpkey)
            print(f"The local image name is {local_download_path}")
            local_upload_path = "/tmp/resized-{}".format(tmpkey)
            print(f"The local thumbnail name is {local_upload_path}")

            s3_client.download_file(bucket_name, original_s3_path, local_download_path)

            resize_image(local_download_path, local_upload_path)

            s3_client.upload_file(local_upload_path, bucket_name, destination_s3_path)

    except Exception as e:
        print(e)
