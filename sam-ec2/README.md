### AWS SAM EC2

AWS SAM example creates a postgresql database

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

# Role Policies for EC2 / VPC

|                       |
|-----------------------|
| ec2:RunInstances  |
| ec2:CreateTags  |
| ec2:DescribeInstances        |

# Run

```
sam build --profile aambrizb
sam validate --profile aambrizb
sam deploy --guided --profile aambrizb --guided
```
