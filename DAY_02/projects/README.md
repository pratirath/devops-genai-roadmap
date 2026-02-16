# 🚀 Day 2 Projects

This folder contains all hands-on projects built on Day 2.

---

## 📁 Projects List

### 1. docker-nginx-demo
**Focus:** Volume mounting and live updates

**What it does:**
- Serves custom HTML using nginx
- Demonstrates volume mounting
- Shows live file updates without container restart

**Key Files:**
- `index.html` - Custom HTML with gradient background

**Commands Used:**
```bash
docker run -d -p 8080:80 \
  -v $(pwd):/usr/share/nginx/html \
  --name my-web nginx
```

**Skills Learned:**
- Volume mounting with `-v` flag
- Port mapping with `-p` flag
- Container naming with `--name`
- Live development workflow

---

### 2. my-first-docker-app
**Focus:** Building custom Docker images

**What it does:**
- Python HTTP server showing current time
- Custom Dockerfile from scratch
- Demonstrates image building and deployment

**Key Files:**
- `app.py` - Python web server
- `Dockerfile` - Container definition

**Dockerfile:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
```

**Commands Used:**
```bash
docker build -t my-python-app:v1 .
docker run -d -p 8080:8080 --name my-app my-python-app:v1
```

**Skills Learned:**
- Dockerfile syntax
- Image building
- Container deployment
- Python app containerization

---

## 📊 Projects Summary

| Project | Type | Duration | Status |
|---------|------|----------|--------|
| **docker-nginx-demo** | Volume mounting | 20 min | ✅ Complete |
| **my-first-docker-app** | Custom Dockerfile | 30 min | ✅ Complete |

---

## 🎓 Skills Practiced

Through these projects, I learned:
- ✅ Volume mounting for development
- ✅ Writing Dockerfiles
- ✅ Building Docker images
- ✅ Running containers with custom configurations
- ✅ Port mapping
- ✅ Container lifecycle management

---

## 🔜 How to Run These Projects

### docker-nginx-demo:
```bash
cd docker-nginx-demo
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html --name demo nginx
open http://localhost:8080
```

### my-first-docker-app:
```bash
cd my-first-docker-app
docker build -t my-app:v1 .
docker run -d -p 8080:8080 --name my-app my-app:v1
open http://localhost:8080
```

---

## 💡 Key Takeaways

1. **Volume Mounting = Fast Development**
   - Edit files locally
   - See changes instantly
   - No container rebuild needed

2. **Dockerfiles = Reproducible Builds**
   - Same result every time
   - Version controlled
   - Team-shareable

3. **Containers = Isolated Environments**
   - No conflicts
   - Clean deployment
   - Easy cleanup

---

## 🌟 Achievement Unlocked!

✅ Built first containerized application  
✅ Created custom Dockerfile from scratch  
✅ Deployed working Python web app  

**Status:** Docker Developer! 🐳

---

## 🔗 Related Resources

- **Day 2 Plan:** [../docs/DAY_2_PLAN.md](../docs/DAY_2_PLAN.md)
- **Day 2 Notes:** [../notes/day-02-notes.md](../notes/day-02-notes.md)
- **Docker Docs:** https://docs.docker.com

---

**These projects represent my first steps into containerization technology! 🚀**
