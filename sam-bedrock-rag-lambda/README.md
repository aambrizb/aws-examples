### AWS BedRock-Lambda-API-Gateway

AWS SAM example creates a invoke bedrock model although lambda function
I set region: us-east-1 because the model anthropic.claude-3-sonnet-20240229-v1:0 is not available in mx-central-1

It's necessary request permission for the model anthropic.claude-3-sonnet-20240229-v1:0 directly on AWS BedRock 


| Keyword | Description                    |
|---------|--------------------------------|
| Author  | Jesús Alejandro Ambríz Bedolla |
| Email   | aambrizb@gmail.com             |
| Rev     | May/2025                       |

## Policies AWS

| Policy        |
|---------------|
| SamFullAccess |
|               |

# Role Policies

|                       |
|-----------------------|
| iam:AttachRolePolicy  |
| iam:DetachRolePolicy  |
| iam:CreateRole        |
| iam:TagRole           |
| iam:GetRole           |
| iam:DeleteRole        |
| iam:CreatePolicy      |
| iam:PutRolePolicy     |


# Run

```
sam build --profile aambrizb
sam validate --profile aambrizb
sam local invoke --profile aambrizb
sam deploy --profile aambrizb --guided
```
