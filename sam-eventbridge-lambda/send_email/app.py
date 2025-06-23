import json
import boto3

SES        = boto3.client("ses",region_name="us-east-1")
EMAIL_FROM = "noreply@domain.com"
EMAIL_TO   = "aambrizb@gmail.com"
SUBJECT    = "[CREATED] Object has created S3"

def lambda_handler(event, context):

  try:

    bucket_name = ""
    object_key  = ""

    if event and 'detail' in event:
      bucket_name = event["detail"]["bucket"]["name"]
      object_key  = event["detail"]["object"]["key"]

    text = f"""
      Event. S3 Created
      BucketName: {bucket_name}
      Object: {object_key}
    """

    response = SES.send_email(
      Source=EMAIL_FROM,
      Destination={
        "ToAddresses":[EMAIL_TO],
      },
      Message={
        "Subject":{"Data":SUBJECT},
        "Body":{
          "Text":{"Data":text}
        }
      }
    )

    return {"statusCode":200,"body":"Send email successfully"}

  except Exception as ex:
    return {"statusCode":500,"body":str(ex)}
