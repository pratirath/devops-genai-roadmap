# 📅 Day 5 - Docker Networking & Security

**Date:** February 20, 2026  
**Focus:** Container networking, network isolation, security hardening, secrets management  
**Duration:** 8 hours (split across morning, afternoon, evening)

---

## 🎯 Learning Objectives

By the end of Day 5, you will be able to:

### Networking:
- ✅ Understand and implement Docker network drivers (bridge, host, overlay, none)
- ✅ Create custom bridge networks with custom subnets
- ✅ Configure inter-container communication and service discovery
- ✅ Implement network segmentation and isolation
- ✅ Master port mapping and publishing strategies
- ✅ Use network aliases for flexible service discovery
- ✅ Design multi-tier network architectures

### Security:
- ✅ Scan container images for vulnerabilities (Trivy, Scout, Snyk)
- ✅ Implement Docker secrets for sensitive data management
- ✅ Run containers as non-root users
- ✅ Configure read-only filesystems and tmpfs mounts
- ✅ Drop Linux capabilities and add only necessary ones
- ✅ Set resource limits (CPU, memory, PIDs)
- ✅ Apply security options (no-new-privileges)
- ✅ Create secure, hardened Dockerfiles

---

## 📚 Topics Covered

### Morning Session (6:00 - 9:00 AM)
1. **Docker Networking Fundamentals**
   - Network drivers: bridge, host, none, overlay, macvlan
   - Default vs custom networks
   - DNS-based service discovery
   - Network inspection and troubleshooting

2. **Advanced Networking Patterns**
   - Service discovery with container names
   - Network aliases and multiple names
   - Multi-network containers
   - Port mapping strategies
   - 3-tier network architecture lab

3. **Docker Security Fundamentals**
   - Image vulnerability scanning
   - Official vs community images
   - Content trust and image signing
   - Reducing attack surface (minimal base images)
   - Non-root user implementation
   - Read-only filesystems
   - Capability management
   - Resource limiting

### Afternoon Session (12:00 - 3:00 PM)
4. **Hands-On Project: Secure E-Commerce Microservices**
   - Multi-tier architecture with 4 isolated networks
   - Frontend, backend, database, payment network zones
   - Docker secrets integration
   - Complete security hardening
   - Health checks and dependency management
   - Resource limits and security options

### Evening Session (7:00 - 9:00 PM)
5. **Docker Secrets Management**
   - Creating and managing secrets
   - File-based vs swarm secrets
   - Reading secrets in applications (Python, Node.js)
   - Best practices for sensitive data

6. **Security Scanning & Hardening**
   - Comprehensive vulnerability scanning
   - Creating security baseline Dockerfiles
   - Automated security check scripts
   - Network security testing
   - Isolation verification

---

## 🏗️ Project Structure

```
DAY_05/
├── README.md                          # This file
├── docs/
│   ├── DAY_5_PLAN.md                 # Detailed 8-hour schedule
│   └── NETWORK_ARCHITECTURE.md       # Network design guide
├── notes/
│   └── day-05-notes.md               # Your learning notes
└── projects/
    └── secure-ecommerce/              # Main project
        ├── README.md
        ├── docker-compose.yml         # Multi-network compose file
        ├── .env.example
        ├── security-check.sh          # Security scanning script
        ├── services/
        │   ├── frontend/
        │   ├── api-gateway/
        │   ├── product-api/
        │   ├── order-api/
        │   └── payment-api/
        ├── nginx/
        │   └── conf.d/
        ├── database/
        │   └── migrations/
        └── secrets/
            ├── db_password.txt
            ├── payment_api_key.txt
            └── stripe_key.txt
```

---

## 🚀 Quick Start

### Prerequisites
```bash
# Ensure Docker is running
docker --version

# Install security scanning tools
brew install trivy  # macOS
# or
apt-get install trivy  # Linux

# Verify installation
trivy --version
```

### Get Started
```bash
# Navigate to Day 5
cd ~/DevOps-Roadmap/DAY_05

# Review the action plan
cat docs/DAY_5_PLAN.md

# Start with networking basics
docker network ls
docker network inspect bridge

# Create your first custom network
docker network create --driver bridge my-custom-network

# Inspect it
docker network inspect my-custom-network

# Start the secure e-commerce project (afternoon)
cd projects/secure-ecommerce
docker compose up -d

# Run security scan
./security-check.sh <image-name>
```

---

## 🛠️ Essential Commands Reference

### Network Management
```bash
# List all networks
docker network ls

# Create custom network
docker network create my-network

# Create network with custom subnet
docker network create --driver bridge \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1 \
  custom-net

# Inspect network
docker network inspect my-network

# Connect container to network
docker network connect my-network container-name

# Disconnect from network
docker network disconnect my-network container-name

# Remove network
docker network rm my-network

# Remove all unused networks
docker network prune
```

### Security Commands
```bash
# Scan image for vulnerabilities
trivy image nginx:latest
docker scout cves nginx:latest

# Check who container runs as
docker inspect nginx --format='{{.Config.User}}'

# Run as non-root
docker run -d --user 1001:1001 nginx

# Read-only filesystem
docker run -d --read-only --tmpfs /tmp nginx

# Drop all capabilities
docker run -d --cap-drop=ALL nginx

# Resource limits
docker run -d --memory="512m" --cpus="0.5" nginx

# Security options
docker run -d --security-opt=no-new-privileges nginx
```

### Secrets Management
```bash
# Create secret (Swarm mode)
echo "password123" | docker secret create db_pass -

# List secrets
docker secret ls

# Inspect secret
docker secret inspect db_pass

# Remove secret
docker secret rm db_pass
```

---

## 📖 Key Concepts

### Network Drivers

| Driver | Use Case | Isolation | External Access |
|--------|----------|-----------|-----------------|
| **bridge** | Default, single-host | Yes | Via port mapping |
| **host** | Performance-critical | No | Direct |
| **none** | Complete isolation | Complete | None |
| **overlay** | Multi-host (Swarm) | Yes | Configurable |
| **macvlan** | Legacy apps | Physical network | Direct |

### Security Best Practices

#### ✅ DO:
- Use official, verified images
- Scan images for vulnerabilities
- Run as non-root users
- Use minimal base images (Alpine, distroless)
- Implement secrets for sensitive data
- Set resource limits
- Use read-only filesystems where possible
- Drop unnecessary capabilities
- Keep images updated
- Use specific version tags (not `latest`)

#### ❌ DON'T:
- Run as root
- Hardcode secrets in images
- Use random community images
- Grant unnecessary capabilities
- Run with `--privileged` flag
- Expose unnecessary ports
- Skip vulnerability scanning
- Use outdated base images

---

## 🎯 Learning Milestones

### By End of Morning Session:
- [ ] Understand all network drivers
- [ ] Create custom networks
- [ ] Configure inter-container communication
- [ ] Implement network isolation
- [ ] Scan images for vulnerabilities
- [ ] Create non-root Dockerfiles

### By End of Afternoon Session:
- [ ] Build secure microservices architecture
- [ ] Implement 4 isolated networks
- [ ] Configure Docker secrets
- [ ] Apply security hardening
- [ ] Set resource limits
- [ ] Test network isolation

### By End of Evening Session:
- [ ] Master secrets management
- [ ] Run comprehensive security scans
- [ ] Create security baseline
- [ ] Verify isolation
- [ ] Document security measures

---

## 📊 Progress Tracker

**Overall Roadmap Progress:**
```
Day 1-2: Docker Basics         ✅ 100%
Day 3: Docker Compose          ✅ 100%
Day 4: Production Ready        ✅ 100%
Day 5: Network & Security      🔄 In Progress
Day 6-30: Advanced Topics      ⏳ Upcoming
```

**Today's Progress:**
```
Morning Session   ███░░░░░░░  30%
Afternoon Session ░░░░░░░░░░   0%
Evening Session   ░░░░░░░░░░   0%
```

---

## 🔗 Resources

### Official Documentation:
- [Docker Networking](https://docs.docker.com/network/)
- [Docker Security](https://docs.docker.com/engine/security/)
- [Docker Secrets](https://docs.docker.com/engine/swarm/secrets/)
- [Docker Security Best Practices](https://docs.docker.com/develop/security-best-practices/)

### Video Tutorials:
- [Docker Networking Crash Course](https://www.youtube.com/watch?v=bKFMS5C4CG0) - 30 min
- [Docker Security Best Practices](https://www.youtube.com/watch?v=KINjI1tlo2w) - 25 min
- [Docker Networks Explained](https://www.youtube.com/watch?v=Vegb37mK2KM) - 20 min

### Security Tools:
- [Trivy](https://github.com/aquasecurity/trivy) - Vulnerability scanner
- [Docker Scout](https://docs.docker.com/scout/) - Built-in scanning
- [Snyk](https://snyk.io/) - Security platform
- [Hadolint](https://github.com/hadolint/hadolint) - Dockerfile linter

### Advanced Reading:
- [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)

---

## 🎓 Mini-Challenges

Want extra practice? Try these:

### Challenge 1: Network Architect (30 min)
Design and implement a 4-tier network:
- DMZ (public-facing services)
- Application tier
- Backend services
- Database tier

Test isolation between tiers.

### Challenge 2: Security Hardening (45 min)
Take any existing Docker project:
- Add non-root user
- Implement secrets
- Add health checks
- Set resource limits
- Achieve <5 CRITICAL vulnerabilities

### Challenge 3: Zero-Trust Microservices (60 min)
Build services that:
- Authenticate each request
- Use mTLS between services
- Implement API gateway auth
- Log all access attempts

---

## 🏆 Success Criteria

You've successfully completed Day 5 if you can:

### Knowledge Check:
- [ ] Explain the 5 network drivers and when to use each
- [ ] Describe how Docker DNS works
- [ ] List 10 security best practices
- [ ] Explain Linux capabilities in containers
- [ ] Describe how Docker secrets work

### Practical Skills:
- [ ] Create isolated network architecture
- [ ] Implement Docker secrets
- [ ] Run vulnerability scans
- [ ] Harden Dockerfiles
- [ ] Configure resource limits
- [ ] Test network isolation

### Deliverables:
- [ ] Secure e-commerce project running
- [ ] All services in correct networks
- [ ] Secrets properly configured
- [ ] Security scan results documented
- [ ] Network architecture documented
- [ ] Code pushed to GitHub

---

## 🚀 Next Steps (Day 6)

**Preview: Kubernetes Fundamentals**
- Kubernetes architecture overview
- Pods, Deployments, Services concepts
- kubectl command line tool
- Minikube local setup
- Deploy first application to K8s
- Expose services
- Scale deployments

*Get ready to move beyond single-host Docker! 🎯*

---

## 💡 Pro Tips

1. **Network Naming:** Use descriptive names like `frontend-net`, `backend-net`, `db-net`
2. **Secrets Security:** Never commit secret files to Git (add to `.gitignore`)
3. **Scan Regularly:** Make security scanning part of your build process
4. **Test Isolation:** Always verify network isolation works as expected
5. **Documentation:** Document your network architecture - you'll forget it later
6. **Resource Limits:** Always set limits in production to prevent resource exhaustion
7. **Version Pinning:** Use specific versions in production, not `latest`

---

## 📝 Notes Section

Use `notes/day-05-notes.md` to document:
- Key concepts learned
- Commands practiced
- Issues encountered and solutions
- Questions for further research
- Personal insights and aha moments

---

## 🆘 Troubleshooting

### Network Issues:
```bash
# Container can't reach another container
- Check both are on same network
- Verify DNS resolution: docker exec container nslookup other-container
- Check network: docker network inspect network-name

# Port already in use
- Check what's using port: lsof -i :PORT
- Change port mapping in docker-compose.yml

# Network not isolated
- Ensure using internal: true for backend networks
- Test isolation: docker exec container1 ping container2
```

### Security Issues:
```bash
# Permission denied errors
- Check if running as non-root
- Verify file permissions
- Check volume mount ownership

# Secrets not working
- Ensure secret files exist
- Check file paths in docker-compose.yml
- Verify secret mounted at /run/secrets/
```

---

**Keep pushing! Today you're learning skills that separate senior engineers from juniors. Security = Job security! 🔒💰**
