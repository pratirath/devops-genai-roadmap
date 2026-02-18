# Day 4 Notes - Advanced Docker

**Date:** February 19, 2026  
**Topics:** Volumes, Multi-Stage Builds, Production Best Practices

---

## 📝 Key Concepts

### Docker Volumes

**What are volumes?**
- Persistent data storage mechanism
- Separate from container filesystem
- Managed by Docker
- Survive container deletion

**Why use volumes?**
- Data persistence
- Share data between containers
- Backup and restore
- Better performance than bind mounts

**Types of Mounts:**
1. **Volumes** (recommended for production)
2. **Bind Mounts** (good for development)
3. **tmpfs Mounts** (temporary data)

---

## 💻 Commands Learned

### Volume Management
```bash
# Create named volume
docker volume create volume_name

# List all volumes
docker volume ls

# Inspect volume
docker volume inspect volume_name

# Remove volume
docker volume rm volume_name

# Remove unused volumes
docker volume prune

# Use volume in container
docker run -v volume_name:/path/in/container image_name

# Bind mount
docker run -v /host/path:/container/path image_name

# Read-only mount
docker run -v volume_name:/path:ro image_name
```

### Image Optimization
```bash
# Build with specific tag
docker build -t image_name:tag .

# Check image size
docker images

# Remove dangling images
docker image prune

# View image layers
docker history image_name
```

### Docker Hub
```bash
# Login
docker login

# Tag image
docker tag local_image:tag username/repo:tag

# Push to Docker Hub
docker push username/repo:tag

# Pull from Docker Hub
docker pull username/repo:tag
```

---

## 🏗️ Multi-Stage Build Template

```dockerfile
# Stage 1: Build/Dependencies
FROM base-image AS builder
WORKDIR /app
# Install build dependencies
# Build application
# Create artifacts

# Stage 2: Runtime
FROM smaller-base-image
WORKDIR /app
# Copy only necessary files from builder
COPY --from=builder /app/artifact .
# Configure runtime
CMD ["run-command"]
```

---

## ✅ Best Practices Checklist

### Dockerfile
- [ ] Use specific tags (not `latest`)
- [ ] Minimize number of layers
- [ ] Use `.dockerignore`
- [ ] Run as non-root user
- [ ] Use `COPY` instead of `ADD`
- [ ] Order instructions for cache optimization
- [ ] Use multi-stage builds
- [ ] Add `HEALTHCHECK`
- [ ] Set proper `WORKDIR`
- [ ] Clean up in same layer

### Docker Compose
- [ ] Use version control
- [ ] Define networks explicitly
- [ ] Use named volumes
- [ ] Add health checks
- [ ] Set resource limits
- [ ] Configure logging
- [ ] Use `.env` files
- [ ] Add `depends_on` with conditions
- [ ] Set restart policies

### Security
- [ ] Scan images for vulnerabilities
- [ ] Use official base images
- [ ] Keep images updated
- [ ] Don't store secrets in images
- [ ] Run as non-root
- [ ] Limit container capabilities
- [ ] Use read-only filesystems where possible

---

## 🎯 Project Notes

### Blog Microservice
**What I built:**
-

**Challenges faced:**
-

**Solutions implemented:**
-

**What I learned:**
-

---

## 📊 Image Size Comparison

| Build Type | Size | Reduction |
|------------|------|-----------|
| Single-stage | MB | - |
| Multi-stage | MB | % |

---

## 🐛 Errors & Solutions

### Error 1:
**Issue:**
**Solution:**
**Learning:**

### Error 2:
**Issue:**
**Solution:**
**Learning:**

---

## 💡 Key Takeaways

1. **Volumes are essential for:**
   -
   -

2. **Multi-stage builds help with:**
   -
   -

3. **Production-ready means:**
   -
   -

4. **Always remember to:**
   -
   -

---

## 🔗 Useful Resources

- Docker Volumes Docs:
- Multi-Stage Builds:
- Best Practices:
- Docker Hub:

---

## ✨ Tomorrow's Focus

Day 5 will cover:
- Docker networking
- Custom networks
- Network drivers
- Container security
- Docker secrets

---

## 📈 Self-Assessment

Rate your understanding (1-5):
- Docker Volumes: /5
- Multi-Stage Builds: /5
- Best Practices: /5
- Production Readiness: /5

**Overall Day 4 Rating:** /5

---

*Notes completed: [Date/Time]*
