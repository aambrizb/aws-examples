import json
import boto3

def lambda_handler(event, context):

    # bedrock-runtime is not available in mx-central-1 but whether in us-east-1
    bedrock = boto3.client("bedrock-runtime",region_name="us-east-1")

    payload = {
        "messages": [
            {"role": "user", "content": "Explain to me what is RAG in 10 seconds"}
        ],
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300
    }

    response = bedrock.invoke_model(
        modelId     = 'anthropic.claude-3-sonnet-20240229-v1:0',
        contentType = 'application/json',
        accept      = 'application/json',
        body        = json.dumps(payload)
    )

    result = json.loads(response['body'].read())

    print(result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "answer": result['content'][0]['text']
        }),
    }
