# 📅 Day 4 Action Plan - Advanced Docker & Volume Management

**Date:** February 19, 2026  
**Focus:** Docker Volumes, Data Persistence, Multi-Stage Builds & Best Practices  
**Goal:** Master data management in containers and optimize Docker images

---

## ✅ Previous Days' Achievements

**Day 1-2:** Docker Fundamentals ✅
- Mastered 50+ Docker commands
- Built custom Dockerfiles
- Created containerized applications

**Day 3:** Docker Compose & Multi-Container Apps ✅
- Completed 2 full-stack projects
- Mastered docker-compose orchestration
- Implemented health checks and networking
- **Projects:** docker-compose-crash-course, fullstack-app

**You're crushing it! 🔥 Keep the momentum!**

---

## 🎯 Today's Learning Objectives

By end of Day 4, you will:
- ✅ Master Docker volumes and data persistence
- ✅ Understand bind mounts vs named volumes
- ✅ Learn multi-stage Docker builds
- ✅ Optimize Docker images for production
- ✅ Implement Docker best practices
- ✅ Build a production-ready containerized application
- ✅ Push images to Docker Hub

---

## 🎯 Today's Schedule

### **Morning Session (6:00 - 9:00 AM) - 3 hours**

#### 6:00 - 7:00 AM: Docker Volumes Deep Dive (60 min)

**Learn:**
- What are Docker volumes?
- Why do we need data persistence?
- Types of mounts: volumes, bind mounts, tmpfs

**Watch:**
- [Docker Volumes Explained](https://www.youtube.com/watch?v=p2PH_YPCsis) - 20 min
- [Docker Data Persistence Tutorial](https://www.youtube.com/watch?v=VOK06Q4QqvE) - 30 min

**Practice Commands:**
```bash
# Create a named volume
docker volume create my-data

# List volumes
docker volume ls

# Inspect volume
docker volume inspect my-data

# Run container with volume
docker run -d --name db-container \
  -v my-data:/var/lib/postgresql/data \
  postgres:15-alpine

# Check volume location
docker volume inspect my-data | grep Mountpoint

# Bind mount (host directory)
docker run -d -v $(pwd)/data:/app/data nginx

# Read-only volume
docker run -d -v my-data:/data:ro nginx

# Remove unused volumes
docker volume prune
```

**Key Concepts to Understand:**
- Volume lifecycle
- Data persistence after container removal
- Volume drivers
- Backup and restore strategies

---

#### 7:00 - 8:00 AM: Multi-Stage Docker Builds (60 min)

**Why Multi-Stage Builds?**
- Smaller final images
- Better security (no build tools in production)
- Faster deployments
- Reduced attack surface

**Watch:**
- [Multi-Stage Docker Builds](https://www.youtube.com/watch?v=zpkqNPwEzac) - 15 min

**Practice - Create Multi-Stage Dockerfile:**

**Example 1: Node.js App**
```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

**Example 2: Python App**
```dockerfile
# Stage 1: Dependencies
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

**Compare Image Sizes:**
```bash
# Build both versions
docker build -t myapp:single-stage -f Dockerfile.single .
docker build -t myapp:multi-stage -f Dockerfile.multi .

# Compare sizes
docker images | grep myapp
```

---

#### 8:00 - 9:00 AM: Docker Best Practices (60 min)

**Learn Production Best Practices:**

**1. Use Specific Tags (Not latest)**
```dockerfile
# ❌ Bad
FROM node:latest

# ✅ Good
FROM node:18.19.0-alpine3.19
```

**2. Minimize Layers**
```dockerfile
# ❌ Bad
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y vim

# ✅ Good
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*
```

**3. Use .dockerignore**
Create `.dockerignore`:
```
node_modules
npm-debug.log
.git
.gitignore
README.md
.env
.DS_Store
__pycache__
*.pyc
.pytest_cache
.coverage
```

**4. Don't Run as Root**
```dockerfile
# Create non-root user
RUN addgroup -g 1001 -S appuser && \
    adduser -u 1001 -S appuser -G appuser

USER appuser
```

**5. Use COPY Instead of ADD**
```dockerfile
# ✅ Use COPY for local files
COPY app.py /app/

# Only use ADD for URLs or tar extraction
ADD https://example.com/file.tar.gz /tmp/
```

**6. Leverage Build Cache**
```dockerfile
# ✅ Copy dependency files first
COPY package.json package-lock.json ./
RUN npm ci

# Then copy source code
COPY . .
```

**Watch:**
- [Docker Best Practices](https://www.youtube.com/watch?v=8vXoMqWgbQQ) - 25 min

---

### **Afternoon Session (12:00 - 3:00 PM) - 3 hours**

#### 12:00 - 3:00 PM: Project - Production-Ready Microservice

**Build:** Blog API with PostgreSQL (Production-Ready)

**Project Structure:**
```bash
mkdir -p ~/DevOps-Roadmap/DAY_04/projects/blog-microservice
cd ~/DevOps-Roadmap/DAY_04/projects/blog-microservice

mkdir -p backend/{app,tests}
mkdir -p database/{migrations,backups}
mkdir -p nginx
touch docker-compose.yml .dockerignore README.md
```

**Features to Implement:**
1. ✅ Multi-stage Dockerfile for backend
2. ✅ Named volumes for database persistence
3. ✅ Nginx reverse proxy
4. ✅ Health checks for all services
5. ✅ Environment variable management
6. ✅ Database migrations
7. ✅ Backup/restore scripts
8. ✅ Non-root user in containers
9. ✅ Resource limits
10. ✅ Production-ready logging

**Backend API Endpoints:**
- `GET /api/health` - Health check
- `GET /api/posts` - List all posts
- `POST /api/posts` - Create post
- `GET /api/posts/:id` - Get specific post
- `PUT /api/posts/:id` - Update post
- `DELETE /api/posts/:id` - Delete post

**Create `backend/Dockerfile`:**
```dockerfile
# Stage 1: Build and install dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-alpine

WORKDIR /app

# Install runtime dependencies
RUN apk add --no-cache libpq

# Create non-root user
RUN addgroup -g 1001 -S appuser && \
    adduser -u 1001 -S appuser -G appuser

# Copy wheels from builder
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

# Install from wheels
RUN pip install --no-cache-dir /wheels/* && \
    rm -rf /wheels

# Copy application code
COPY --chown=appuser:appuser app/ ./app/

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000/api/health')" || exit 1

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app.main:app"]
```

**Create `docker-compose.yml`:**
```yaml
services:
  # PostgreSQL Database
  db:
    image: postgres:15-alpine
    container_name: blog-db
    environment:
      POSTGRES_DB: ${DB_NAME:-blogdb}
      POSTGRES_USER: ${DB_USER:-bloguser}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-changeme}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/migrations:/docker-entrypoint-initdb.d:ro
      - ./database/backups:/backups
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER:-bloguser}"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: blog-api
    environment:
      DB_HOST: db
      DB_NAME: ${DB_NAME:-blogdb}
      DB_USER: ${DB_USER:-bloguser}
      DB_PASSWORD: ${DB_PASSWORD:-changeme}
      API_PORT: 8000
      LOG_LEVEL: ${LOG_LEVEL:-INFO}
    depends_on:
      db:
        condition: service_healthy
    networks:
      - backend
      - frontend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    restart: unless-stopped

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: blog-nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - backend
    networks:
      - frontend
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
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    restart: unless-stopped

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge

volumes:
  postgres_data:
    driver: local
```

**Create `.env.example`:**
```bash
# Database Configuration
DB_NAME=blogdb
DB_USER=bloguser
DB_PASSWORD=super_secret_password_change_in_production

# API Configuration
API_PORT=8000
LOG_LEVEL=INFO

# Environment
ENV=production
```

---

### **Evening Session (7:00 - 9:00 PM) - 2 hours**

#### 7:00 - 8:00 PM: Docker Hub & Image Management

**Create Docker Hub Account:**
1. Go to hub.docker.com
2. Sign up / Sign in
3. Create repository: `your-username/blog-api`

**Tag and Push Images:**
```bash
# Build with tag
docker build -t your-username/blog-api:v1.0.0 ./backend
docker build -t your-username/blog-api:latest ./backend

# Login to Docker Hub
docker login

# Push to Docker Hub
docker push your-username/blog-api:v1.0.0
docker push your-username/blog-api:latest

# View your images
docker images

# Remove local image
docker rmi your-username/blog-api:v1.0.0

# Pull from Docker Hub
docker pull your-username/blog-api:v1.0.0
```

**Update docker-compose.yml to use Docker Hub image:**
```yaml
backend:
  image: your-username/blog-api:v1.0.0
  # Remove build section when using pre-built image
```

---

#### 8:00 - 9:00 PM: Volume Backup & Restore

**Learn Backup Strategies:**

**1. Database Backup Script:**
Create `scripts/backup-db.sh`:
```bash
#!/bin/bash
# Database Backup Script

BACKUP_DIR="./database/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${TIMESTAMP}.sql"

echo "Creating backup: ${BACKUP_FILE}"

docker exec blog-db pg_dump -U bloguser blogdb > "${BACKUP_DIR}/${BACKUP_FILE}"

# Compress backup
gzip "${BACKUP_DIR}/${BACKUP_FILE}"

echo "Backup completed: ${BACKUP_FILE}.gz"

# Keep only last 7 backups
cd "${BACKUP_DIR}"
ls -t *.gz | tail -n +8 | xargs -r rm

echo "Cleaned old backups. Keeping last 7."
```

**2. Database Restore Script:**
Create `scripts/restore-db.sh`:
```bash
#!/bin/bash
# Database Restore Script

if [ -z "$1" ]; then
  echo "Usage: ./restore-db.sh <backup-file.sql.gz>"
  exit 1
fi

BACKUP_FILE=$1

echo "Restoring from: ${BACKUP_FILE}"

# Decompress and restore
gunzip -c "${BACKUP_FILE}" | docker exec -i blog-db psql -U bloguser -d blogdb

echo "Restore completed!"
```

**3. Volume Backup:**
```bash
# Backup entire volume
docker run --rm \
  -v blog_postgres_data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/volume_backup_$(date +%Y%m%d).tar.gz -C /data .

# Restore volume
docker run --rm \
  -v blog_postgres_data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar xzf /backup/volume_backup_20260219.tar.gz -C /data
```

**Make scripts executable:**
```bash
chmod +x scripts/*.sh
```

---

## 🎯 Mini-Challenges (Choose 2)

### Challenge 1: Image Optimization Race
- Build the same app with single-stage and multi-stage
- Compare sizes
- Document your findings
- Goal: Reduce image size by >50%

### Challenge 2: Volume Lab
- Create 3 different volume types
- Test data persistence
- Backup and restore
- Document the process

### Challenge 3: Docker Hub Portfolio
- Push 3 different images to Docker Hub
- Add detailed README for each
- Include usage examples
- Make them public for portfolio

---

## 📝 Today's Deliverables

**By end of Day 4, you must have:**

1. ✅ **Blog Microservice Project**
   - Multi-stage Dockerfile
   - Production-ready docker-compose.yml
   - Volume persistence
   - Backup/restore scripts
   - Documentation

2. ✅ **Docker Hub Account**
   - At least 1 image pushed
   - Repository with README
   - Proper tagging

3. ✅ **Notes Document**
   - Volumes concepts
   - Multi-stage builds
   - Best practices checklist
   - Backup strategies

4. ✅ **GitHub Update**
   - Push DAY_04 projects
   - Update main README
   - Add project documentation

---

## 📚 Resources for Today

### Videos:
- [Docker Volumes Tutorial](https://www.youtube.com/watch?v=p2PH_YPCsis)
- [Multi-Stage Builds](https://www.youtube.com/watch?v=zpkqNPwEzac)
- [Docker Best Practices](https://www.youtube.com/watch?v=8vXoMqWgbQQ)

### Documentation:
- [Docker Volumes Docs](https://docs.docker.com/storage/volumes/)
- [Multi-Stage Builds Docs](https://docs.docker.com/build/building/multi-stage/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

### Articles:
- [Docker Image Optimization](https://docs.docker.com/develop/dev-best-practices/)
- [Production Docker Setup](https://dockerlabs.collabnix.com/)

---

## ✅ End of Day Checklist

- [ ] Completed Docker volumes tutorial
- [ ] Practiced volume commands
- [ ] Built multi-stage Dockerfile
- [ ] Compared image sizes
- [ ] Created production-ready project
- [ ] Implemented health checks
- [ ] Set up backup scripts
- [ ] Created Docker Hub account
- [ ] Pushed image to Docker Hub
- [ ] Tested backup and restore
- [ ] Updated GitHub repository
- [ ] Documented learnings in notes
- [ ] Updated main README progress

---

## 🎯 Success Metrics

**Knowledge:**
- [ ] Can explain 3 types of mounts
- [ ] Can write multi-stage Dockerfile
- [ ] Understand Docker best practices
- [ ] Know how to backup volumes

**Practical:**
- [ ] Reduced image size by 50%+
- [ ] Created production-ready compose file
- [ ] Pushed image to Docker Hub
- [ ] Implemented working backups

---

## 🚀 Tomorrow's Preview (Day 5)

**Focus:** Docker Networking Deep Dive & Security
- Custom bridge networks
- Network drivers (bridge, host, overlay)
- Container security scanning
- Docker secrets management
- Security best practices
- Build secure microservices

**Get excited!** 🔥

---

## 💪 Motivational Reminder

**Day 4 Progress:**
```
████████░░░░░░░░░░░░░░░░ 20% Complete
```

You're building real DevOps skills! 

**What you've learned so far:**
- ✅ Docker fundamentals
- ✅ Custom Dockerfiles
- ✅ Docker Compose orchestration
- ✅ Multi-container applications
- ✅ Data persistence (today!)
- ✅ Production best practices (today!)

**You're not just learning - you're building a portfolio! 🎯**

---

## 📞 Need Help?

**Stuck on something?**
- Check Docker docs: docs.docker.com
- Search Stack Overflow
- Ask in Docker Community Slack
- Review previous day's notes

**Time Management Tips:**
- Set timer for each session
- Take 10-min breaks
- Stay hydrated
- Don't skip hands-on practice

---

**Ready? Let's make Day 4 amazing! 🚀**

**Start Time:** February 19, 2026, 6:00 AM  
**End Goal:** Production-ready Docker skills

*Remember: Every container you build, every volume you create, every image you optimize - you're getting closer to that 20+ LPA role! Keep pushing! 💪*
