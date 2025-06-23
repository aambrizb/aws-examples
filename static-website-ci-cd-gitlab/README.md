# static-website-ci-cd-gitlab

Example CI/CD Gitlab on AWS S3 Bucket


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
## Installation Runner
```
curl -L --output gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-$(uname -s | tr '[:upper:]' '[:lower:]')-amd64
chmod +x gitlab-runner
sudo mv gitlab-runner /usr/local/bin/
```

## Register Runner
```
gitlab-runner register
```

## List Runners
```
gitlab-runner list
```

## Run Runners
```
gitlab-runner run
```


## Configuration
### CI/CD
#### Variables

| Variable              | Description           |
|-----------------------|-----------------------|
| AWS_ACCESS_KEY_ID     | AWS Access Key ID     |
| AWS_SECRET_ACCESS_KEY | AWS Secret Access Key |
| AWS_DEFAULT_REGION    | AWS Default Region    |
| S3_BUCKET_NAME        | AWS S3 Bucket Name    |
|                       |                       |
