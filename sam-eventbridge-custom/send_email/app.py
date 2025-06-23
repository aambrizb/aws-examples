import json
import boto3

SES        = boto3.client("ses",region_name="us-east-1")
EMAIL_FROM = 'noreply@domain.com'
EMAIL_TO   = 'aambrizb@gmail.com'
SUBJECT    = 'Custom EventBridge'

def lambda_handler(event, context):

  text = f"""
    Custom EventBridge:
    {json.dumps(event)}
    """

  try:
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

    return {"statusCode": 200, "body": "Invoked successfully"}

  except Exception as ex:
    return {"statusCode": 500,"body": str(ex)}