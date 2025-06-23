import boto3
import time
import json

GROUP_NAME = "core.domain.com"
LOG_STREAM = "script_pendientes"
ACCESS_KEY = "key"
SECRET_KEY = "secret"

client = boto3.client(
  "logs",
  region_name           = 'us-east-1',
  aws_access_key_id     = ACCESS_KEY,
  aws_secret_access_key = SECRET_KEY,
)

try:
  client.create_log_group(logGroupName=GROUP_NAME)
except Exception as ex:
  print(ex)

try:
  client.create_log_stream(
    logGroupName  = GROUP_NAME,
    logStreamName = LOG_STREAM
  )
except Exception as ex:
  print(ex)

streams = client.describe_log_streams(
  logGroupName        = GROUP_NAME,
  logStreamNamePrefix = LOG_STREAM
)

SEQUENCE_TOKEN = streams['logStreams'][0].get('uploadSequenceToken')

timestamp = int(time.time() * 1000)

event = {
  'app'     : 'app',
  'module'  : 'module',
  'message' : "Text Log example"
}

log_event = {
  'timestamp' : timestamp,
  'message'   : json.dumps(event)
}

kwargs = {
  'logGroupName'  : GROUP_NAME,
  'logStreamName' : LOG_STREAM,
  'logEvents'     : [log_event]
}

response = client.put_log_events(**kwargs)
print(response)