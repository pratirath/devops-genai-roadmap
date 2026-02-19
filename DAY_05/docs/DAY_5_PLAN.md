# 📅 Day 5 Action Plan - Docker Networking & Security

**Date:** February 19, 2026  
**Focus:** Docker Networks, Container Security, Secrets Management  
**Goal:** Master container networking and implement security best practices

---

## ✅ Previous Days' Achievements

**Day 1-2:** Docker Fundamentals ✅
- Mastered container basics and commands
- Built custom Dockerfiles

**Day 3:** Docker Compose ✅
- Multi-container orchestration
- 2 full-stack projects completed

**Day 4:** Production Readiness ✅
- Volumes and data persistence
- Multi-stage builds
- Image optimization

**You're on fire! 🔥 Now let's master networking and security!**

---

## 🎯 Today's Learning Objectives

By end of Day 5, you will:
- ✅ Understand Docker networking models
- ✅ Create and manage custom networks
- ✅ Master inter-container communication
- ✅ Implement network security and isolation
- ✅ Learn Docker security best practices
- ✅ Use Docker secrets for sensitive data
- ✅ Scan containers for vulnerabilities
- ✅ Build a secure microservices architecture

---

## 🎯 Today's Schedule

### **Morning Session (6:00 - 9:00 AM) - 3 hours**

#### 6:00 - 7:00 AM: Docker Networking Fundamentals (60 min)

**Understand Network Drivers:**

**1. Bridge Network (Default)**
- Default network for standalone containers
- Containers on same bridge can communicate
- Isolated from host network

**2. Host Network**
- Container shares host network stack
- No network isolation
- Better performance, less security

**3. None Network**
- No network access
- Complete isolation
- For security-sensitive tasks

**4. Overlay Network**
- Multi-host networking
- Used in Docker Swarm/Kubernetes
- Spans multiple Docker daemons

**5. Macvlan Network**
- Assigns MAC address to container
- Container appears as physical device
- Direct connection to network

**Watch:**
- [Docker Networking Crash Course](https://www.youtube.com/watch?v=bKFMS5C4CG0) - 30 min
- [Docker Networks Explained](https://www.youtube.com/watch?v=Vegb37mK2KM) - 20 min

**Practice Commands:**
```bash
# List networks
docker network ls

# Inspect default bridge
docker network inspect bridge

# Create custom bridge network
docker network create my-network

# Create network with custom subnet
docker network create --driver bridge \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1 \
  custom-network

# Run container in specific network
docker run -d --name web --network my-network nginx

# Connect running container to network
docker network connect my-network container-name

# Disconnect from network
docker network disconnect my-network container-name

# Inspect network
docker network inspect my-network

# Remove network
docker network rm my-network

# Prune unused networks
docker network prune
```

**Key Concepts:**
- DNS resolution between containers
- Network aliases
- Port publishing vs exposing
- Network drivers and use cases
- Container-to-container communication

---

#### 7:00 - 8:00 AM: Advanced Networking Patterns (60 min)

**1. Service Discovery with DNS:**
```bash
# Create network
docker network create app-network

# Run backend container
docker run -d --name backend \
  --network app-network \
  my-backend-image

# Run frontend container
docker run -d --name frontend \
  --network app-network \
  -e BACKEND_URL=http://backend:8080 \
  my-frontend-image

# Frontend can reach backend by name!
# No hardcoded IPs needed
```

**2. Network Aliases:**
```bash
# Multiple names for same container
docker run -d --name db \
  --network app-network \
  --network-alias database \
  --network-alias postgres \
  postgres:15

# Accessible as: db, database, or postgres
```

**3. Multiple Networks:**
```bash
# Frontend network (public-facing)
docker network create frontend-net

# Backend network (internal only)
docker network create backend-net

# API gateway in both networks
docker run -d --name gateway \
  --network frontend-net \
  --network backend-net \
  nginx

# Backend only in backend network
docker run -d --name api \
  --network backend-net \
  my-api

# Frontend only in frontend network
docker run -d --name web \
  --network frontend-net \
  my-web-app
```

**4. Port Mapping:**
```bash
# Publish specific port
docker run -d -p 8080:80 nginx

# Publish to specific interface
docker run -d -p 127.0.0.1:8080:80 nginx

# Publish all exposed ports randomly
docker run -d -P nginx

# Publish multiple ports
docker run -d -p 80:80 -p 443:443 nginx
```

**Practice Lab:**
Create a 3-tier app with isolated networks:
```yaml
networks:
  frontend:
  backend:
  database:

services:
  web:
    networks:
      - frontend
  
  api:
    networks:
      - frontend
      - backend
  
  db:
    networks:
      - backend
```

---

#### 8:00 - 9:00 AM: Docker Security Fundamentals (60 min)

**Watch:**
- [Docker Security Best Practices](https://www.youtube.com/watch?v=KINjI1tlo2w) - 25 min

**1. Image Security:**

**Scan for Vulnerabilities:**
```bash
# Using Docker Scout (built-in)
docker scout cves nginx:latest

# Using Trivy
brew install trivy
trivy image nginx:latest

# Using Snyk
docker scan nginx:latest
```

**2. Use Official & Verified Images:**
```bash
# ✅ Official images
FROM nginx:1.25-alpine
FROM postgres:15-alpine
FROM python:3.11-slim

# ❌ Random community images
FROM random-user/nginx
```

**3. Sign and Verify Images:**
```bash
# Enable Docker Content Trust
export DOCKER_CONTENT_TRUST=1

# Now only signed images can be pulled
docker pull nginx:latest
```

**4. Reduce Attack Surface:**
```dockerfile
# ❌ Large base image with unnecessary tools
FROM ubuntu:latest
RUN apt-get install -y curl wget vim git

# ✅ Minimal base image
FROM alpine:3.19
RUN apk add --no-cache curl
```

**5. Run as Non-Root:**
```dockerfile
# Create and use non-root user
FROM alpine:3.19

RUN addgroup -g 1001 appgroup && \
    adduser -u 1001 -G appgroup -s /bin/sh -D appuser

USER appuser

WORKDIR /app
COPY --chown=appuser:appgroup . .

CMD ["./app"]
```

**6. Read-Only Filesystem:**
```bash
# Run with read-only root filesystem
docker run -d --read-only \
  --tmpfs /tmp \
  --tmpfs /var/run \
  nginx
```

**7. Drop Capabilities:**
```bash
# Drop all capabilities, add only needed ones
docker run -d \
  --cap-drop=ALL \
  --cap-add=NET_BIND_SERVICE \
  nginx
```

**8. Resource Limits:**
```bash
# Limit CPU and memory
docker run -d \
  --memory="512m" \
  --memory-swap="1g" \
  --cpus="0.5" \
  --pids-limit=100 \
  nginx
```

---

### **Afternoon Session (12:00 - 3:00 PM) - 3 hours**

#### 12:00 - 3:00 PM: Project - Secure Microservices Network

**Build:** E-Commerce Microservices with Network Isolation

**Project Structure:**
```bash
mkdir -p ~/DevOps-Roadmap/DAY_05/projects/secure-ecommerce
cd ~/DevOps-Roadmap/DAY_05/projects/secure-ecommerce

mkdir -p services/{frontend,product-api,order-api,payment-api}
mkdir -p database/migrations
mkdir -p nginx/conf.d
mkdir -p secrets
touch docker-compose.yml .env.example README.md
```

**Architecture:**
```
                    Internet
                       |
                   [Nginx Proxy]
                       |
              ┌────────┴────────┐
              |                 |
         [Frontend]        [API Gateway]
              |                 |
         frontend-net    ┌──────┴──────┐
                         |             |
                   [Product API]  [Order API]
                         |             |
                    backend-net    backend-net
                         |             |
                   [Product DB]  [Order DB]
                         |             |
                    database-net  database-net
```

**Network Segmentation:**
1. **Frontend Network:** Public-facing services
2. **Backend Network:** Internal APIs
3. **Database Network:** Data layer (most secure)
4. **Payment Network:** Isolated for PCI compliance

**Create `docker-compose.yml`:**
```yaml
version: '3.8'

networks:
  frontend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
  
  backend:
    driver: bridge
    internal: true  # No external access
    ipam:
      config:
        - subnet: 172.21.0.0/24
  
  database:
    driver: bridge
    internal: true
    ipam:
      config:
        - subnet: 172.22.0.0/24
  
  payment:
    driver: bridge
    internal: true
    ipam:
      config:
        - subnet: 172.23.0.0/24

services:
  # Nginx Reverse Proxy (Public-facing)
  nginx:
    image: nginx:alpine
    container_name: ecom-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    networks:
      - frontend
    depends_on:
      - frontend
      - api-gateway
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 128M
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /var/cache/nginx
      - /var/run
    restart: unless-stopped

  # Frontend (React/Vue/Angular)
  frontend:
    build: ./services/frontend
    container_name: ecom-frontend
    environment:
      - API_URL=http://api-gateway:8080
    networks:
      - frontend
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp
    restart: unless-stopped

  # API Gateway (Routes to microservices)
  api-gateway:
    build: ./services/api-gateway
    container_name: ecom-gateway
    networks:
      - frontend
      - backend
    environment:
      - PRODUCT_SERVICE=http://product-api:8001
      - ORDER_SERVICE=http://order-api:8002
      - PAYMENT_SERVICE=http://payment-api:8003
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    security_opt:
      - no-new-privileges:true
    restart: unless-stopped

  # Product Microservice
  product-api:
    build: ./services/product-api
    container_name: ecom-product-api
    networks:
      - backend
      - database
    environment:
      - DB_HOST=product-db
      - DB_NAME=products
      - DB_USER=productuser
      - DB_PASSWORD_FILE=/run/secrets/db_password
    secrets:
      - db_password
    depends_on:
      product-db:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    restart: unless-stopped

  # Product Database
  product-db:
    image: postgres:15-alpine
    container_name: ecom-product-db
    networks:
      - database
    environment:
      - POSTGRES_DB=products
      - POSTGRES_USER=productuser
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - product_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U productuser"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    security_opt:
      - no-new-privileges:true
    restart: unless-stopped

  # Order Microservice
  order-api:
    build: ./services/order-api
    container_name: ecom-order-api
    networks:
      - backend
      - database
      - payment  # Can access payment service
    environment:
      - DB_HOST=order-db
      - DB_NAME=orders
      - DB_USER=orderuser
      - DB_PASSWORD_FILE=/run/secrets/db_password
      - PAYMENT_SERVICE=http://payment-api:8003
    secrets:
      - db_password
      - payment_api_key
    depends_on:
      order-db:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8002/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    restart: unless-stopped

  # Order Database
  order-db:
    image: postgres:15-alpine
    container_name: ecom-order-db
    networks:
      - database
    environment:
      - POSTGRES_DB=orders
      - POSTGRES_USER=orderuser
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - order_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U orderuser"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    security_opt:
      - no-new-privileges:true
    restart: unless-stopped

  # Payment Microservice (Highly Isolated)
  payment-api:
    build: ./services/payment-api
    container_name: ecom-payment-api
    networks:
      - payment  # Only in payment network
    environment:
      - STRIPE_KEY_FILE=/run/secrets/stripe_key
      - PAYMENT_PROCESSOR=stripe
    secrets:
      - stripe_key
      - payment_api_key
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8003/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 256M
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    read_only: true
    tmpfs:
      - /tmp
    restart: unless-stopped

secrets:
  db_password:
    file: ./secrets/db_password.txt
  payment_api_key:
    file: ./secrets/payment_api_key.txt
  stripe_key:
    file: ./secrets/stripe_key.txt

volumes:
  product_data:
  order_data:
```

**Security Features Implemented:**
1. ✅ Network segmentation (4 isolated networks)
2. ✅ Internal networks (no external access)
3. ✅ Docker secrets for sensitive data
4. ✅ Non-root users in all containers
5. ✅ Read-only filesystems
6. ✅ Capability dropping
7. ✅ Resource limits
8. ✅ Health checks
9. ✅ Security options (no-new-privileges)
10. ✅ Tmpfs for temporary data

---

### **Evening Session (7:00 - 9:00 PM) - 2 hours**

#### 7:00 - 8:00 PM: Docker Secrets Management

**1. Create Secrets:**
```bash
# Create secret files
mkdir -p secrets
echo "super_secret_db_password" > secrets/db_password.txt
echo "payment_api_secret_key_123" > secrets/payment_api_key.txt
echo "sk_test_stripe_key_xyz" > secrets/stripe_key.txt

# Set proper permissions
chmod 600 secrets/*.txt
```

**2. Using Secrets in Docker Swarm:**
```bash
# Initialize swarm (for secrets support)
docker swarm init

# Create secret
echo "my_secret_password" | docker secret create db_password -

# List secrets
docker secret ls

# Inspect secret (won't show value)
docker secret inspect db_password

# Use secret in service
docker service create \
  --name db \
  --secret db_password \
  -e POSTGRES_PASSWORD_FILE=/run/secrets/db_password \
  postgres:15-alpine

# Secret is mounted at /run/secrets/db_password
```

**3. Using Secrets in Docker Compose:**
```yaml
secrets:
  db_password:
    file: ./secrets/db_password.txt
  # Or from environment
  api_key:
    environment: "API_KEY"

services:
  app:
    secrets:
      - db_password
      - api_key
```

**4. Reading Secrets in Application:**

**Python:**
```python
import os

def get_secret(secret_name):
    secret_path = f'/run/secrets/{secret_name}'
    if os.path.exists(secret_path):
        with open(secret_path, 'r') as f:
            return f.read().strip()
    return os.getenv(secret_name)  # Fallback to env var

# Usage
db_password = get_secret('db_password')
stripe_key = get_secret('stripe_key')
```

**Node.js:**
```javascript
const fs = require('fs');
const path = require('path');

function getSecret(secretName) {
  const secretPath = path.join('/run/secrets', secretName);
  
  if (fs.existsSync(secretPath)) {
    return fs.readFileSync(secretPath, 'utf8').trim();
  }
  
  return process.env[secretName];
}

// Usage
const dbPassword = getSecret('db_password');
const stripeKey = getSecret('stripe_key');
```

---

#### 8:00 - 9:00 PM: Security Scanning & Hardening

**1. Scan Images for Vulnerabilities:**
```bash
# Using Docker Scout
docker scout cves nginx:latest
docker scout recommendations nginx:latest

# Using Trivy (comprehensive)
trivy image python:3.11-slim

# Scan and fail on HIGH/CRITICAL
trivy image --severity HIGH,CRITICAL python:3.11-slim

# Generate report
trivy image --format json -o report.json nginx:latest

# Using Snyk
snyk container test nginx:latest
```

**2. Create Security Baseline Dockerfile:**
```dockerfile
# Use specific version (not latest)
FROM python:3.11.8-alpine3.19

# Create non-root user
RUN addgroup -g 1001 appgroup && \
    adduser -u 1001 -G appgroup -s /bin/sh -D appuser

# Set working directory
WORKDIR /app

# Install dependencies as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    # Clean up
    rm -rf /root/.cache

# Copy application
COPY --chown=appuser:appgroup . .

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Expose port (documentation only)
EXPOSE 8000

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
```

**3. Security Checklist Script:**
```bash
#!/bin/bash
# security-check.sh

echo "🔍 Docker Security Scan"
echo "======================="

IMAGE=$1

if [ -z "$IMAGE" ]; then
  echo "Usage: ./security-check.sh <image-name>"
  exit 1
fi

echo "📦 Scanning image: $IMAGE"
echo ""

# 1. Scan for vulnerabilities
echo "1️⃣ Vulnerability Scan (Trivy):"
trivy image --severity HIGH,CRITICAL $IMAGE

# 2. Check if running as root
echo ""
echo "2️⃣ Checking for root user:"
USER=$(docker inspect $IMAGE --format='{{.Config.User}}')
if [ -z "$USER" ]; then
  echo "❌ WARNING: Container runs as root!"
else
  echo "✅ Running as user: $USER"
fi

# 3. Check image age
echo ""
echo "3️⃣ Checking image age:"
CREATED=$(docker inspect $IMAGE --format='{{.Created}}')
echo "Created: $CREATED"

# 4. Check for secrets
echo ""
echo "4️⃣ Checking for secrets in image:"
docker history --no-trunc $IMAGE | grep -i -E 'password|secret|key|token' && \
  echo "❌ WARNING: Possible secrets found!" || \
  echo "✅ No obvious secrets found"

# 5. Check size
echo ""
echo "5️⃣ Image size:"
docker images $IMAGE --format "{{.Size}}"

echo ""
echo "✅ Security scan complete!"
```

**Make executable:**
```bash
chmod +x security-check.sh
./security-check.sh nginx:latest
```

**4. Network Security Testing:**
```bash
# Test network isolation
docker exec container1 ping container2

# Should fail if on different isolated networks
# Should succeed if on same network

# Check which networks container is on
docker inspect container-name --format='{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}'

# Monitor network traffic
docker run --rm --net=container:container-name nicolaka/netshoot tcpdump

# Test DNS resolution
docker exec container nslookup other-container
```

---

## 🎯 Mini-Challenges (Choose 2)

### Challenge 1: Network Architect
- Design 4-tier network architecture
- Implement DMZ, backend, database zones
- Test isolation between networks
- Document security benefits

### Challenge 2: Security Hardening
- Take existing project
- Add all security features
- Scan for vulnerabilities
- Achieve <10 HIGH/CRITICAL issues

### Challenge 3: Zero-Trust Microservices
- Implement service-to-service authentication
- Use mutual TLS between services
- Add API gateway with auth
- Document security model

---

## 📝 Today's Deliverables

**By end of Day 5, you must have:**

1. ✅ **Secure E-Commerce Project**
   - 4 isolated networks
   - Docker secrets implementation
   - Security hardening
   - Vulnerability scanning

2. ✅ **Security Documentation**
   - Network architecture diagram
   - Security measures implemented
   - Scan results and remediation
   - Best practices checklist

3. ✅ **Network Lab Results**
   - Custom network configurations
   - DNS resolution tests
   - Isolation verification
   - Port mapping examples

4. ✅ **GitHub Update**
   - Push DAY_05 projects
   - Update main README
   - Add security documentation

---

## 📚 Resources for Today

### Videos:
- [Docker Networking](https://www.youtube.com/watch?v=bKFMS5C4CG0)
- [Docker Security](https://www.youtube.com/watch?v=KINjI1tlo2w)
- [Microservices Security](https://www.youtube.com/watch?v=Yd2AkgRUTLI)

### Documentation:
- [Docker Networks](https://docs.docker.com/network/)
- [Docker Security](https://docs.docker.com/engine/security/)
- [Secrets Management](https://docs.docker.com/engine/swarm/secrets/)

### Tools:
- [Trivy](https://github.com/aquasecurity/trivy)
- [Docker Scout](https://docs.docker.com/scout/)
- [Snyk](https://snyk.io/)

---

## ✅ End of Day Checklist

- [ ] Completed networking tutorials
- [ ] Created custom networks
- [ ] Tested network isolation
- [ ] Implemented Docker secrets
- [ ] Scanned images for vulnerabilities
- [ ] Built secure microservices project
- [ ] Documented security measures
- [ ] Ran security checks
- [ ] Updated GitHub repository
- [ ] Documented learnings

---

## 🎯 Success Metrics

**Knowledge:**
- [ ] Explain 5 network drivers
- [ ] Describe network isolation
- [ ] List 10 security best practices
- [ ] Understand secrets management

**Practical:**
- [ ] Created isolated network architecture
- [ ] Implemented Docker secrets
- [ ] Passed security scans
- [ ] Built secure microservices

---

## 🚀 Tomorrow's Preview (Day 6)

**Focus:** Kubernetes Fundamentals
- Kubernetes architecture
- Pods, Deployments, Services
- kubectl commands
- Minikube setup
- Deploy first app to K8s

**Get ready to level up! 🔥**

---

## 💪 Motivational Reminder

**Day 5 Progress:**
```
██████████░░░░░░░░░░░░░░ 25% Complete
```

**What you've mastered:**
- ✅ Docker fundamentals
- ✅ Multi-container apps
- ✅ Data persistence
- ✅ Image optimization
- ✅ Networking (today!)
- ✅ Security (today!)

**You're building enterprise-level skills! 🎯**

Security and networking knowledge = Premium DevOps Engineer = Higher salary! 💰

---

**Ready? Let's secure those containers! 🔒**

*Remember: Security isn't optional - it's essential. Companies pay top dollar for engineers who understand container security! Keep pushing! 💪*
