### AWS SAM EventBridge Custom Event Lambda

AWS SAM example creates Custom Event EventBridge and invoke Lambda

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

# Role Policies SES

|                     |
|---------------------|
| ses:SendEmail  |

# Run

```
sam build --profile aambrizb
sam validate --profile aambrizb
sam deploy --guided --profile aambrizb --guided
```

# Fail Events
```
aws events put-events --entries file://events/fail_event.json --profile aambrizb   
```

# Success Events
```
aws events put-events --entries file://events/success_event.json --profile aambrizb
```