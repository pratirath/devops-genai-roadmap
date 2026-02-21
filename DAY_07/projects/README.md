# Day 7 Project: Portfolio Website & 3-Tier Application on AWS

> **Build production-ready applications on AWS cloud platform**

---

## 🎯 Project Overview

In this hands-on project, you'll deploy **two complete applications** on AWS:

1. **Portfolio Website** - Static site on S3 with CloudFront CDN
2. **3-Tier Application** - Full-stack app (Frontend + Backend + Database)

**Skills You'll Practice:**
- AWS account management and security
- EC2 instance provisioning and management
- S3 bucket configuration and website hosting
- VPC networking and security groups
- Multi-tier architecture design
- Cost optimization strategies

---

## 📦 Project 1: Portfolio Website on S3

### **Architecture:**
```
User → CloudFront CDN → S3 Bucket (Static Website)
```

### **Features:**
- ✅ Responsive portfolio design
- ✅ Project showcase with tech stacks
- ✅ Learning stats dashboard
- ✅ Custom error pages
- ✅ Public access via bucket policy
- ✅ Optional: Custom domain with Route53

---

### **Quick Start (20 minutes)**

**Step 1: Create S3 Bucket**
```bash
# Create bucket (name must be globally unique)
aws s3 mb s3://devops-portfolio-yourname-2026

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket devops-portfolio-yourname-2026 \
  --versioning-configuration Status=Enabled

# Enable static website hosting
aws s3 website s3://devops-portfolio-yourname-2026/ \
  --index-document index.html \
  --error-document error.html
```

**Step 2: Create Website Files**

Save this as `index.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Portfolio - AWS S3</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        header { text-align: center; padding: 50px 0; }
        h1 { font-size: 3em; margin-bottom: 10px; }
        .subtitle { font-size: 1.2em; opacity: 0.9; }
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
        .projects { margin: 40px 0; }
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
        @media (max-width: 768px) {
            h1 { font-size: 2em; }
            .stats { grid-template-columns: 1fr; }
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
                <div class="stat-number">7</div>
                <div class="stat-label">Projects Done</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">40%</div>
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
                <h3>4. AWS Cloud Portfolio (This Site!)</h3>
                <p>Static website hosted on Amazon S3 with global distribution.</p>
                <div class="tech-stack">
                    <span class="tech-badge">AWS S3</span>
                    <span class="tech-badge">CloudFront</span>
                    <span class="tech-badge">Route53</span>
                    <span class="tech-badge">HTML/CSS</span>
                </div>
            </div>
        </div>

        <footer>
            <p>🌟 Hosted on Amazon S3 | Built with ❤️ during DevOps Learning Journey</p>
            <p style="margin-top: 10px;">GitHub: pratirath/devops-genai-roadmap</p>
            <p style="margin-top: 5px;">Email: rathodpratiksha798@gmail.com</p>
        </footer>
    </div>
</body>
</html>
```

Save this as `error.html`:
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
            margin: 0;
        }
        .error-container {
            padding: 40px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { font-size: 8em; margin: 0; }
        p { font-size: 1.5em; margin: 20px 0; }
        a {
            color: #ffd700;
            text-decoration: none;
            font-size: 1.2em;
            padding: 10px 20px;
            border: 2px solid #ffd700;
            border-radius: 5px;
            display: inline-block;
            margin-top: 20px;
            transition: all 0.3s;
        }
        a:hover {
            background: #ffd700;
            color: #667eea;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <h1>404</h1>
        <p>Oops! Page not found</p>
        <p style="font-size: 1em; opacity: 0.8;">The page you're looking for doesn't exist.</p>
        <a href="/">← Go Home</a>
    </div>
</body>
</html>
```

**Step 3: Upload Files**
```bash
# Upload files
aws s3 cp index.html s3://devops-portfolio-yourname-2026/
aws s3 cp error.html s3://devops-portfolio-yourname-2026/

# Verify upload
aws s3 ls s3://devops-portfolio-yourname-2026/
```

**Step 4: Make Bucket Public**

Create `bucket-policy.json`:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::devops-portfolio-yourname-2026/*"
    }
  ]
}
```

Apply policy:
```bash
# Disable block public access
aws s3api put-public-access-block \
  --bucket devops-portfolio-yourname-2026 \
  --public-access-block-configuration \
  "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

# Apply bucket policy
aws s3api put-bucket-policy \
  --bucket devops-portfolio-yourname-2026 \
  --policy file://bucket-policy.json
```

**Step 5: Access Your Website**
```bash
# Website URL (replace region and bucket name):
http://devops-portfolio-yourname-2026.s3-website-us-east-1.amazonaws.com

# Test in browser
open http://devops-portfolio-yourname-2026.s3-website-us-east-1.amazonaws.com
```

---

## 📦 Project 2: 3-Tier Application on AWS

### **Architecture:**
```
┌─────────────────────────────────────────────────────────┐
│                    Internet                              │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────┴────────────────────────────────┐
│                  Frontend Layer                          │
│         S3 Bucket (Static React/HTML)                   │
│              + CloudFront CDN                            │
└────────────────────────┬────────────────────────────────┘
                         │ HTTPS
┌────────────────────────┴────────────────────────────────┐
│                  Backend Layer                           │
│        EC2 Instance (t2.micro)                          │
│     Node.js/Python REST API                             │
│         Port 5000                                        │
└────────────────────────┬────────────────────────────────┘
                         │ Port 5432
┌────────────────────────┴────────────────────────────────┐
│                  Database Layer                          │
│      PostgreSQL (Docker on EC2)                         │
│         Private Subnet                                   │
└─────────────────────────────────────────────────────────┘
```

### **Quick Start (45 minutes)**

**Step 1: Create VPC and Subnets**

```bash
# Create VPC
VPC_ID=$(aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=AppVPC}]' \
  --query 'Vpc.VpcId' \
  --output text)

echo "VPC ID: $VPC_ID"

# Enable DNS hostnames
aws ec2 modify-vpc-attribute \
  --vpc-id $VPC_ID \
  --enable-dns-hostnames

# Create public subnet
PUBLIC_SUBNET=$(aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-Subnet}]' \
  --query 'Subnet.SubnetId' \
  --output text)

echo "Public Subnet: $PUBLIC_SUBNET"

# Create Internet Gateway
IGW_ID=$(aws ec2 create-internet-gateway \
  --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=AppIGW}]' \
  --query 'InternetGateway.InternetGatewayId' \
  --output text)

echo "Internet Gateway: $IGW_ID"

# Attach IGW to VPC
aws ec2 attach-internet-gateway \
  --vpc-id $VPC_ID \
  --internet-gateway-id $IGW_ID

# Create route table
ROUTE_TABLE=$(aws ec2 create-route-table \
  --vpc-id $VPC_ID \
  --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=Public-RT}]' \
  --query 'RouteTable.RouteTableId' \
  --output text)

echo "Route Table: $ROUTE_TABLE"

# Add route to Internet
aws ec2 create-route \
  --route-table-id $ROUTE_TABLE \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id $IGW_ID

# Associate route table with subnet
aws ec2 associate-route-table \
  --subnet-id $PUBLIC_SUBNET \
  --route-table-id $ROUTE_TABLE
```

**Step 2: Create Security Groups**

```bash
# Backend security group
BACKEND_SG=$(aws ec2 create-security-group \
  --group-name backend-sg \
  --description "Security group for backend API" \
  --vpc-id $VPC_ID \
  --query 'GroupId' \
  --output text)

echo "Backend SG: $BACKEND_SG"

# Allow SSH
aws ec2 authorize-security-group-ingress \
  --group-id $BACKEND_SG \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0

# Allow API port
aws ec2 authorize-security-group-ingress \
  --group-id $BACKEND_SG \
  --protocol tcp \
  --port 5000 \
  --cidr 0.0.0.0/0

# Allow PostgreSQL (from same SG)
aws ec2 authorize-security-group-ingress \
  --group-id $BACKEND_SG \
  --protocol tcp \
  --port 5432 \
  --source-group $BACKEND_SG
```

**Step 3: Create Key Pair**

```bash
# Create key pair
aws ec2 create-key-pair \
  --key-name app-key \
  --query 'KeyMaterial' \
  --output text > app-key.pem

# Set permissions
chmod 400 app-key.pem
```

**Step 4: Create Backend Server**

Create `backend-setup.sh`:
```bash
#!/bin/bash
set -e

# Update system
yum update -y

# Install Docker
yum install -y docker
systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Create application directory
mkdir -p /home/ec2-user/app
cd /home/ec2-user/app

# Create docker-compose.yml
cat > docker-compose.yml <<'EOF'
version: '3.8'

services:
  database:
    image: postgres:15
    container_name: app-db
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppass123
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data
    restart: always

  backend:
    image: node:18-alpine
    container_name: app-backend
    working_dir: /app
    volumes:
      - ./backend:/app
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://appuser:apppass123@database:5432/appdb
      PORT: 5000
    command: sh -c "npm install && npm start"
    depends_on:
      - database
    restart: always

volumes:
  db-data:
EOF

# Create backend app
mkdir -p backend
cd backend

# Create package.json
cat > package.json <<'EOF'
{
  "name": "backend-api",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "pg": "^8.11.0",
    "cors": "^2.8.5"
  }
}
EOF

# Create server.js
cat > server.js <<'EOF'
const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Database connection
const pool = new Pool({
  connectionString: process.env.DATABASE_URL
});

// Initialize database
pool.query(`
  CREATE TABLE IF NOT EXISTS visitors (
    id SERIAL PRIMARY KEY,
    count INTEGER DEFAULT 0,
    last_visit TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
`).then(() => {
  pool.query(`
    INSERT INTO visitors (count)
    SELECT 0
    WHERE NOT EXISTS (SELECT 1 FROM visitors)
  `);
});

// Routes
app.get('/', (req, res) => {
  res.json({
    message: 'AWS 3-Tier Application API',
    version: '1.0.0',
    endpoints: {
      health: '/health',
      stats: '/api/stats',
      increment: '/api/increment'
    }
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date() });
});

app.get('/api/stats', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM visitors LIMIT 1');
    res.json({
      visits: result.rows[0]?.count || 0,
      lastVisit: result.rows[0]?.last_visit
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/increment', async (req, res) => {
  try {
    await pool.query(`
      UPDATE visitors 
      SET count = count + 1, last_visit = CURRENT_TIMESTAMP
    `);
    const result = await pool.query('SELECT * FROM visitors LIMIT 1');
    res.json({
      visits: result.rows[0].count,
      lastVisit: result.rows[0].last_visit
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(port, '0.0.0.0', () => {
  console.log(`✅ Backend API running on port ${port}`);
});
EOF

# Start application
cd /home/ec2-user/app
docker-compose up -d

echo "✅ Application deployed successfully!"
```

Launch EC2 instance:
```bash
# Launch instance
INSTANCE_ID=$(aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name app-key \
  --security-group-ids $BACKEND_SG \
  --subnet-id $PUBLIC_SUBNET \
  --associate-public-ip-address \
  --user-data file://backend-setup.sh \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Backend-API}]' \
  --query 'Instances[0].InstanceId' \
  --output text)

echo "Instance ID: $INSTANCE_ID"

# Wait for instance to be running
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# Get public IP
PUBLIC_IP=$(aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text)

echo "✅ Backend server: http://$PUBLIC_IP:5000"
```

**Step 5: Create Frontend**

Create `frontend.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS 3-Tier Application</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            width: 100%;
            background: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        h1 { text-align: center; margin-bottom: 30px; }
        .stats {
            text-align: center;
            margin: 30px 0;
        }
        .stat-number {
            font-size: 4em;
            font-weight: bold;
            color: #ffd700;
        }
        .stat-label {
            font-size: 1.2em;
            opacity: 0.9;
            margin-top: 10px;
        }
        button {
            width: 100%;
            padding: 15px;
            font-size: 1.1em;
            background: #ffd700;
            color: #1e3c72;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        button:hover {
            background: #ffed4e;
            transform: scale(1.02);
        }
        .info {
            margin-top: 30px;
            padding: 20px;
            background: rgba(255,255,255,0.05);
            border-radius: 10px;
            font-size: 0.9em;
        }
        .info h3 { margin-bottom: 10px; color: #ffd700; }
        .status {
            text-align: center;
            margin: 20px 0;
            padding: 10px;
            border-radius: 5px;
        }
        .status.success { background: rgba(76, 175, 80, 0.3); }
        .status.error { background: rgba(244, 67, 54, 0.3); }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 AWS 3-Tier Application</h1>
        
        <div class="stats">
            <div class="stat-number" id="visitCount">Loading...</div>
            <div class="stat-label">Total Visits</div>
            <div style="margin-top: 10px; opacity: 0.7;">
                Last visit: <span id="lastVisit">-</span>
            </div>
        </div>

        <button onclick="incrementVisit()">Click to Visit</button>

        <div id="status" class="status" style="display: none;"></div>

        <div class="info">
            <h3>📊 Architecture</h3>
            <p><strong>Frontend:</strong> S3 Static Website</p>
            <p><strong>Backend:</strong> EC2 (Node.js API)</p>
            <p><strong>Database:</strong> PostgreSQL (Docker)</p>
            <p><strong>Network:</strong> VPC with public subnet</p>
            <br>
            <p><strong>Backend API:</strong> <span id="apiUrl"></span></p>
        </div>
    </div>

    <script>
        // Update this with your EC2 public IP
        const API_URL = 'http://YOUR_EC2_PUBLIC_IP:5000';
        
        document.getElementById('apiUrl').textContent = API_URL;

        async function getStats() {
            try {
                const response = await fetch(`${API_URL}/api/stats`);
                const data = await response.json();
                document.getElementById('visitCount').textContent = data.visits;
                document.getElementById('lastVisit').textContent = 
                    data.lastVisit ? new Date(data.lastVisit).toLocaleString() : 'Never';
            } catch (error) {
                console.error('Error:', error);
                document.getElementById('visitCount').textContent = 'Error';
            }
        }

        async function incrementVisit() {
            try {
                const response = await fetch(`${API_URL}/api/increment`, {
                    method: 'POST'
                });
                const data = await response.json();
                
                document.getElementById('visitCount').textContent = data.visits;
                document.getElementById('lastVisit').textContent = 
                    new Date(data.lastVisit).toLocaleString();
                
                showStatus('Visit recorded! 🎉', 'success');
            } catch (error) {
                console.error('Error:', error);
                showStatus('Failed to record visit', 'error');
            }
        }

        function showStatus(message, type) {
            const status = document.getElementById('status');
            status.textContent = message;
            status.className = `status ${type}`;
            status.style.display = 'block';
            setTimeout(() => {
                status.style.display = 'none';
            }, 3000);
        }

        // Load stats on page load
        getStats();
    </script>
</body>
</html>
```

Upload to S3:
```bash
# Replace YOUR_EC2_PUBLIC_IP with actual IP in frontend.html first!
sed -i '' "s/YOUR_EC2_PUBLIC_IP/$PUBLIC_IP/g" frontend.html

# Upload to S3
aws s3 cp frontend.html s3://devops-portfolio-yourname-2026/app.html

# Access at:
echo "Frontend: http://devops-portfolio-yourname-2026.s3-website-us-east-1.amazonaws.com/app.html"
```

---

## ✅ Testing Your Application

### **Test Backend API:**
```bash
# Health check
curl http://$PUBLIC_IP:5000/health

# Get stats
curl http://$PUBLIC_IP:5000/api/stats

# Increment counter
curl -X POST http://$PUBLIC_IP:5000/api/increment

# Check database
ssh -i app-key.pem ec2-user@$PUBLIC_IP
docker exec -it app-db psql -U appuser -d appdb -c "SELECT * FROM visitors;"
```

### **Test Frontend:**
1. Open browser to S3 website URL
2. Click "Click to Visit" button
3. Watch counter increment
4. Check database updates

---

## 🧹 Cleanup (Important!)

```bash
# Terminate EC2 instance
aws ec2 terminate-instances --instance-ids $INSTANCE_ID

# Delete security group (wait for instance to terminate first)
aws ec2 delete-security-group --group-id $BACKEND_SG

# Delete route table association
aws ec2 disassociate-route-table --association-id <association-id>

# Delete route table
aws ec2 delete-route-table --route-table-id $ROUTE_TABLE

# Detach and delete Internet Gateway
aws ec2 detach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID
aws ec2 delete-internet-gateway --internet-gateway-id $IGW_ID

# Delete subnet
aws ec2 delete-subnet --subnet-id $PUBLIC_SUBNET

# Delete VPC
aws ec2 delete-vpc --vpc-id $VPC_ID

# Delete S3 bucket
aws s3 rm s3://devops-portfolio-yourname-2026 --recursive
aws s3 rb s3://devops-portfolio-yourname-2026

# Delete key pair
aws ec2 delete-key-pair --key-name app-key
rm app-key.pem
```

---

## 📊 Project Success Metrics

By completing these projects, you'll have:

- ✅ **2 live applications** on AWS
- ✅ **S3 static website** with bucket policies
- ✅ **3-tier architecture** (Frontend + Backend + Database)
- ✅ **VPC networking** with public subnets
- ✅ **Security groups** properly configured
- ✅ **EC2 instance** management experience
- ✅ **Docker containerization** on cloud
- ✅ **Cost optimization** awareness

**Estimated Time:** 90 minutes  
**AWS Cost:** $0 (Free Tier)  
**Resume Value:** High! 🎯

---

## 🎓 What You Learned

1. **S3 Static Hosting:**
   - Bucket creation and configuration
   - Website hosting setup
   - Bucket policies for public access
   - Error page handling

2. **EC2 Management:**
   - Instance provisioning
   - User data scripts
   - SSH access
   - Application deployment

3. **VPC Networking:**
   - VPC creation
   - Subnet configuration
   - Internet Gateway setup
   - Route tables

4. **Security:**
   - Security groups
   - IAM best practices
   - Network isolation
   - Access control

5. **DevOps Skills:**
   - Infrastructure automation
   - Multi-tier architecture
   - Container orchestration
   - Cloud deployment

---

**Congratulations!** You've successfully deployed production-ready applications on AWS! 🎉

**Next:** Add CI/CD pipeline to automate deployments! 🚀
