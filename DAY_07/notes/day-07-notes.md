# Day 7: AWS Fundamentals - Learning Notes

> **Date:** February 21, 2026  
> **Focus:** AWS Cloud Platform Basics  
> **Time:** 8 hours

---

## 📝 Session 1: AWS Account & IAM (9:00 AM - 12:00 PM)

### **AWS Account Setup**

**Account Details:**
- Account ID: ___________________________________
- Root Email: ___________________________________
- Created Date: ___________________________________
- Default Region: ___________________________________

**Security Setup:**
- [ ] Root account MFA enabled
- [ ] MFA device type: ___________________________________
- [ ] Billing alerts configured
- [ ] Cost Explorer enabled

**Billing Alerts:**
| Threshold | Alert Created | Status |
|-----------|---------------|--------|
| $5        | [ ]           | ___    |
| $10       | [ ]           | ___    |
| $20       | [ ]           | ___    |

---

### **IAM (Identity & Access Management)**

**IAM Users Created:**

1. **Admin User:**
   - Username: ___________________________________
   - Access Type: [ ] Console [ ] Programmatic
   - MFA Enabled: [ ] Yes [ ] No
   - Groups: ___________________________________

2. **Developer User:**
   - Username: ___________________________________
   - Access Type: [ ] Console [ ] Programmatic
   - Permissions: ___________________________________

3. **Read-Only User:**
   - Username: ___________________________________
   - Access Type: [ ] Console [ ] Programmatic
   - Permissions: ___________________________________

**IAM Groups:**

| Group Name | Attached Policies | Members |
|------------|-------------------|---------|
| Admins     |                   |         |
| Developers |                   |         |
| Viewers    |                   |         |

**IAM Roles Created:**

| Role Name | Service | Use Case | Policy |
|-----------|---------|----------|--------|
| EC2-S3-Access | EC2 | S3 read/write |        |
|           |     |          |        |
|           |     |          |        |

**Key Learnings:**
```
1. Principle of Least Privilege:
   - 
   - 
   - 

2. IAM Best Practices:
   - 
   - 
   - 

3. Common Mistakes to Avoid:
   - 
   - 
   - 
```

---

### **AWS CLI Configuration**

**Installation:**
```bash
# AWS CLI Version:
aws --version
# Output: 

# Configuration:
aws configure
# Access Key ID: ************
# Secret Access Key: ************
# Default Region: 
# Output Format: 
```

**Testing:**
```bash
# Test 1: Get caller identity
aws sts get-caller-identity
# Output:


# Test 2: List S3 buckets
aws s3 ls
# Output:


# Test 3: List EC2 instances
aws ec2 describe-instances
# Output:

```

**CLI Commands Practiced:**

| Command | Purpose | Result |
|---------|---------|--------|
| aws sts get-caller-identity | Check current user |  |
| aws iam list-users | List all IAM users |  |
| aws s3 ls | List S3 buckets |  |
| aws ec2 describe-instances | List EC2 instances |  |

---

## 📝 Session 2: Core AWS Services (1:00 PM - 4:00 PM)

### **Amazon EC2 (Elastic Compute Cloud)**

**EC2 Instance 1: Web Server**

**Configuration:**
- Instance ID: ___________________________________
- Instance Type: ___________________________________
- AMI ID: ___________________________________
- Availability Zone: ___________________________________
- Public IP: ___________________________________
- Private IP: ___________________________________
- Security Group: ___________________________________
- Key Pair: ___________________________________

**Security Group Rules:**

| Type | Protocol | Port | Source | Purpose |
|------|----------|------|--------|---------|
| SSH  | TCP      | 22   | 0.0.0.0/0 | Remote access |
| HTTP | TCP      | 80   | 0.0.0.0/0 | Web traffic |
| HTTPS| TCP      | 443  | 0.0.0.0/0 | Secure web |

**User Data Script:**
```bash
#!/bin/bash
# Installation commands:




# Application setup:




# Output:

```

**Connection Test:**
```bash
# SSH Command:
ssh -i _____.pem ec2-user@_____

# Web Server Test:
curl http://_____

# Result:

```

**Instance Metadata Queries:**
```bash
# Instance ID:
curl http://169.254.169.254/latest/meta-data/instance-id
# Result: 

# Public IP:
curl http://169.254.169.254/latest/meta-data/public-ipv4
# Result: 

# Availability Zone:
curl http://169.254.169.254/latest/meta-data/placement/availability-zone
# Result: 
```

---

### **Amazon S3 (Simple Storage Service)**

**S3 Bucket 1: Static Website**

**Configuration:**
- Bucket Name: ___________________________________
- Region: ___________________________________
- Versioning: [ ] Enabled [ ] Disabled
- Public Access: [ ] Enabled [ ] Disabled
- Website Endpoint: ___________________________________

**Files Uploaded:**

| File | Size | Upload Date | URL |
|------|------|-------------|-----|
| index.html |  |  |  |
| error.html |  |  |  |
| style.css |  |  |  |
| script.js |  |  |  |

**Bucket Policy:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "",
      "Principal": "",
      "Action": "",
      "Resource": ""
    }
  ]
}
```

**Website URL:**
- URL: ___________________________________
- Tested: [ ] Yes [ ] No
- Working: [ ] Yes [ ] No

**S3 Commands Used:**
```bash
# Create bucket:
aws s3 mb s3://_____

# Upload file:
aws s3 cp _____ s3://_____/

# List contents:
aws s3 ls s3://_____/

# Enable website hosting:


# Result:

```

---

### **Amazon VPC (Virtual Private Cloud)**

**VPC Configuration:**
- VPC ID: ___________________________________
- CIDR Block: ___________________________________
- DNS Hostnames: [ ] Enabled [ ] Disabled
- DNS Resolution: [ ] Enabled [ ] Disabled

**Subnets:**

| Subnet Name | CIDR | AZ | Type | Route Table |
|-------------|------|-----|------|-------------|
| Public-1    | 10.0.1.0/24 |  | Public |  |
| Private-1   | 10.0.2.0/24 |  | Private |  |

**Internet Gateway:**
- IGW ID: ___________________________________
- Attached to VPC: ___________________________________
- State: ___________________________________

**Route Tables:**

**Public Route Table:**
| Destination | Target | Purpose |
|-------------|--------|---------|
| 10.0.0.0/16 | local  | VPC local |
| 0.0.0.0/0   | igw-xxx | Internet |

**Private Route Table:**
| Destination | Target | Purpose |
|-------------|--------|---------|
| 10.0.0.0/16 | local  | VPC local |

**VPC Architecture Diagram:**
```
Draw your VPC architecture here:

┌─────────────────────────────────────────────────┐
│                                                   │
│                                                   │
│                                                   │
│                                                   │
│                                                   │
│                                                   │
│                                                   │
│                                                   │
│                                                   │
└─────────────────────────────────────────────────┘
```

---

## 📝 Session 3: Project & Cost Optimization (4:00 PM - 6:00 PM)

### **Project: 3-Tier AWS Application**

**Architecture Components:**

**Frontend (S3):**
- Bucket: ___________________________________
- URL: ___________________________________
- Files: ___________________________________

**Backend (EC2):**
- Instance ID: ___________________________________
- Public IP: ___________________________________
- Application: ___________________________________
- Port: ___________________________________

**Database:**
- Type: [ ] RDS [ ] EC2 + Docker
- Engine: ___________________________________
- Connection String: ___________________________________

**Security Groups:**

| Component | Security Group | Inbound Rules |
|-----------|----------------|---------------|
| Frontend  | N/A (S3)       | Public HTTP/HTTPS |
| Backend   |                |                   |
| Database  |                |                   |

**Testing:**

1. **Frontend Test:**
   ```bash
   # URL: 
   # Status: 
   # Result: 
   ```

2. **Backend API Test:**
   ```bash
   # Endpoint: 
   # Response: 
   # Status: 
   ```

3. **Database Test:**
   ```bash
   # Connection test: 
   # Result: 
   ```

4. **End-to-End Flow:**
   ```
   Frontend → Backend → Database
   
   Test scenario:
   
   
   Result:
   
   ```

---

### **Cost Management**

**Current Costs:**
```bash
# Check current month costs
aws ce get-cost-and-usage \
  --time-period Start=2026-02-01,End=2026-02-28 \
  --granularity MONTHLY \
  --metrics BlendedCost

# Output:


```

**Resource Inventory:**

| Resource Type | Count | Monthly Cost | Free Tier Status |
|---------------|-------|--------------|------------------|
| EC2 t2.micro  |       |              |                  |
| EBS Volumes   |       |              |                  |
| S3 Buckets    |       |              |                  |
| Elastic IPs   |       |              |                  |
| Data Transfer |       |              |                  |

**Cost Optimization Actions:**

- [ ] Stopped unused EC2 instances
- [ ] Deleted unattached EBS volumes
- [ ] Released unused Elastic IPs
- [ ] Cleaned up old S3 objects
- [ ] Set up lifecycle policies
- [ ] Enabled cost allocation tags

**Billing Alerts Status:**
- [ ] CloudWatch billing alarms created
- [ ] Email notifications configured
- [ ] Budget alerts set up
- [ ] Cost anomaly detection enabled

---

## 🎯 Key Concepts Learned

### **IAM:**
```
1. Users vs Groups vs Roles:
   - 
   - 
   - 

2. Policies:
   - Managed policies: 
   - Inline policies: 
   - Resource-based policies: 

3. Access Keys:
   - When to use: 
   - When NOT to use: 
   - Best practices: 
```

### **EC2:**
```
1. Instance Types:
   - t2.micro: 
   - t3.small: 
   - Use cases: 

2. Security Groups:
   - Stateful vs stateless: 
   - Best practices: 
   - Common rules: 

3. User Data:
   - Purpose: 
   - Execution: 
   - Limitations: 
```

### **S3:**
```
1. Bucket Naming:
   - Rules: 
   - Best practices: 

2. Storage Classes:
   - Standard: 
   - Standard-IA: 
   - Glacier: 

3. Access Control:
   - Bucket policies: 
   - ACLs: 
   - IAM policies: 
```

### **VPC:**
```
1. CIDR Blocks:
   - Private IP ranges: 
   - Subnet sizing: 
   - Best practices: 

2. Public vs Private Subnets:
   - Difference: 
   - Use cases: 
   - Routing: 

3. NAT Gateway:
   - Purpose: 
   - Cost: 
   - Alternatives: 
```

---

## 💡 Important Commands

### **EC2 Management:**
```bash
# Launch instance:


# Stop instance:


# Terminate instance:


# Get instance details:


```

### **S3 Operations:**
```bash
# Create bucket:


# Upload file:


# Sync directory:


# Delete bucket:


```

### **VPC Commands:**
```bash
# Create VPC:


# Create subnet:


# Create Internet Gateway:


# Modify route table:


```

---

## ❓ Questions & Answers

### **Question 1:**
Q: 
A: 

### **Question 2:**
Q: 
A: 

### **Question 3:**
Q: 
A: 

### **Question 4:**
Q: 
A: 

### **Question 5:**
Q: 
A: 

---

## 🐛 Issues Encountered

### **Issue 1:**
**Problem:** 
**Solution:** 
**Time Spent:** 
**Lesson Learned:** 

### **Issue 2:**
**Problem:** 
**Solution:** 
**Time Spent:** 
**Lesson Learned:** 

### **Issue 3:**
**Problem:** 
**Solution:** 
**Time Spent:** 
**Lesson Learned:** 

---

## ✅ Daily Summary

### **Completed Tasks:**
- [ ] AWS account created with MFA
- [ ] IAM users and groups configured
- [ ] AWS CLI installed and configured
- [ ] EC2 instance launched
- [ ] S3 static website hosted
- [ ] Custom VPC created
- [ ] 3-tier application deployed
- [ ] Billing alerts configured
- [ ] Resources cleaned up

### **Time Breakdown:**
- Account Setup: _____ hours
- IAM Configuration: _____ hours
- EC2 Practice: _____ hours
- S3 Website: _____ hours
- VPC Setup: _____ hours
- Project Deployment: _____ hours
- Cost Optimization: _____ hours
- **Total:** _____ hours

### **Skills Gained:**
1. 
2. 
3. 
4. 
5. 

### **Next Steps:**
1. 
2. 
3. 
4. 
5. 

---

## 📊 Self-Assessment

Rate your understanding (1-5):

| Topic | Understanding | Confidence | Need Practice |
|-------|---------------|------------|---------------|
| IAM   |     /5        |    /5      | [ ]           |
| EC2   |     /5        |    /5      | [ ]           |
| S3    |     /5        |    /5      | [ ]           |
| VPC   |     /5        |    /5      | [ ]           |
| CLI   |     /5        |    /5      | [ ]           |
| Cost  |     /5        |    /5      | [ ]           |

**Overall Day Rating:** _____ /10

**What went well:**



**What could be improved:**



**Action items for tomorrow:**



---

## 🔗 Useful Resources Found

1. 
2. 
3. 
4. 
5. 

---

**Notes Date:** ___________________  
**Reviewed:** [ ] Yes [ ] No  
**Ready for Day 8:** [ ] Yes [ ] No
