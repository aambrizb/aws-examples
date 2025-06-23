### AWS SAM (Serverless Application Model) Lambda

This example creates a basic lambda with api-gateway on AWS Services.
Change your --profile tag depending on your environment.

| Keyword | Description                    |
|---------|--------------------------------|
| Author  | Jesús Alejandro Ambríz Bedolla |
| Email   | aambrizb@gmail.com             |
| Rev     | May/2025                       |

## Required Policies

| Policy        |
|---------------|
| SamFullAccess |
|               |

# Required Role Policies

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
