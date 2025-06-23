#!/bin/bash

BUCKET_NAME=$1
REGION=$2
PROFILE=$3

if [ -z "$BUCKET_NAME" ] || [ -z "$REGION" ]; then
  echo "Use: ./create-bucket-wwww.sh <bucket-name> <region> <profile>"
  exit 1
fi

# Create Bucket

aws s3api create-bucket \
  --bucket "$BUCKET_NAME" \
  --region "$REGION" \
  --profile $PROFILE \
  $( [ "$REGION" != "us-east-1" ] && echo "--create-bucket-configuration LocationConstraint=$REGION" )

# Assign Website

echo "[*] Create bucket"

aws s3 website "$BUCKET_NAME" \
  --index-document index.html \
  --error-document index.html \
  --profile $PROFILE

# Unblock public access
echo "[*] Public Access Block"
aws s3api put-public-access-block \
  --bucket "$BUCKET_NAME" \
  --public-access-block-configuration \
    BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false \
  --profile $PROFILE

# Policy
echo "[*] Policy"
aws s3api put-bucket-policy \
  --bucket "$BUCKET_NAME" \
  --policy "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Sid\": \"PublicReadGetObject\",
      \"Effect\": \"Allow\",
      \"Principal\": \"*\",
      \"Action\": \"s3:GetObject\",
      \"Resource\": \"arn:aws:s3:::$BUCKET_NAME/*\"
    }]
  }" \
  --profile $PROFILE

# Sync Files
aws s3 sync ./www s3://$BUCKET_NAME --profile $PROFILE

# Export
echo "URL: http://$BUCKET_NAME.s3-website.$REGION.amazonaws.com"
