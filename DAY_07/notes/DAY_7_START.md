# Day 7: AWS Fundamentals - Quick Start Guide

> **🚀 Fast track to AWS cloud deployment in 8 hours!**

---

## ⚡ Quick Overview

**What you'll achieve today:**
- ✅ AWS account with professional security setup
- ✅ First EC2 web server running
- ✅ Portfolio website hosted on S3
- ✅ Custom VPC with networking
- ✅ 3-tier production application
- ✅ Cost monitoring and optimization

**Time:** 8 hours | **Cost:** $0 (Free Tier) | **Projects:** 2

---

## 🎯 Why AWS Today?

### **Career Impact:**
- 90% of DevOps jobs require AWS experience
- AWS skills add 15-25% salary premium
- Cloud migration is #1 enterprise priority
- Gateway to 20+ LPA roles

### **What Makes This Different:**
Unlike tutorials that just show you buttons to click, you'll:
- ✅ **Automate everything** with AWS CLI
- ✅ **Understand security** from day one
- ✅ **Deploy real applications** not hello-world
- ✅ **Learn cost optimization** to stay in free tier
- ✅ **Build portfolio** with live projects

---

## 📋 Pre-Flight Checklist

### **Before You Start:**

```bash
# 1. Check AWS CLI installation
aws --version
# Expected: aws-cli/2.x.x or higher

# 2. If not installed (macOS):
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

# 3. Verify installation
aws --version
```

### **What You'll Need:**
- [ ] Valid email address (for AWS account)
- [ ] Credit/debit card (won't be charged with Free Tier)
- [ ] Phone number (for verification)
- [ ] 8 hours of focused time
- [ ] Notebook for tracking resources

### **Mindset:**
- 💪 **Hands-on first** - Learn by doing
- 🔍 **Security-conscious** - Never compromise
- 💰 **Cost-aware** - Monitor everything
- 📝 **Document everything** - You'll need it later

---

## ⏱️ 8-Hour Schedule

### **Morning: Foundation (9:00 AM - 12:00 PM)**

| Time | Task | Duration | Outcome |
|------|------|----------|---------|
| 9:00-9:30 | AWS Account Setup | 30 min | Secure account with MFA |
| 9:30-10:30 | IAM Configuration | 60 min | 3 users, 3 groups, proper security |
| 10:30-11:00 | AWS CLI Setup | 30 min | Configured and tested |
| 11:00-12:00 | Explore Console | 60 min | Comfort with AWS interface |

**Break:** 12:00 PM - 1:00 PM (Lunch)

### **Afternoon: Core Services (1:00 PM - 4:00 PM)**

| Time | Task | Duration | Outcome |
|------|------|----------|---------|
| 1:00-2:00 | Launch EC2 | 60 min | Running web server |
| 2:00-3:00 | S3 Website | 60 min | Live portfolio site |
| 3:00-4:00 | VPC Networking | 60 min | Custom network setup |

**Break:** 4:00 PM - 4:15 PM (Quick break)

### **Evening: Real Project (4:00 PM - 6:00 PM)**

| Time | Task | Duration | Outcome |
|------|------|----------|---------|
| 4:00-5:00 | 3-Tier App | 60 min | Full-stack deployment |
| 5:00-5:30 | Testing | 30 min | End-to-end verification |
| 5:30-6:00 | Cost & Cleanup | 30 min | Monitor costs, document |

---

## 🚀 Session 1: AWS Account & Security (9:00 AM - 10:30 AM)

### **Step 1: Create AWS Account (15 minutes)**

1. Go to https://aws.amazon.com/
2. Click "Create an AWS Account"
3. Enter email and account name
4. Choose "Personal" account type
5. Enter credit card (Free Tier - won't charge)
6. Verify phone number
7. Select "Basic Support - Free"

**✅ Checkpoint:** You should receive welcome email

### **Step 2: Secure Root Account (15 minutes)**

```bash
# 1. Sign in to AWS Console
# 2. Click on your account name (top right)
# 3. Go to "Security Credentials"
# 4. Under "Multi-factor authentication (MFA)"
# 5. Click "Activate MFA"
# 6. Choose "Virtual MFA device"
# 7. Use Google Authenticator / Authy app
# 8. Scan QR code and enter two consecutive codes
```

**✅ Checkpoint:** MFA badge shows "Active"

**🔒 Critical:** After this, NEVER use root account for daily tasks!

### **Step 3: Create IAM Admin User (20 minutes)**

**Via Console (Easier for first time):**
1. Services → IAM
2. Users → Add User
3. Username: `admin-user`
4. Access type: ✅ Programmatic ✅ Console
5. Attach policy: `AdministratorAccess`
6. Download credentials CSV
7. Enable MFA for admin-user

**Via CLI (After you have access keys):**
```bash
# Create user
aws iam create-user --user-name admin-user

# Attach admin policy
aws iam attach-user-policy \
  --user-name admin-user \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess

# Create access key
aws iam create-access-key --user-name admin-user
# SAVE THE OUTPUT - YOU'LL NEED IT!
```

**✅ Checkpoint:** Can login as admin-user with MFA

### **Step 4: Configure AWS CLI (20 minutes)**

```bash
# Configure with your admin-user credentials
aws configure

# You'll be prompted for:
# AWS Access Key ID: (from CSV or create-access-key output)
# AWS Secret Access Key: (from CSV or create-access-key output)
# Default region name: us-east-1
# Default output format: json

# Test configuration
aws sts get-caller-identity

# Expected output:
# {
#     "UserId": "AIDAXXXXXXXXXXXXXXXXX",
#     "Account": "123456789012",
#     "Arn": "arn:aws:iam::123456789012:user/admin-user"
# }

# If you see your details, ✅ YOU'RE READY!
```

### **Step 5: Set Up Billing Alerts (20 minutes)**

**Enable Billing Alerts:**
```bash
# 1. Go to AWS Console → Billing Dashboard
# 2. Click "Billing preferences"
# 3. Enable:
#    ✅ "Receive PDF Invoice By Email"
#    ✅ "Receive Free Tier Usage Alerts"
#    ✅ "Receive Billing Alerts"
# 4. Enter email and save
```

**Create CloudWatch Billing Alarm:**
```bash
# Create SNS topic for alerts
aws sns create-topic --name billing-alerts

# Subscribe your email
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:YOUR_ACCOUNT_ID:billing-alerts \
  --protocol email \
  --notification-endpoint your-email@example.com

# Create $10 billing alarm
aws cloudwatch put-metric-alarm \
  --alarm-name billing-alarm-10usd \
  --alarm-description "Alert when bill exceeds $10" \
  --metric-name EstimatedCharges \
  --namespace AWS/Billing \
  --statistic Maximum \
  --period 21600 \
  --evaluation-periods 1 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold \
  --alarm-actions arn:aws:sns:us-east-1:YOUR_ACCOUNT_ID:billing-alerts
```

**✅ Checkpoint:** Billing alarm shows in CloudWatch console

---

## 🚀 Session 2: EC2 & S3 (1:00 PM - 3:00 PM)

### **Quick EC2 Launch (30 minutes)**

```bash
# 1. Create key pair
aws ec2 create-key-pair \
  --key-name my-key \
  --query 'KeyMaterial' \
  --output text > my-key.pem
chmod 400 my-key.pem

# 2. Get default VPC ID
VPC_ID=$(aws ec2 describe-vpcs \
  --filters "Name=isDefault,Values=true" \
  --query 'Vpcs[0].VpcId' \
  --output text)

# 3. Create security group
SG_ID=$(aws ec2 create-security-group \
  --group-name web-server-sg \
  --description "Web server security group" \
  --vpc-id $VPC_ID \
  --query 'GroupId' \
  --output text)

# 4. Allow SSH and HTTP
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 80 --cidr 0.0.0.0/0

# 5. Launch instance
INSTANCE_ID=$(aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name my-key \
  --security-group-ids $SG_ID \
  --user-data '#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from AWS EC2!</h1>" > /var/www/html/index.html' \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' \
  --query 'Instances[0].InstanceId' \
  --output text)

# 6. Wait for instance to be running
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# 7. Get public IP
PUBLIC_IP=$(aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text)

echo "✅ Web server running at: http://$PUBLIC_IP"
```

**Test:** Open browser to `http://$PUBLIC_IP` - You should see "Hello from AWS EC2!"

### **Quick S3 Website (30 minutes)**

```bash
# 1. Create bucket (name must be globally unique!)
BUCKET_NAME="my-portfolio-$(date +%s)"
aws s3 mb s3://$BUCKET_NAME

# 2. Create index.html
cat > index.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My AWS Portfolio</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 50px;
        }
        h1 { font-size: 3em; }
    </style>
</head>
<body>
    <h1>🚀 Welcome to My AWS Portfolio</h1>
    <p>This site is hosted on Amazon S3!</p>
</body>
</html>
EOF

# 3. Upload file
aws s3 cp index.html s3://$BUCKET_NAME/

# 4. Enable website hosting
aws s3 website s3://$BUCKET_NAME/ \
  --index-document index.html

# 5. Make public
cat > bucket-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::$BUCKET_NAME/*"
  }]
}
EOF

aws s3api put-public-access-block \
  --bucket $BUCKET_NAME \
  --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

aws s3api put-bucket-policy \
  --bucket $BUCKET_NAME \
  --policy file://bucket-policy.json

# 6. Get website URL
echo "✅ Website URL: http://$BUCKET_NAME.s3-website-us-east-1.amazonaws.com"
```

**Test:** Open the website URL in browser

---

## 💡 Pro Tips for Success

### **1. Cost Management:**
```bash
# Always check Free Tier limits
# EC2: 750 hours/month of t2.micro
# S3: 5GB storage
# Data transfer: 15GB/month

# Monitor costs daily
aws ce get-cost-and-usage \
  --time-period Start=2026-02-01,End=2026-02-28 \
  --granularity MONTHLY \
  --metrics BlendedCost
```

### **2. Resource Tracking:**
Create a spreadsheet to track:
- Instance IDs
- Security Group IDs
- VPC IDs
- Bucket names
- IP addresses

### **3. Security Checklist:**
- [ ] Root account MFA enabled
- [ ] Admin user MFA enabled
- [ ] No access keys for root
- [ ] Security groups follow least privilege
- [ ] Regular credential rotation

### **4. Common Mistakes to Avoid:**
- ❌ Using root account for daily tasks
- ❌ Leaving EC2 instances running overnight
- ❌ Not setting billing alerts
- ❌ Public S3 buckets without intention
- ❌ Hardcoding credentials in code

---

## 🎯 Success Checklist

By end of Day 7, you should have:

**Security:**
- [ ] AWS account with MFA
- [ ] IAM admin user created
- [ ] Billing alerts configured
- [ ] AWS CLI working

**Services:**
- [ ] 1 running EC2 instance
- [ ] 1 S3-hosted website
- [ ] Custom VPC created
- [ ] Security groups configured

**Projects:**
- [ ] Static portfolio website live
- [ ] 3-tier application deployed
- [ ] Database connected and working
- [ ] All resources tagged

**Documentation:**
- [ ] Resource IDs documented
- [ ] Architecture diagram drawn
- [ ] Costs monitored
- [ ] Notes completed

---

## 🆘 Quick Troubleshooting

### **Can't SSH to EC2:**
```bash
# Check security group allows port 22
aws ec2 describe-security-groups --group-ids $SG_ID

# Check instance is running
aws ec2 describe-instances --instance-ids $INSTANCE_ID

# Verify key permissions
chmod 400 my-key.pem

# SSH with verbose
ssh -v -i my-key.pem ec2-user@$PUBLIC_IP
```

### **S3 Website Not Accessible:**
```bash
# Check bucket policy
aws s3api get-bucket-policy --bucket $BUCKET_NAME

# Check public access block
aws s3api get-public-access-block --bucket $BUCKET_NAME

# Verify website configuration
aws s3api get-bucket-website --bucket $BUCKET_NAME
```

### **High Costs Alert:**
```bash
# List all running instances
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType]'

# Stop unnecessary instances
aws ec2 stop-instances --instance-ids $INSTANCE_ID
```

---

## 📚 Essential Resources

**Official:**
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS CLI Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html)
- [AWS Documentation](https://docs.aws.amazon.com/)

**Learning:**
- [AWS Getting Started](https://aws.amazon.com/getting-started/)
- [AWS Hands-On Tutorials](https://aws.amazon.com/getting-started/hands-on/)
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/)

**Cost:**
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

---

## 🎓 What's Next?

**Tomorrow (Day 8):**
Choose your path:
1. **Advanced Kubernetes** - StatefulSets, Helm, Ingress
2. **AWS CI/CD** - CodePipeline, CodeBuild, CodeDeploy
3. **Infrastructure as Code** - Terraform or CloudFormation

**This Week:**
- Write blog post about AWS learning
- Apply to 5 DevOps jobs
- Practice AWS CLI commands
- Build another project

**Career Prep:**
- Update resume with AWS skills
- Update LinkedIn profile
- Prepare AWS interview answers
- Practice architecture diagrams

---

## 💪 Motivation

**You're not just learning AWS - you're building your future!**

By end of today:
- ✅ You'll have **2 live cloud applications**
- ✅ You'll understand **cloud architecture**
- ✅ You'll be **resume-ready** for cloud roles
- ✅ You'll have **hands-on AWS experience**

**20+ LPA roles are within reach!** 🎯

---

**Ready? Let's build something amazing on AWS!** ☁️🚀

**Start here:** [DAY_7_PLAN.md](docs/DAY_7_PLAN.md)
