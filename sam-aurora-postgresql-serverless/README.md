### AWS SAM Aurora PostgreSQL Serverless

AWS SAM example creates RDS Aurora PostgreSQL with serverless mode

| Keyword | Description                    |
|---------|--------------------------------|
| Author  | Jesús Alejandro Ambríz Bedolla |
| Email   | aambrizb@gmail.com             |
| Rev     | May/2025                       |

## Policies AWS

| Policy             |
|--------------------|
| SamFullAccess      |

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

# Role Policies Aurora ServerLess PostgreSQL

|                     |
|---------------------|
| rds:DescribeDBClusters  |
| rds:CreateDBCluster  |
| kms:*  |
| secretsmanager:*  |


# Run

```
sam build --profile aambrizb
sam validate --profile aambrizb
sam deploy --guided --profile aambrizb --guided
```