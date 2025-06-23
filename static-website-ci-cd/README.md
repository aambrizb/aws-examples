# AWS S3 static-website-ci-cd

AWS Example CI/CD on commit update S3 bucket


| Keyword | Description                    |
|---------|--------------------------------|
| Author  | Jesús Alejandro Ambríz Bedolla |
| Email   | aambrizb@gmail.com             |
| Rev     | May/2025                       |


## Policies

| Policy        |
|---------------|
| AmazonS3FullAccess |
|               |

## Variables 
### Secrets and Variables 
#### Actions
##### Repository Secrets

| Descripcion              | Valor                 |
|--------------------------|-----------------------|
| AWS_ACCESS_KEY_ID        | AWS Access Key ID     |
| AWS_SECRET_ACCESS_KEY    | AWS Secret Access Key |
| AWS_REGION               | AWS Región            |
| S3_BUCKET                | Nombre del Bucket     |
| STACK_NAME               | Nombre del Stack      |


## Push to Repository

```
git push origin main
```

## Result

```
Endpoint. http://<bucket>.s3-website.<region>.amazonaws.com/
```
