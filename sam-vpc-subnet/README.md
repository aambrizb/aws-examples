### AWS SAM VPC, Subnet, Gateway

AWS SAM example creates a VPC environment

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

# Role Policies for VPC

|                       |
|-----------------------|
| ec2:CreateVpc  |
| ec2:DeleteVpc  |
| ec2:DescribeVpcs        |
| ec2:CreateSubnet           |
| ec2:DeleteSubnet           |
| ec2:ModifySubnetAttribute        |
| ec2:DescribeSubnets      |
| ec2:CreateInternetGateway     |
| ec2:DeleteInternetGateway     |
| ec2:AttachInternetGateway     |
| ec2:DescribeInternetGateways     |
| ec2:CreateRouteTable     |
| ec2:CreateRoute     |
| ec2:AssociateRouteTable     |
| ec2:DescribeRouteTables     |
| ec2:ModifyVpcAttribut     |
| ec2:DescribeAvailabilityZones     |


# Run

```
sam build --profile aambrizb
sam validate --profile aambrizb
sam deploy --guided --profile aambrizb --guided
```
