# SAM - DJANGO FARGATE

## Policies ECR

| Policies             |
|----------------------|
| ecr:CreateRepository |
|                      |


## Create Repository

```
aws ecr create-repository --repository-name sam_django_fargate --region us-east-1 --profile aambrizb
```

## Build Image

```
docker build -t sam_django_fargate .
```

## Authenticated ECR Docker (use repositoryUri)

```
aws ecr get-login-password --region us-east-1 --profile aambrizb | docker login --username AWS --password-stdin 981539705167.dkr.ecr.us-east-1.amazonaws.com/sam_django_fargate
```

## Tag Image
```
docker tag sam_django_fargate:latest 981539705167.dkr.ecr.us-east-1.amazonaws.com/sam_django_fargate:latest
```
## Push Image

```
docker push 981539705167.dkr.ecr.us-east-1.amazonaws.com/sam_django_fargate
```

## List Images

```
aws ecr list-images --repository-name sam_django_fargate --region us-east-1 --profile aambrizb 
```

## CloudFormation

```
aws cloudformation deploy --template-file template.yaml --stack-name sam-django-fargate --capabilities CAPABILITY_NAMED_IAM --region us-east-1 --profile aambrizb
```

## See errors CloudFormation

```
aws cloudformation describe-stack-events --stack-name sam-django-fargate --profile aambrizb
```

