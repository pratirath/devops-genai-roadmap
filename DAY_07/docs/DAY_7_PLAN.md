# Day 7: AWS Fundamentals - Cloud Foundation for DevOps

> **Date:** February 21, 2026  
> **Focus:** AWS Core Services, IAM, EC2, S3, VPC, and Cloud Deployment  
> **Duration:** 8 hours  
> **Goal:** Master AWS fundamentals and deploy cloud-based applications

---

## 📋 Learning Objectives

By the end of Day 7, you will:
- ✅ Set up AWS Free Tier account with security best practices
- ✅ Master IAM (Identity and Access Management)
- ✅ Launch and manage EC2 instances
- ✅ Use S3 for object storage and static website hosting
- ✅ Configure VPC and networking fundamentals
- ✅ Automate AWS tasks with AWS CLI
- ✅ Implement cost optimization strategies
- ✅ Deploy a complete 3-tier application on AWS

---

## 🎯 Why AWS Skills Matter for 20+ LPA Roles

### **Market Demand:**
- ☁️ **90%+** of enterprises use AWS or multi-cloud
- 💰 **AWS expertise** adds 15-25% salary premium
- 🚀 **Cloud computing** is essential DevOps skill
- 📈 **AWS certifications** highly valued by employers

### **Career Impact:**
- Cloud DevOps Engineer: **₹18-30 LPA**
- AWS Solutions Architect: **₹22-38 LPA**
- Cloud SRE: **₹25-45 LPA**
- Cloud Platform Engineer: **₹28-50 LPA**

---

## 📚 Session Breakdown

### **Morning Session (3 hours): AWS Fundamentals & Account Setup**

#### **Hour 1: AWS Account Setup & Security (9:00 AM - 10:00 AM)**

**Topics:**
1. Create AWS Free Tier account
2. Set up root account MFA (Multi-Factor Authentication)
3. Understanding AWS Free Tier limits
4. Set up billing alerts
5. AWS Console navigation

**Hands-On:**
```bash
# AWS Free Tier Includes:
# - 750 hours/month EC2 t2.micro or t3.micro
# - 5GB S3 Standard Storage
# - 750 hours RDS db.t2.micro
# - 1 Million Lambda requests
# - 25GB DynamoDB storage
```

**Account Security Checklist:**
- [ ] Enable MFA on root account
- [ ] Create billing alarm ($5, $10, $20 thresholds)
- [ ] Set up CloudWatch billing alerts
- [ ] Enable AWS Cost Explorer
- [ ] Review security recommendations

**Documentation:**
- Take screenshots of MFA setup
- Document billing alert configuration
- Note down account ID and region

---

#### **Hour 2: IAM - Identity & Access Management (10:00 AM - 11:00 AM)**

**Topics:**
1. IAM Users, Groups, Roles, and Policies
2. Principle of Least Privilege
3. Creating admin user (never use root!)
4. Access Keys vs Console Access
5. IAM Best Practices

**Hands-On Tasks:**

1. **Create Admin User:**
```json
// AdminUser Policy (AdministratorAccess)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

2. **Create Developer Group:**
```bash
# Create IAM Group
aws iam create-group --group-name Developers

# Attach policy to group
aws iam attach-group-policy \
  --group-name Developers \
  --policy-arn arn:aws:iam::aws:policy/PowerUserAccess
```

3. **Create Service Role for EC2:**
```bash
# Create trust policy for EC2
cat > trust-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

# Create role
aws iam create-role \
  --role-name EC2-S3-Access \
  --assume-role-policy-document file://trust-policy.json
```

**IAM Best Practices:**
- ✅ Never use root account for daily tasks
- ✅ Enable MFA for all users
- ✅ Use groups to assign permissions
- ✅ Rotate access keys regularly
- ✅ Use roles for EC2/Lambda instead of access keys
- ✅ Follow principle of least privilege
- ✅ Enable CloudTrail for audit logging

**Practice Exercise:**
- Create 3 users: admin-user, dev-user, read-only-user
- Create 3 groups: Admins, Developers, Viewers
- Assign appropriate policies
- Test permissions by switching users

---

#### **Hour 3: AWS CLI & CloudShell Setup (11:00 AM - 12:00 PM)**

**Topics:**
1. Installing AWS CLI v2
2. Configuring AWS credentials
3. AWS CloudShell (browser-based CLI)
4. Basic AWS CLI commands
5. AWS CLI profiles for multiple accounts

**Installation:**

**macOS:**
```bash
# Install AWS CLI v2
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

# Verify installation
aws --version
# aws-cli/2.15.0 Python/3.11.6 Darwin/23.0.0 source/arm64
```

**Configuration:**
```bash
# Configure AWS CLI
aws configure

# Enter:
# AWS Access Key ID: YOUR_ACCESS_KEY
# AWS Secret Access Key: YOUR_SECRET_KEY
# Default region name: us-east-1
# Default output format: json

# Test configuration
aws sts get-caller-identity
```

**Essential AWS CLI Commands:**

```bash
# IAM Commands
aws iam list-users
aws iam get-user --user-name admin-user
aws iam list-groups
aws iam list-roles

# S3 Commands
aws s3 ls                          # List buckets
aws s3 mb s3://my-bucket-name      # Create bucket
aws s3 cp file.txt s3://bucket/    # Upload file
aws s3 sync ./local s3://bucket/   # Sync directory

# EC2 Commands
aws ec2 describe-instances
aws ec2 describe-vpcs
aws ec2 describe-security-groups

# Account Information
aws sts get-caller-identity        # Who am I?
aws account get-contact-information

# Cost and Billing
aws ce get-cost-and-usage \
  --time-period Start=2026-02-01,End=2026-02-20 \
  --granularity MONTHLY \
  --metrics BlendedCost
```

**CloudShell Practice:**
- Launch CloudShell from AWS Console
- Run basic commands
- Upload/download files
- Install additional tools (docker, kubectl, etc.)

---

### **Afternoon Session (3 hours): Core AWS Services**

#### **Hour 4: Amazon EC2 - Elastic Compute Cloud (1:00 PM - 2:00 PM)**

**Topics:**
1. EC2 instance types and families
2. AMIs (Amazon Machine Images)
3. Security Groups (virtual firewalls)
4. Key Pairs for SSH access
5. EBS volumes
6. Instance metadata

**Hands-On: Launch Your First EC2 Instance**

1. **Create Key Pair:**
```bash
# Create key pair
aws ec2 create-key-pair \
  --key-name devops-learning-key \
  --query 'KeyMaterial' \
  --output text > devops-learning-key.pem

# Set permissions
chmod 400 devops-learning-key.pem
```

2. **Create Security Group:**
```bash
# Create security group
aws ec2 create-security-group \
  --group-name web-server-sg \
  --description "Security group for web server" \
  --vpc-id vpc-xxxxxxxx

# Allow SSH (port 22)
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxxxxx \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0

# Allow HTTP (port 80)
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxxxxx \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```

3. **Launch EC2 Instance:**
```bash
# Launch t2.micro instance (Free Tier)
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name devops-learning-key \
  --security-group-ids sg-xxxxxxxx \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' \
  --user-data file://user-data.sh
```

4. **User Data Script (user-data.sh):**
```bash
#!/bin/bash
# Update system
yum update -y

# Install web server
yum install -y httpd

# Start web server
systemctl start httpd
systemctl enable httpd

# Create sample webpage
cat > /var/www/html/index.html <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>My First AWS EC2 Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 50px;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Hello from AWS EC2!</h1>
        <p>This server is running on Amazon EC2</p>
        <p>Instance ID: <span id="instance-id">Loading...</span></p>
        <p>Availability Zone: <span id="az">Loading...</span></p>
    </div>
    <script>
        fetch('http://169.254.169.254/latest/meta-data/instance-id')
            .then(r => r.text())
            .then(id => document.getElementById('instance-id').textContent = id);
        
        fetch('http://169.254.169.254/latest/meta-data/placement/availability-zone')
            .then(r => r.text())
            .then(az => document.getElementById('az').textContent = az);
    </script>
</body>
</html>
EOF
```

5. **Connect to EC2 Instance:**
```bash
# Get instance public IP
aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=WebServer" \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text

# SSH into instance
ssh -i devops-learning-key.pem ec2-user@<PUBLIC_IP>

# Check web server status
sudo systemctl status httpd

# View website
curl http://<PUBLIC_IP>
```

**EC2 Instance Types:**
- **t2.micro** - 1 vCPU, 1 GB RAM (Free Tier)
- **t3.small** - 2 vCPU, 2 GB RAM
- **t3.medium** - 2 vCPU, 4 GB RAM
- **m5.large** - 2 vCPU, 8 GB RAM

---

#### **Hour 5: Amazon S3 - Simple Storage Service (2:00 PM - 3:00 PM)**

**Topics:**
1. S3 buckets and objects
2. S3 storage classes
3. Bucket policies and ACLs
4. S3 versioning
5. S3 lifecycle policies
6. Static website hosting

**Hands-On: Create S3 Bucket & Host Static Website**

1. **Create S3 Bucket:**
```bash
# Create bucket (must be globally unique name)
aws s3 mb s3://devops-learning-pratirath-2026

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket devops-learning-pratirath-2026 \
  --versioning-configuration Status=Enabled

# Enable static website hosting
aws s3 website s3://devops-learning-pratirath-2026/ \
  --index-document index.html \
  --error-document error.html
```

2. **Create Website Files:**

**index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Learning Portfolio - AWS S3</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        header {
            text-align: center;
            padding: 50px 0;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }
        .stat-card {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            backdrop-filter: blur(10px);
        }
        .stat-number {
            font-size: 3em;
            font-weight: bold;
            color: #ffd700;
        }
        .stat-label {
            font-size: 1.1em;
            margin-top: 10px;
            opacity: 0.9;
        }
        .projects {
            margin: 40px 0;
        }
        .project-card {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
        }
        .project-card h3 {
            color: #ffd700;
            margin-bottom: 10px;
        }
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        .tech-badge {
            background: rgba(255,255,255,0.2);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }
        footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 DevOps Learning Journey</h1>
            <p class="subtitle">30-Day Roadmap to 20+ LPA DevOps Engineer</p>
        </header>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">7</div>
                <div class="stat-label">Days Completed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">6</div>
                <div class="stat-label">Projects Done</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">35%</div>
                <div class="stat-label">Progress</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">100%</div>
                <div class="stat-label">Commitment</div>
            </div>
        </div>

        <div class="projects">
            <h2 style="text-align: center; margin-bottom: 30px;">📦 Completed Projects</h2>
            
            <div class="project-card">
                <h3>1. Docker Multi-Container App</h3>
                <p>Full-stack application with Docker Compose, including frontend, backend, and PostgreSQL database.</p>
                <div class="tech-stack">
                    <span class="tech-badge">Docker</span>
                    <span class="tech-badge">Docker Compose</span>
                    <span class="tech-badge">Flask</span>
                    <span class="tech-badge">PostgreSQL</span>
                </div>
            </div>

            <div class="project-card">
                <h3>2. Kubernetes Blog Application</h3>
                <p>Multi-tier blog app deployed on Kubernetes with Pods, Deployments, and Services.</p>
                <div class="tech-stack">
                    <span class="tech-badge">Kubernetes</span>
                    <span class="tech-badge">Minikube</span>
                    <span class="tech-badge">kubectl</span>
                    <span class="tech-badge">YAML</span>
                </div>
            </div>

            <div class="project-card">
                <h3>3. Secure E-Commerce Microservices</h3>
                <p>4-tier isolated Docker network architecture with security scanning and secrets management.</p>
                <div class="tech-stack">
                    <span class="tech-badge">Docker Networks</span>
                    <span class="tech-badge">Trivy</span>
                    <span class="tech-badge">Security</span>
                    <span class="tech-badge">Microservices</span>
                </div>
            </div>

            <div class="project-card">
                <h3>4. AWS Cloud Website (This Site!)</h3>
                <p>Static website hosted on Amazon S3 with CloudFront CDN for global distribution.</p>
                <div class="tech-stack">
                    <span class="tech-badge">AWS S3</span>
                    <span class="tech-badge">AWS EC2</span>
                    <span class="tech-badge">IAM</span>
                    <span class="tech-badge">CloudFront</span>
                </div>
            </div>
        </div>

        <footer>
            <p>🌟 Hosted on Amazon S3 | Built with ❤️ during DevOps Learning Journey</p>
            <p style="margin-top: 10px;">GitHub: pratirath/devops-genai-roadmap</p>
        </footer>
    </div>
</body>
</html>
```

**error.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        h1 { font-size: 5em; }
        p { font-size: 1.5em; }
    </style>
</head>
<body>
    <div>
        <h1>404</h1>
        <p>Oops! Page not found</p>
        <a href="/" style="color: #ffd700;">Go Home</a>
    </div>
</body>
</html>
```

3. **Upload Files to S3:**
```bash
# Upload files
aws s3 cp index.html s3://devops-learning-pratirath-2026/
aws s3 cp error.html s3://devops-learning-pratirath-2026/

# Make files public
aws s3api put-bucket-policy \
  --bucket devops-learning-pratirath-2026 \
  --policy file://bucket-policy.json
```

**bucket-policy.json:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::devops-learning-pratirath-2026/*"
    }
  ]
}
```

4. **Access Website:**
```bash
# Website URL format:
# http://devops-learning-pratirath-2026.s3-website-us-east-1.amazonaws.com

# Get website endpoint
aws s3api get-bucket-website \
  --bucket devops-learning-pratirath-2026
```

**S3 Storage Classes:**
- **Standard** - Frequent access, high availability
- **Standard-IA** - Infrequent access, lower cost
- **One Zone-IA** - Infrequent access, single AZ
- **Glacier** - Archive, retrieval in minutes to hours
- **Glacier Deep Archive** - Long-term archive, retrieval in hours

---

#### **Hour 6: Amazon VPC - Virtual Private Cloud (3:00 PM - 4:00 PM)**

**Topics:**
1. VPC fundamentals
2. Subnets (public vs private)
3. Internet Gateway and NAT Gateway
4. Route tables
5. Network ACLs vs Security Groups
6. VPC peering

**Hands-On: Create Custom VPC**

1. **Create VPC:**
```bash
# Create VPC
aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=DevOps-VPC}]'

# Enable DNS hostnames
aws ec2 modify-vpc-attribute \
  --vpc-id vpc-xxxxxxxx \
  --enable-dns-hostnames
```

2. **Create Subnets:**
```bash
# Public subnet (AZ 1)
aws ec2 create-subnet \
  --vpc-id vpc-xxxxxxxx \
  --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-Subnet-1}]'

# Private subnet (AZ 1)
aws ec2 create-subnet \
  --vpc-id vpc-xxxxxxxx \
  --cidr-block 10.0.2.0/24 \
  --availability-zone us-east-1a \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Private-Subnet-1}]'
```

3. **Create Internet Gateway:**
```bash
# Create IGW
aws ec2 create-internet-gateway \
  --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=DevOps-IGW}]'

# Attach to VPC
aws ec2 attach-internet-gateway \
  --vpc-id vpc-xxxxxxxx \
  --internet-gateway-id igw-xxxxxxxx
```

4. **Create Route Tables:**
```bash
# Create public route table
aws ec2 create-route-table \
  --vpc-id vpc-xxxxxxxx \
  --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=Public-RT}]'

# Add route to Internet Gateway
aws ec2 create-route \
  --route-table-id rtb-xxxxxxxx \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id igw-xxxxxxxx

# Associate with public subnet
aws ec2 associate-route-table \
  --subnet-id subnet-xxxxxxxx \
  --route-table-id rtb-xxxxxxxx
```

**VPC Architecture Diagram:**
```
┌─────────────────────────────────────────────────────────────┐
│                      VPC (10.0.0.0/16)                       │
│                                                               │
│  ┌────────────────────────┐  ┌────────────────────────┐     │
│  │  Public Subnet         │  │  Private Subnet        │     │
│  │  (10.0.1.0/24)         │  │  (10.0.2.0/24)         │     │
│  │                        │  │                        │     │
│  │  ┌──────────────┐      │  │  ┌──────────────┐     │     │
│  │  │ Web Server   │      │  │  │  Database    │     │     │
│  │  │ EC2          │      │  │  │  RDS         │     │     │
│  │  └──────────────┘      │  │  └──────────────┘     │     │
│  │                        │  │                        │     │
│  │  Internet Gateway ↑    │  │  NAT Gateway ↑         │     │
│  └────────────────────────┘  └────────────────────────┘     │
│                                                               │
└─────────────────────────────────────────────────────────────┘
                         ↕
                    Internet
```

---

### **Evening Session (2 hours): AWS Project & Cost Optimization**

#### **Hour 7: Deploy Full-Stack Application on AWS (4:00 PM - 5:00 PM)**

**Project: 3-Tier Web Application on AWS**

**Architecture:**
- Frontend: S3 + CloudFront
- Backend: EC2 instance
- Database: RDS PostgreSQL (or EC2 with Docker PostgreSQL)

**Implementation:**

1. **Backend Setup (EC2):**

```bash
# Launch EC2 for backend
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name devops-learning-key \
  --security-group-ids sg-backend \
  --subnet-id subnet-private \
  --user-data file://backend-setup.sh \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Backend-API}]'
```

**backend-setup.sh:**
```bash
#!/bin/bash
yum update -y
yum install -y docker
systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user

# Pull and run backend container
docker run -d \
  --name backend-api \
  -p 5000:5000 \
  -e DATABASE_URL=postgresql://user:pass@db-host:5432/appdb \
  your-backend-image:latest
```

2. **Frontend Deployment (S3):**
```bash
# Build frontend (assuming React app)
npm run build

# Upload to S3
aws s3 sync build/ s3://frontend-bucket/

# Configure CloudFront for CDN
aws cloudfront create-distribution \
  --origin-domain-name frontend-bucket.s3.amazonaws.com \
  --default-root-object index.html
```

3. **Database Setup (RDS or EC2):**
```bash
# Option 1: RDS PostgreSQL (costs money)
aws rds create-db-instance \
  --db-instance-identifier myapp-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password YourPassword123! \
  --allocated-storage 20

# Option 2: PostgreSQL on EC2 (Free Tier)
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=appdb \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15
```

---

#### **Hour 8: Cost Optimization & Cleanup (5:00 PM - 6:00 PM)**

**Topics:**
1. AWS Free Tier limits
2. Cost monitoring and alerts
3. Resource cleanup best practices
4. AWS Cost Explorer
5. Savings plans and reserved instances

**Cost Optimization Checklist:**

```bash
# 1. Set up billing alerts
aws cloudwatch put-metric-alarm \
  --alarm-name billing-alarm-10usd \
  --alarm-description "Alert when bill exceeds $10" \
  --metric-name EstimatedCharges \
  --namespace AWS/Billing \
  --statistic Maximum \
  --period 21600 \
  --evaluation-periods 1 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold

# 2. List all running EC2 instances
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name]' \
  --output table

# 3. List all S3 buckets and sizes
aws s3 ls
aws s3 ls s3://bucket-name --recursive --summarize

# 4. Check for unattached EBS volumes
aws ec2 describe-volumes \
  --filters "Name=status,Values=available" \
  --query 'Volumes[*].[VolumeId,Size,State]' \
  --output table

# 5. List elastic IPs (charged if not attached)
aws ec2 describe-addresses \
  --query 'Addresses[?AssociationId==null].[PublicIp,AllocationId]' \
  --output table
```

**Resource Cleanup:**

```bash
# Stop EC2 instances
aws ec2 stop-instances --instance-ids i-xxxxxxxx

# Terminate EC2 instances
aws ec2 terminate-instances --instance-ids i-xxxxxxxx

# Delete S3 bucket (must be empty first)
aws s3 rm s3://bucket-name --recursive
aws s3 rb s3://bucket-name

# Release Elastic IP
aws ec2 release-address --allocation-id eipalloc-xxxxxxxx

# Delete security groups
aws ec2 delete-security-group --group-id sg-xxxxxxxx

# Delete VPC (delete dependencies first)
aws ec2 delete-vpc --vpc-id vpc-xxxxxxxx
```

**Free Tier Monitoring:**
```bash
# Get current month's costs
aws ce get-cost-and-usage \
  --time-period Start=2026-02-01,End=2026-02-28 \
  --granularity MONTHLY \
  --metrics BlendedCost UnblendedCost \
  --group-by Type=SERVICE

# Get Free Tier usage
aws ce get-cost-and-usage \
  --time-period Start=2026-02-01,End=2026-02-28 \
  --granularity MONTHLY \
  --filter file://free-tier-filter.json \
  --metrics UsageQuantity
```

---

## 📝 Day 7 Checklist

### **Morning:**
- [ ] Create AWS account with MFA enabled
- [ ] Set up billing alerts ($5, $10, $20)
- [ ] Create admin IAM user
- [ ] Configure AWS CLI
- [ ] Create 3 IAM users with different permissions
- [ ] Test AWS CloudShell

### **Afternoon:**
- [ ] Launch EC2 instance with web server
- [ ] SSH into EC2 instance
- [ ] Create S3 bucket
- [ ] Host static website on S3
- [ ] Create custom VPC with public/private subnets
- [ ] Set up Internet Gateway and route tables

### **Evening:**
- [ ] Deploy 3-tier application (Frontend, Backend, Database)
- [ ] Configure security groups for each tier
- [ ] Test application end-to-end
- [ ] Set up cost monitoring
- [ ] Clean up unused resources
- [ ] Document architecture diagram

---

## 🎓 Key Concepts to Master

### **IAM:**
- Users, Groups, Roles, Policies
- Principle of Least Privilege
- MFA for security
- Access Keys vs Console Access

### **EC2:**
- Instance types and families
- AMIs and user data
- Security groups
- Key pairs for SSH
- Elastic IPs
- Instance metadata

### **S3:**
- Buckets and objects
- Bucket policies
- Storage classes
- Versioning
- Static website hosting
- Lifecycle policies

### **VPC:**
- CIDR blocks
- Subnets (public vs private)
- Internet Gateway
- NAT Gateway
- Route tables
- Security Groups vs NACLs

---

## 💡 Pro Tips

1. **Always Use Free Tier Resources:**
   - t2.micro or t3.micro EC2 instances
   - 5GB S3 storage
   - 750 hours/month EC2 usage

2. **Stop (Don't Just Pause) Resources:**
   - Stopped EC2 instances don't incur compute charges
   - Still charged for EBS volumes

3. **Use Tags for Everything:**
   ```bash
   --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=MyServer},{Key=Project,Value=DevOps},{Key=Environment,Value=Learning}]'
   ```

4. **Enable CloudTrail for Audit:**
   - Track all API calls
   - Security and compliance
   - Free for management events

5. **Use AWS Calculator:**
   - https://calculator.aws/
   - Estimate costs before deployment

6. **Region Matters:**
   - us-east-1 (N. Virginia) - Usually cheapest
   - Consider latency to users
   - Data transfer costs between regions

---

## 🔗 Essential Resources

### **Official AWS:**
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS CLI Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html)
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/)

### **Tutorials:**
- [AWS Hands-On Tutorials](https://aws.amazon.com/getting-started/hands-on/)
- [AWS Workshops](https://workshops.aws/)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)

### **Cost Management:**
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)

### **Certifications:**
- [AWS Certified Cloud Practitioner](https://aws.amazon.com/certification/certified-cloud-practitioner/)
- [AWS Certified Solutions Architect - Associate](https://aws.amazon.com/certification/certified-solutions-architect-associate/)

---

## 🚀 What's Next?

**Day 8: Advanced AWS & CI/CD**
- AWS CodePipeline
- AWS CodeBuild
- AWS CodeDeploy
- Elastic Beanstalk
- ECS (Elastic Container Service)
- ECR (Elastic Container Registry)

**Future Topics:**
- AWS Lambda (Serverless)
- API Gateway
- DynamoDB
- CloudFormation (Infrastructure as Code)
- Auto Scaling Groups
- Load Balancers (ALB, NLB)

---

## 📊 Success Metrics

By end of Day 7, you should have:
- ✅ Active AWS account with proper security
- ✅ 1 running EC2 instance with web server
- ✅ 1 S3-hosted static website
- ✅ Custom VPC with public/private subnets
- ✅ 3-tier application deployed
- ✅ Billing alerts configured
- ✅ AWS CLI configured and tested
- ✅ Basic understanding of IAM, EC2, S3, VPC

**Time Investment:** 8 hours  
**Hands-On:** 6 hours  
**Theory:** 2 hours  
**Projects:** 2 (Static website + 3-tier app)

---

## 🎯 Career Impact

### **Skills Gained Today:**
- ✅ AWS account management
- ✅ Cloud infrastructure setup
- ✅ Security best practices (IAM, MFA)
- ✅ Compute services (EC2)
- ✅ Storage services (S3)
- ✅ Networking (VPC)
- ✅ Cost optimization
- ✅ AWS CLI automation

### **Interview Questions You Can Now Answer:**
1. How do you secure an AWS account?
2. Explain the difference between Security Groups and NACLs
3. What's the difference between stopping and terminating an EC2 instance?
4. How do you host a static website on S3?
5. Explain VPC, subnets, and route tables
6. What are IAM roles and when would you use them?
7. How do you monitor AWS costs?

### **Resume Bullet Points:**
- "Deployed and managed cloud infrastructure on AWS, including EC2, S3, and VPC"
- "Implemented security best practices using IAM roles, MFA, and principle of least privilege"
- "Automated AWS resource management using AWS CLI and shell scripts"
- "Optimized cloud costs by implementing billing alerts and resource tagging"
- "Hosted production-ready applications on AWS with 3-tier architecture"

---

**Remember:** AWS is the foundation of modern DevOps. Master these basics, and you're 50% closer to your 20+ LPA goal! 🎯

**Tomorrow:** We level up with Advanced Kubernetes (StatefulSets, Helm, Ingress) OR continue with AWS CI/CD pipeline!

Good luck! 🚀
