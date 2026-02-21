# Day 7: AWS Fundamentals - Cloud Foundation for DevOps

> **Transform from local development to cloud deployment!**  
> Master AWS core services and deploy your first cloud application.

---

## 🎯 What You'll Learn Today

Today marks your entry into **cloud computing** - the backbone of modern DevOps. You'll master:

- ✅ **AWS Account Setup** - Security-first approach with IAM and MFA
- ✅ **EC2** - Launch and manage virtual servers
- ✅ **S3** - Object storage and static website hosting
- ✅ **VPC** - Networking fundamentals
- ✅ **AWS CLI** - Automate everything from command line
- ✅ **Cost Optimization** - Stay within Free Tier limits
- ✅ **3-Tier Application** - Deploy complete stack on AWS

---

## 📊 Day Overview

| Time | Session | Topics | Hands-On |
|------|---------|--------|----------|
| **9:00 - 12:00** | Morning | AWS Account, IAM, AWS CLI | Setup account, create users, configure CLI |
| **1:00 - 4:00** | Afternoon | EC2, S3, VPC | Launch servers, host website, create VPC |
| **4:00 - 6:00** | Evening | Full-Stack App, Cost Optimization | Deploy 3-tier app, set billing alerts |

**Total Time:** 8 hours  
**Hands-On:** 6 hours  
**Projects:** 2 (S3 website + 3-tier app)

---

## 🚀 Quick Start

### **Prerequisites:**
```bash
# Check if AWS CLI is installed
aws --version

# If not, install (macOS)
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

### **Today's Goals:**
1. ✅ Create AWS account with MFA
2. ✅ Launch first EC2 instance
3. ✅ Host website on S3
4. ✅ Create custom VPC
5. ✅ Deploy 3-tier application
6. ✅ Set up cost monitoring

---

## 📚 Topics Covered

### **1. AWS Account & IAM (Identity and Access Management)**

**Core Concepts:**
- Root account vs IAM users
- Multi-Factor Authentication (MFA)
- IAM Users, Groups, Roles, Policies
- Access Keys vs Console Access
- Principle of Least Privilege

**Hands-On:**
```bash
# Create IAM user
aws iam create-user --user-name devops-admin

# Create access key
aws iam create-access-key --user-name devops-admin

# Attach admin policy
aws iam attach-user-policy \
  --user-name devops-admin \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

**Why It Matters:**
- 🔒 **Security** - Never use root account for daily tasks
- 🎯 **Compliance** - Meet enterprise security standards
- 💼 **Professional** - Essential for any DevOps role

---

### **2. Amazon EC2 (Elastic Compute Cloud)**

**Core Concepts:**
- Instance types and families
- Amazon Machine Images (AMIs)
- Security Groups (virtual firewalls)
- SSH key pairs
- User data scripts
- Instance metadata

**Hands-On:**
```bash
# Launch t2.micro instance (Free Tier)
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name my-key \
  --security-group-ids sg-xxxxxx \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]'

# Connect via SSH
ssh -i my-key.pem ec2-user@<public-ip>
```

**Common Use Cases:**
- Web servers (Apache, Nginx)
- Application servers (Node.js, Python)
- Build servers (Jenkins, GitLab Runner)
- Database servers (PostgreSQL, MySQL)

---

### **3. Amazon S3 (Simple Storage Service)**

**Core Concepts:**
- Buckets and objects
- Storage classes (Standard, IA, Glacier)
- Bucket policies and ACLs
- Versioning
- Static website hosting
- Lifecycle policies

**Hands-On:**
```bash
# Create bucket
aws s3 mb s3://my-website-bucket

# Upload file
aws s3 cp index.html s3://my-website-bucket/

# Enable static website hosting
aws s3 website s3://my-website-bucket/ \
  --index-document index.html \
  --error-document error.html
```

**Real-World Applications:**
- Static website hosting
- Application file storage
- Backup and archive
- Data lakes
- Content distribution

---

### **4. Amazon VPC (Virtual Private Cloud)**

**Core Concepts:**
- CIDR blocks and IP addressing
- Public vs Private subnets
- Internet Gateway (IGW)
- NAT Gateway
- Route tables
- Security Groups vs Network ACLs

**Architecture:**
```
┌──────────────────────────────────────────────┐
│           VPC (10.0.0.0/16)                   │
│                                                │
│  ┌─────────────────┐  ┌─────────────────┐    │
│  │ Public Subnet   │  │ Private Subnet  │    │
│  │ 10.0.1.0/24     │  │ 10.0.2.0/24     │    │
│  │                 │  │                 │    │
│  │  Web Server     │  │  Database       │    │
│  │  (EC2)          │  │  (RDS)          │    │
│  └─────────────────┘  └─────────────────┘    │
│           │                    │               │
│    Internet Gateway      NAT Gateway          │
│                                                │
└──────────────────────────────────────────────┘
                    ↕
                Internet
```

**Hands-On:**
```bash
# Create VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16

# Create subnet
aws ec2 create-subnet \
  --vpc-id vpc-xxxxx \
  --cidr-block 10.0.1.0/24

# Create Internet Gateway
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway \
  --vpc-id vpc-xxxxx \
  --internet-gateway-id igw-xxxxx
```

---

## 🏗️ Today's Projects

### **Project 1: S3 Static Website**

**What You'll Build:**
- Professional portfolio website
- Hosted entirely on S3
- Public access via bucket policy
- Custom error pages

**Features:**
- ✅ Responsive design
- ✅ Project showcase
- ✅ Learning stats dashboard
- ✅ Error handling

**Outcome:**
- Live website URL
- Understanding of S3 hosting
- Bucket policy configuration

---

### **Project 2: 3-Tier AWS Application**

**Architecture:**
```
Frontend (S3 + CloudFront)
         ↓
Backend (EC2 + Docker)
         ↓
Database (PostgreSQL on EC2 or RDS)
```

**Components:**
1. **Frontend:** Static files on S3
2. **Backend:** REST API on EC2
3. **Database:** PostgreSQL container

**Skills Practiced:**
- Multi-tier architecture design
- Security group configuration
- Service integration
- End-to-end deployment

---

## 💰 Cost Management

### **Free Tier Limits (12 months):**
- **EC2:** 750 hours/month of t2.micro or t3.micro
- **S3:** 5GB Standard Storage
- **S3:** 20,000 GET requests, 2,000 PUT requests
- **Data Transfer:** 15GB out to internet

### **Billing Alerts Setup:**
```bash
# Create billing alarm
aws cloudwatch put-metric-alarm \
  --alarm-name billing-alarm-10usd \
  --alarm-description "Alert at $10" \
  --metric-name EstimatedCharges \
  --namespace AWS/Billing \
  --statistic Maximum \
  --period 21600 \
  --evaluation-periods 1 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold
```

### **Cost Optimization Tips:**
1. ✅ **Stop** (not just pause) EC2 instances when not in use
2. ✅ Delete **unattached** EBS volumes
3. ✅ Release **unused** Elastic IPs
4. ✅ Use **lifecycle policies** for S3
5. ✅ Enable **Cost Explorer** for tracking
6. ✅ Tag **all resources** for cost allocation

---

## 🛠️ Essential Commands Reference

### **AWS CLI Configuration:**
```bash
# Configure CLI
aws configure

# Test configuration
aws sts get-caller-identity

# List all regions
aws ec2 describe-regions --output table
```

### **EC2 Commands:**
```bash
# List instances
aws ec2 describe-instances

# Start instance
aws ec2 start-instances --instance-ids i-xxxxx

# Stop instance
aws ec2 stop-instances --instance-ids i-xxxxx

# Terminate instance
aws ec2 terminate-instances --instance-ids i-xxxxx

# Get instance public IP
aws ec2 describe-instances \
  --instance-ids i-xxxxx \
  --query 'Reservations[0].Instances[0].PublicIpAddress'
```

### **S3 Commands:**
```bash
# List buckets
aws s3 ls

# Create bucket
aws s3 mb s3://bucket-name

# Upload file
aws s3 cp file.txt s3://bucket-name/

# Sync directory
aws s3 sync ./local-dir s3://bucket-name/

# Delete bucket (must be empty)
aws s3 rb s3://bucket-name --force
```

### **IAM Commands:**
```bash
# List users
aws iam list-users

# List groups
aws iam list-groups

# List roles
aws iam list-roles

# Get current user
aws sts get-caller-identity
```

---

## 📖 Learning Path

### **Morning (3 hours):**
1. Create AWS account
2. Set up MFA on root account
3. Create IAM admin user
4. Configure AWS CLI
5. Explore AWS Console

### **Afternoon (3 hours):**
1. Launch EC2 instance
2. SSH into server
3. Install web server
4. Create S3 bucket
5. Host static website
6. Create custom VPC

### **Evening (2 hours):**
1. Deploy 3-tier application
2. Configure security groups
3. Test application
4. Set up billing alerts
5. Clean up resources

---

## ✅ Daily Checklist

### **Setup:**
- [ ] AWS account created
- [ ] Root account MFA enabled
- [ ] IAM admin user created
- [ ] AWS CLI installed and configured
- [ ] Billing alerts set up ($5, $10, $20)

### **EC2:**
- [ ] First EC2 instance launched
- [ ] SSH connection established
- [ ] Web server installed and running
- [ ] Security group configured
- [ ] Instance tagged properly

### **S3:**
- [ ] S3 bucket created
- [ ] Static website files uploaded
- [ ] Bucket policy configured
- [ ] Website accessible via URL
- [ ] Error page tested

### **VPC:**
- [ ] Custom VPC created
- [ ] Public subnet created
- [ ] Private subnet created
- [ ] Internet Gateway attached
- [ ] Route table configured

### **Project:**
- [ ] 3-tier application deployed
- [ ] Frontend accessible
- [ ] Backend API working
- [ ] Database connected
- [ ] End-to-end flow tested

### **Cost Management:**
- [ ] Cost Explorer enabled
- [ ] Billing dashboard reviewed
- [ ] Unused resources cleaned up
- [ ] Tags applied to all resources

---

## 🎓 Key Takeaways

### **Security:**
- ✅ Never use root account for daily operations
- ✅ Always enable MFA
- ✅ Follow principle of least privilege
- ✅ Use IAM roles instead of access keys when possible
- ✅ Rotate credentials regularly

### **Best Practices:**
- ✅ Tag all resources consistently
- ✅ Use CloudWatch for monitoring
- ✅ Enable CloudTrail for audit logs
- ✅ Implement backup strategies
- ✅ Document your architecture
- ✅ Use Infrastructure as Code (future topic)

### **Architecture:**
- ✅ Separate public and private subnets
- ✅ Use security groups as firewalls
- ✅ Implement defense in depth
- ✅ Plan for high availability
- ✅ Consider disaster recovery

---

## 🔗 Resources

### **Official Documentation:**
- [AWS Getting Started](https://aws.amazon.com/getting-started/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)
- [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

### **Hands-On Labs:**
- [AWS Hands-On Tutorials](https://aws.amazon.com/getting-started/hands-on/)
- [AWS Workshops](https://workshops.aws/)
- [Qwiklabs](https://www.qwiklabs.com/)

### **Certifications:**
- [AWS Cloud Practitioner](https://aws.amazon.com/certification/certified-cloud-practitioner/)
- [AWS Solutions Architect - Associate](https://aws.amazon.com/certification/certified-solutions-architect-associate/)

### **Cost Management:**
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

---

## 🚀 What's Next?

**Day 8 Options:**

1. **Advanced Kubernetes:**
   - StatefulSets, DaemonSets
   - Persistent Volumes
   - Helm package manager
   - Ingress controllers

2. **AWS CI/CD:**
   - CodePipeline
   - CodeBuild
   - CodeDeploy
   - Elastic Beanstalk
   - ECS/ECR

3. **Continue AWS Deep Dive:**
   - Lambda (Serverless)
   - DynamoDB
   - CloudFormation
   - Auto Scaling
   - Load Balancers

---

## 💡 Pro Tips

1. **Use CloudShell for Quick Tasks:**
   - No AWS CLI installation needed
   - Pre-authenticated
   - Built-in tools

2. **Bookmark AWS Service Health:**
   - https://status.aws.amazon.com/
   - Check before troubleshooting

3. **Use AWS Architecture Icons:**
   - https://aws.amazon.com/architecture/icons/
   - For professional diagrams

4. **Join AWS Community:**
   - AWS re:Post (Q&A forum)
   - AWS User Groups
   - AWS Events and Webinars

5. **Practice in Different Regions:**
   - Understanding regional differences
   - Latency considerations
   - Compliance requirements

---

## 📊 Success Metrics

By the end of Day 7:
- ✅ **2 running applications** (S3 website + 3-tier app)
- ✅ **4 AWS services mastered** (IAM, EC2, S3, VPC)
- ✅ **Billing alerts configured**
- ✅ **AWS CLI proficiency**
- ✅ **Cloud architecture understanding**
- ✅ **Security best practices implemented**

**Time Invested:** 8 hours  
**Projects Completed:** 2  
**Services Learned:** 4  
**Career Readiness:** Cloud DevOps ready! ☁️

---

## 🎯 Interview Preparation

### **Questions You Can Now Answer:**

1. **Q:** How do you secure an AWS account?  
   **A:** MFA on root, IAM users with least privilege, regular key rotation, CloudTrail logging

2. **Q:** What's the difference between Security Groups and NACLs?  
   **A:** SGs are stateful, instance-level; NACLs are stateless, subnet-level

3. **Q:** How do you host a static website on S3?  
   **A:** Enable static website hosting, set index/error documents, configure bucket policy

4. **Q:** Explain EC2 pricing models  
   **A:** On-Demand, Reserved, Spot, Savings Plans, Dedicated Hosts

5. **Q:** What's the difference between stopping and terminating an EC2 instance?  
   **A:** Stop preserves data, can restart; Terminate deletes instance and data

### **Resume Additions:**

- "Deployed and managed AWS infrastructure including EC2, S3, VPC, and IAM"
- "Implemented cloud security best practices with MFA, IAM roles, and principle of least privilege"
- "Automated AWS resource provisioning using AWS CLI and shell scripts"
- "Optimized cloud costs staying within AWS Free Tier limits with billing monitoring"
- "Deployed 3-tier web applications on AWS with proper network isolation"

---

**Ready to become a cloud DevOps engineer? Let's dive into AWS!** ☁️🚀

**See you in the detailed plan:** [DAY_7_PLAN.md](docs/DAY_7_PLAN.md)
