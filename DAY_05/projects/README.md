# 🔒 Secure E-Commerce Microservices

A production-grade, security-hardened microservices architecture demonstrating Docker networking, network isolation, secrets management, and security best practices.

---

## 🏗️ Architecture

### Network Topology

```
                          Internet
                             |
                    [Nginx Reverse Proxy]
                     (80/443) - Public
                             |
                ┌────────────┴──────────────┐
                |                           |
          [Frontend Web]            [API Gateway]
           (React/Vue)                  (8080)
                |                           |
         frontend-net              ┌────────┴────────┐
                                   |                 |
                                   |                 |
                            [Product API]      [Order API]
                               (8001)            (8002)
                                   |                 |
                                   |                 |
                              backend-net       backend-net
                                   |                 |
                      ┌────────────┴─────┐           |
                      |                  |           |
                [Product DB]      [Payment API]  [Order DB]
                (PostgreSQL)         (8003)     (PostgreSQL)
                      |                  |           |
                database-net      payment-net   database-net
```

### Network Segmentation

| Network | Subnet | Internal | Purpose | Services |
|---------|--------|----------|---------|----------|
| **frontend** | 172.20.0.0/24 | No | Public-facing | nginx, frontend, api-gateway |
| **backend** | 172.21.0.0/24 | Yes | Business logic | api-gateway, product-api, order-api |
| **database** | 172.22.0.0/24 | Yes | Data persistence | product-db, order-db |
| **payment** | 172.23.0.0/24 | Yes | PCI compliance | payment-api, order-api |

### Service Communication Matrix

| From → To | Frontend | API Gateway | Product API | Order API | Payment API | Product DB | Order DB |
|-----------|----------|-------------|-------------|-----------|-------------|------------|----------|
| **Internet** | ✅ (80,443) | ✅ (via nginx) | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Frontend** | - | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **API Gateway** | ✅ | - | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Product API** | ❌ | ✅ | - | ❌ | ❌ | ✅ | ❌ |
| **Order API** | ❌ | ✅ | ❌ | - | ✅ | ❌ | ✅ |
| **Payment API** | ❌ | ❌ | ❌ | ✅ | - | ❌ | ❌ |

---

## 🔐 Security Features

### ✅ Network Security
- [x] **4 isolated networks** with custom subnets
- [x] **Internal networks** (backend, database, payment) with no external access
- [x] **Network segmentation** following zero-trust principles
- [x] **Least privilege** network access between services
- [x] **DMZ architecture** with nginx as only public-facing service

### ✅ Container Security
- [x] **Non-root users** in all containers (UID 1001)
- [x] **Read-only filesystems** where applicable
- [x] **Capability dropping** (drop ALL, add only needed)
- [x] **Security options** (no-new-privileges)
- [x] **Resource limits** (CPU, memory, PIDs)
- [x] **Health checks** for all services
- [x] **Minimal base images** (Alpine, slim variants)

### ✅ Secrets Management
- [x] **Docker secrets** for sensitive data
- [x] **No hardcoded credentials** in images or code
- [x] **File-based secrets** mounted at `/run/secrets/`
- [x] **Proper permissions** (600) on secret files
- [x] **Excluded from Git** (.gitignore configured)

### ✅ Best Practices
- [x] **Specific version tags** (no `latest`)
- [x] **Multi-stage builds** (future enhancement)
- [x] **Vulnerability scanning** with Trivy
- [x] **Dependency management**
- [x] **Graceful shutdown** handling

---

## 🚀 Quick Start

### Prerequisites
```bash
# Docker & Docker Compose
docker --version  # 20.10+
docker compose version  # 2.0+

# Security scanning (optional)
brew install trivy  # macOS
# or
apt-get install trivy  # Linux
```

### Setup

**1. Clone and navigate:**
```bash
cd ~/DevOps-Roadmap/DAY_05/projects/secure-ecommerce
```

**2. Create secrets:**
```bash
# Create secrets directory
mkdir -p secrets

# Generate secrets
echo "$(openssl rand -base64 32)" > secrets/db_password.txt
echo "$(openssl rand -base64 32)" > secrets/payment_api_key.txt
echo "sk_test_$(openssl rand -hex 16)" > secrets/stripe_key.txt

# Set proper permissions
chmod 600 secrets/*.txt

# Verify
ls -la secrets/
```

**3. Configure environment:**
```bash
# Copy example
cp .env.example .env

# Edit if needed
nano .env
```

**4. Build and start:**
```bash
# Build all services
docker compose build

# Start in detached mode
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f
```

**5. Verify services:**
```bash
# Check all containers are healthy
docker compose ps

# Should see:
# ✅ ecom-nginx          (healthy)
# ✅ ecom-frontend       (healthy)
# ✅ ecom-gateway        (healthy)
# ✅ ecom-product-api    (healthy)
# ✅ ecom-order-api      (healthy)
# ✅ ecom-payment-api    (healthy)
# ✅ ecom-product-db     (healthy)
# ✅ ecom-order-db       (healthy)
```

---

## 🧪 Testing

### API Endpoints

**Health Checks:**
```bash
# Nginx
curl http://localhost/health

# API Gateway
curl http://localhost/api/health

# Product API (via gateway)
curl http://localhost/api/products/health

# Order API (via gateway)
curl http://localhost/api/orders/health
```

**Product Service:**
```bash
# List products
curl http://localhost/api/products

# Get product
curl http://localhost/api/products/1

# Create product (POST)
curl -X POST http://localhost/api/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Laptop","price":999.99,"stock":10}'
```

**Order Service:**
```bash
# List orders
curl http://localhost/api/orders

# Create order
curl -X POST http://localhost/api/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id":1,"quantity":2}'
```

### Network Isolation Testing

**1. Verify frontend can't reach databases directly:**
```bash
# Should fail (timeout or connection refused)
docker exec ecom-frontend ping -c 2 ecom-product-db
docker exec ecom-frontend ping -c 2 ecom-order-db

# Expected: "ping: bad address" or timeout
```

**2. Verify product-api can reach its database:**
```bash
# Should succeed
docker exec ecom-product-api ping -c 2 product-db

# Expected: Successful ping responses
```

**3. Verify backend services can communicate:**
```bash
# Order API → Payment API (same backend + payment networks)
docker exec ecom-order-api curl -s http://payment-api:8003/health

# Expected: {"status":"healthy"}
```

**4. Verify payment API is isolated:**
```bash
# Product API → Payment API (should fail - different networks)
docker exec ecom-product-api curl -s http://payment-api:8003/health

# Expected: Connection timeout or refused
```

**5. DNS resolution test:**
```bash
# Check service discovery
docker exec ecom-gateway nslookup product-api
docker exec ecom-gateway nslookup order-api

# Expected: Resolved IP addresses
```

### Security Testing

**1. Verify non-root user:**
```bash
# Check all services run as non-root
docker exec ecom-product-api whoami
docker exec ecom-order-api whoami
docker exec ecom-payment-api whoami

# Expected: appuser (not root)
```

**2. Verify secrets are mounted:**
```bash
# Check secret files exist
docker exec ecom-product-api ls -l /run/secrets/
docker exec ecom-order-api ls -l /run/secrets/
docker exec ecom-payment-api ls -l /run/secrets/

# Expected: db_password, payment_api_key, stripe_key
```

**3. Run vulnerability scan:**
```bash
# Scan all custom images
./security-check.sh ecom-product-api
./security-check.sh ecom-order-api
./security-check.sh ecom-payment-api

# Expected: Scan results with vulnerability counts
```

---

## 📊 Monitoring

### Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f product-api

# Last 100 lines
docker compose logs --tail=100

# Since 10 minutes ago
docker compose logs --since=10m
```

### Resource Usage
```bash
# Stats for all containers
docker stats

# Specific container
docker stats ecom-product-api

# Check resource limits
docker inspect ecom-product-api --format='{{.HostConfig.Memory}}'
docker inspect ecom-product-api --format='{{.HostConfig.CpuQuota}}'
```

### Network Inspection
```bash
# List networks
docker network ls

# Inspect specific network
docker network inspect secure-ecommerce_frontend
docker network inspect secure-ecommerce_backend
docker network inspect secure-ecommerce_database
docker network inspect secure-ecommerce_payment

# See which containers are on a network
docker network inspect secure-ecommerce_backend --format='{{range .Containers}}{{.Name}} {{end}}'
```

---

## 🛠️ Maintenance

### Secrets Rotation
```bash
# 1. Stop services
docker compose down

# 2. Generate new secrets
echo "$(openssl rand -base64 32)" > secrets/db_password.txt
echo "$(openssl rand -base64 32)" > secrets/payment_api_key.txt

# 3. Update database passwords
# (Manual DB update required)

# 4. Restart
docker compose up -d
```

### Backup
```bash
# Backup databases
docker exec ecom-product-db pg_dump -U productuser products > backup_products.sql
docker exec ecom-order-db pg_dump -U orderuser orders > backup_orders.sql

# Backup volumes
docker run --rm \
  -v secure-ecommerce_product_data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/product_data.tar.gz -C /data .
```

### Restore
```bash
# Restore database
cat backup_products.sql | docker exec -i ecom-product-db psql -U productuser products

# Restore volume
docker run --rm \
  -v secure-ecommerce_product_data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar xzf /backup/product_data.tar.gz -C /data
```

### Updates
```bash
# Pull latest images
docker compose pull

# Rebuild services
docker compose build --no-cache

# Rolling update
docker compose up -d --force-recreate --no-deps service-name
```

---

## 🐛 Troubleshooting

### Service won't start
```bash
# Check logs
docker compose logs service-name

# Check health
docker compose ps

# Inspect container
docker inspect ecom-service-name
```

### Network issues
```bash
# Verify networks exist
docker network ls | grep ecommerce

# Check container network
docker inspect ecom-service-name --format='{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}'

# Test connectivity
docker exec ecom-gateway ping product-api
```

### Secrets not working
```bash
# Verify secret files exist
ls -la secrets/

# Check permissions
chmod 600 secrets/*.txt

# Verify mounted in container
docker exec ecom-product-api ls -l /run/secrets/
```

### Database connection failures
```bash
# Check database is healthy
docker compose ps product-db

# Test connection
docker exec ecom-product-db pg_isready -U productuser

# Check logs
docker compose logs product-db
```

### Port conflicts
```bash
# Check what's using port
lsof -i :80
lsof -i :443

# Change ports in docker-compose.yml
# ports:
#   - "8080:80"  # Use 8080 instead
```

---

## 📁 Project Structure

```
secure-ecommerce/
├── README.md                          # This file
├── docker-compose.yml                 # Main orchestration
├── .env.example                       # Environment template
├── .gitignore                         # Excludes secrets, data
├── security-check.sh                  # Security scanning script
│
├── services/
│   ├── frontend/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── src/
│   │   └── public/
│   │
│   ├── api-gateway/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── app.py
│   │
│   ├── product-api/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── app.py
│   │   └── models.py
│   │
│   ├── order-api/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── app.py
│   │   └── models.py
│   │
│   └── payment-api/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── app.py
│
├── nginx/
│   ├── nginx.conf
│   └── conf.d/
│       └── default.conf
│
├── database/
│   └── migrations/
│       ├── products_schema.sql
│       └── orders_schema.sql
│
└── secrets/                          # Gitignored
    ├── db_password.txt
    ├── payment_api_key.txt
    └── stripe_key.txt
```

---

## 🔒 Security Audit Checklist

### ✅ Completed

- [x] Network segmentation implemented
- [x] Internal networks configured
- [x] Non-root users in all containers
- [x] Secrets management in place
- [x] Resource limits set
- [x] Health checks configured
- [x] Minimal base images used
- [x] Capabilities dropped
- [x] Security options applied
- [x] Read-only filesystems (where possible)

### 🔄 Future Enhancements

- [ ] Implement mTLS between services
- [ ] Add API rate limiting
- [ ] Implement distributed tracing
- [ ] Add centralized logging (ELK stack)
- [ ] Set up monitoring (Prometheus/Grafana)
- [ ] Implement service mesh (Istio/Linkerd)
- [ ] Add WAF for nginx
- [ ] Implement RBAC
- [ ] Add audit logging
- [ ] Set up CI/CD pipeline with security gates

---

## 📚 Learning Outcomes

After completing this project, you understand:

### Networking:
- ✅ How to design multi-tier network architecture
- ✅ Network segmentation and isolation
- ✅ Service discovery with Docker DNS
- ✅ Internal vs external networks
- ✅ Network troubleshooting

### Security:
- ✅ Docker secrets management
- ✅ Running containers as non-root
- ✅ Linux capabilities in containers
- ✅ Resource limiting and isolation
- ✅ Vulnerability scanning
- ✅ Security hardening techniques

### Production Readiness:
- ✅ Health checks and dependencies
- ✅ Graceful degradation
- ✅ Logging and monitoring
- ✅ Backup and restore
- ✅ Secrets rotation

---

## 🎯 Interview Questions You Can Answer

1. **"How do you secure Docker containers?"**
   - Run as non-root users
   - Use Docker secrets for sensitive data
   - Scan images for vulnerabilities
   - Drop unnecessary capabilities
   - Set resource limits
   - Use read-only filesystems
   - Implement network segmentation

2. **"Explain Docker networking in microservices"**
   - Custom bridge networks for service groups
   - Internal networks for backend services
   - DNS-based service discovery
   - Network segmentation for security
   - Multiple networks per container for routing

3. **"How do you implement zero-trust in Docker?"**
   - Network isolation (least privilege)
   - Service-to-service authentication
   - No implicit trust between services
   - Secrets management
   - Audit logging

4. **"What's your Docker security checklist?"**
   - (Reference the Security Audit Checklist above)

---

## 📈 Real-World Applications

This architecture is production-ready and similar to:

- **E-Commerce Platforms:** Amazon, Shopify
- **SaaS Applications:** Stripe, Twilio
- **Financial Services:** Payment processors (PCI compliance)
- **Healthcare:** HIPAA-compliant systems
- **Enterprise:** Zero-trust environments

**Companies using similar patterns:**
- Netflix (microservices)
- Uber (network segmentation)
- Airbnb (secrets management)
- Stripe (PCI compliance zones)

---

## 🆘 Support

**Issues?**
- Check logs: `docker compose logs -f`
- Verify networks: `docker network ls`
- Test isolation: `docker exec container ping other`
- Run security check: `./security-check.sh`

**Questions?**
- Review Day 5 plan: `DAY_05/docs/DAY_5_PLAN.md`
- Check Docker docs: https://docs.docker.com
- OWASP security guide: https://cheatsheetseries.owasp.org/

---

## 📝 License

MIT License - Free to use for learning and commercial projects

---

## 🎉 Congratulations!

You've built a production-grade, security-hardened microservices architecture! 🔒

**Skills demonstrated:**
- ✅ Advanced Docker networking
- ✅ Security best practices
- ✅ Secrets management
- ✅ Zero-trust architecture
- ✅ Production-ready deployments

**Resume-worthy achievement! 💼**

---

**Built with ❤️ for DevOps learners aiming for 20+ LPA roles! 🚀**
