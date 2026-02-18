# DAY 04 - Advanced Docker: Volumes, Multi-Stage Builds & Production Best Practices

## 📅 Date: February 19, 2026

## 🎯 Today's Focus: Data Persistence, Image Optimization & Production Readiness

### 📝 Learning Objectives
- [ ] Master Docker volumes and data persistence
- [ ] Understand bind mounts vs named volumes
- [ ] Learn multi-stage Docker builds
- [ ] Optimize Docker images for production
- [ ] Implement Docker best practices
- [ ] Build production-ready containerized applications
- [ ] Push images to Docker Hub

---

## 📚 Topics Covered

### 1. **Docker Volumes & Data Persistence**
- Types of mounts (volumes, bind mounts, tmpfs)
- Named volumes vs anonymous volumes
- Volume lifecycle management
- Backup and restore strategies
- Volume drivers

### 2. **Multi-Stage Docker Builds**
- Why multi-stage builds?
- Build stage vs runtime stage
- Copying artifacts between stages
- Image size optimization
- Security benefits

### 3. **Docker Best Practices**
- Using specific tags (not latest)
- Minimizing layers
- .dockerignore usage
- Running as non-root user
- COPY vs ADD
- Leveraging build cache
- Resource limits
- Health checks

### 4. **Production Readiness**
- Environment configuration
- Logging strategies
- Monitoring and health checks
- Security hardening
- Backup automation

---

## 🛠️ Today's Project

### Project: Production-Ready Blog Microservice
**Location:** `DAY_04/projects/blog-microservice/`

**Tech Stack:**
- Python Flask (API)
- PostgreSQL (Database)
- Nginx (Reverse Proxy)
- Docker Compose

**Features:**
- ✅ Multi-stage Dockerfile
- ✅ Named volumes for persistence
- ✅ Health checks for all services
- ✅ Non-root user containers
- ✅ Resource limits
- ✅ Automated backups
- ✅ Production logging
- ✅ Network isolation

---

## 📊 Quick Start

### Morning Session (6:00 - 9:00 AM)
```bash
# 1. Volume Practice
docker volume create my-data
docker volume ls
docker volume inspect my-data

# 2. Multi-Stage Build Example
cd DAY_04/projects/examples/multi-stage
docker build -t myapp:single-stage -f Dockerfile.single .
docker build -t myapp:multi-stage -f Dockerfile.multi .
docker images | grep myapp  # Compare sizes

# 3. Best Practices
cat .dockerignore
cat Dockerfile  # Review annotations
```

### Afternoon Session (12:00 - 3:00 PM)
```bash
# Build the main project
cd DAY_04/projects/blog-microservice
cp .env.example .env

# Build and run
docker compose up -d --build

# Check services
docker compose ps
docker compose logs -f

# Test API
curl http://localhost/api/health
curl http://localhost/api/posts
```

### Evening Session (7:00 - 9:00 PM)
```bash
# Docker Hub
docker login
docker tag blog-api:latest your-username/blog-api:v1.0.0
docker push your-username/blog-api:v1.0.0

# Backup & Restore
chmod +x scripts/*.sh
./scripts/backup-db.sh
./scripts/restore-db.sh backups/backup_20260219.sql.gz
```

---

## 📁 Project Structure

```
DAY_04/
├── README.md (this file)
├── docs/
│   └── DAY_4_PLAN.md              # Detailed action plan
├── notes/
│   └── day-04-notes.md            # Learning notes
└── projects/
    ├── blog-microservice/          # Main project
    │   ├── backend/
    │   │   ├── app/
    │   │   ├── tests/
    │   │   ├── Dockerfile          # Multi-stage build
    │   │   └── requirements.txt
    │   ├── database/
    │   │   ├── migrations/
    │   │   └── backups/
    │   ├── nginx/
    │   │   └── nginx.conf
    │   ├── scripts/
    │   │   ├── backup-db.sh
    │   │   └── restore-db.sh
    │   ├── docker-compose.yml
    │   ├── .env.example
    │   └── README.md
    └── examples/
        ├── volumes/                # Volume examples
        ├── multi-stage/            # Multi-stage examples
        └── best-practices/         # Best practices demos
```

---

## 🎓 Key Learnings

### Volume Types Comparison

| Type | Use Case | Persistence | Performance | Portability |
|------|----------|-------------|-------------|-------------|
| **Named Volume** | Database data | Yes | Best | Excellent |
| **Bind Mount** | Development code | Yes | Good | Host-dependent |
| **tmpfs** | Temporary data | No | Fastest | N/A |

### Multi-Stage Build Benefits

**Before (Single Stage):**
```dockerfile
FROM python:3.11
RUN apt-get install -y build-essential gcc
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
# Result: 1.2 GB image
```

**After (Multi-Stage):**
```dockerfile
FROM python:3.11-slim AS builder
RUN pip wheel --wheel-dir /wheels -r requirements.txt

FROM python:3.11-alpine
COPY --from=builder /wheels /wheels
RUN pip install /wheels/* && rm -rf /wheels
COPY . .
CMD ["python", "app.py"]
# Result: 250 MB image (80% reduction!)
```

### Best Practices Checklist

- [ ] Use specific image tags
- [ ] Minimize layers
- [ ] Add .dockerignore
- [ ] Run as non-root user
- [ ] Use COPY instead of ADD
- [ ] Leverage build cache
- [ ] Add health checks
- [ ] Set resource limits
- [ ] Configure logging
- [ ] Use multi-stage builds
- [ ] Scan for vulnerabilities

---

## 🐛 Common Issues & Solutions

### Issue 1: Volume Permission Denied
**Solution:** 
```dockerfile
# Create user with specific UID
RUN addgroup -g 1001 appuser && \
    adduser -u 1001 -S appuser -G appuser
COPY --chown=appuser:appuser . .
USER appuser
```

### Issue 2: Large Image Size
**Solution:** Use multi-stage builds and Alpine base images

### Issue 3: Data Loss on `docker compose down`
**Solution:** Use named volumes (preserved unless `-v` flag used)

---

## 📚 Resources

### Documentation
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [Multi-Stage Builds](https://docs.docker.com/build/building/multi-stage/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Security](https://docs.docker.com/engine/security/)

### Videos
- [Docker Volumes Tutorial](https://www.youtube.com/watch?v=p2PH_YPCsis)
- [Multi-Stage Builds Explained](https://www.youtube.com/watch?v=zpkqNPwEzac)
- [Docker Best Practices](https://www.youtube.com/watch?v=8vXoMqWgbQQ)

---

## ✅ Today's Deliverables

By end of Day 4:
1. ✅ Blog Microservice with multi-stage builds
2. ✅ Volume backup/restore scripts
3. ✅ Docker Hub account with 1+ image
4. ✅ Production-ready docker-compose.yml
5. ✅ Comprehensive documentation
6. ✅ GitHub repository update

---

## 🎯 Success Metrics

### Knowledge
- Explain 3 types of Docker mounts
- Write multi-stage Dockerfile from scratch
- List 10 Docker best practices
- Describe volume backup strategies

### Practical
- Reduce image size by 50%+
- Create production-ready compose file
- Push image to Docker Hub
- Implement automated backups

---

## 🚀 Tomorrow (Day 5)

**Focus:** Docker Networking & Security
- Custom bridge networks
- Network drivers
- Container security
- Docker secrets
- Security scanning

---

## 💪 Progress Tracker

**Overall Roadmap:**
```
████████░░░░░░░░░░░░░░░░ 20% Complete
```

**Days Completed:** 4 / 30  
**Projects Built:** 3  
**Skills Acquired:** 25+

---

**Let's build production-ready Docker skills! 🚀**

*Remember: Today's learning will separate you from 90% of junior DevOps engineers. Production skills = Higher salary! 💰*
