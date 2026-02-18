# Blog Microservice - Production-Ready Docker Project

## 🎯 Project Overview

A production-ready blog API microservice demonstrating advanced Docker concepts:
- Multi-stage Docker builds
- Volume persistence
- Health checks
- Resource limits
- Backup automation
- Network isolation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│          Docker Environment             │
├──────────────┬──────────────┬───────────┤
│   Nginx      │   Flask API  │ PostgreSQL│
│   (Proxy)    │   (Backend)  │   (DB)    │
│   Port: 80   │  Internal    │ Internal  │
└──────────────┴──────────────┴───────────┘
       │              │              │
       └──────────────┴──────────────┘
            app-network (Bridge)
```

---

## 🚀 Quick Start

### Prerequisites
- Docker Desktop installed
- Docker Compose v2+
- Basic understanding of REST APIs

### Setup

1. **Clone and navigate:**
```bash
cd DAY_04/projects/blog-microservice
```

2. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your settings
```

3. **Build and run:**
```bash
docker compose up -d --build
```

4. **Verify services:**
```bash
docker compose ps
docker compose logs -f
```

5. **Test API:**
```bash
# Health check
curl http://localhost/api/health

# Get posts
curl http://localhost/api/posts

# Create post
curl -X POST http://localhost/api/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"My First Post","content":"Hello World!"}'
```

---

## 📡 API Endpoints

### Health
```
GET /api/health
```

### Posts
```
GET    /api/posts           # List all posts
POST   /api/posts           # Create post
GET    /api/posts/:id       # Get specific post
PUT    /api/posts/:id       # Update post
DELETE /api/posts/:id       # Delete post
```

---

## 🔧 Development

### View Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f backend
docker compose logs -f db
docker compose logs -f nginx
```

### Restart Services
```bash
# All
docker compose restart

# Specific
docker compose restart backend
```

### Rebuild
```bash
docker compose down
docker compose up -d --build
```

---

## 💾 Backup & Restore

### Database Backup
```bash
chmod +x scripts/backup-db.sh
./scripts/backup-db.sh
```

Backups stored in: `database/backups/`

### Database Restore
```bash
chmod +x scripts/restore-db.sh
./scripts/restore-db.sh database/backups/backup_YYYYMMDD_HHMMSS.sql.gz
```

### Volume Backup
```bash
# Backup volume to tar.gz
docker run --rm \
  -v blog_postgres_data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/volume_backup_$(date +%Y%m%d).tar.gz -C /data .
```

---

## 📁 Project Structure

```
blog-microservice/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # Flask app
│   │   ├── models.py            # Database models
│   │   └── routes.py            # API routes
│   ├── tests/
│   │   └── test_api.py          # API tests
│   ├── Dockerfile               # Multi-stage build
│   └── requirements.txt         # Python dependencies
├── database/
│   ├── migrations/
│   │   └── init.sql             # Database schema
│   └── backups/                 # Backup directory
├── nginx/
│   └── nginx.conf               # Nginx configuration
├── scripts/
│   ├── backup-db.sh             # Backup script
│   └── restore-db.sh            # Restore script
├── docker-compose.yml           # Main orchestration
├── .env.example                 # Environment template
├── .dockerignore
└── README.md                    # This file
```

---

## 🔒 Security Features

- ✅ Non-root user in containers
- ✅ Read-only volumes where possible
- ✅ Network isolation (frontend/backend networks)
- ✅ Environment-based secrets
- ✅ Resource limits
- ✅ Health checks

---

## 📊 Resource Limits

| Service | CPU Limit | Memory Limit |
|---------|-----------|--------------|
| Nginx | 0.25 | 128 MB |
| Backend | 1.0 | 1 GB |
| Database | 0.5 | 512 MB |

---

## 🐛 Troubleshooting

### Services not starting?
```bash
docker compose ps
docker compose logs
```

### Database connection errors?
```bash
docker compose logs db
docker exec -it blog-db psql -U bloguser -d blogdb
```

### Port conflicts?
```bash
# Check if port 80 is in use
lsof -i :80

# Or change port in docker-compose.yml
ports:
  - "8080:80"
```

---

## 🎓 What You'll Learn

- ✅ Multi-stage Docker builds
- ✅ Volume management and persistence
- ✅ Health check implementation
- ✅ Resource optimization
- ✅ Network isolation
- ✅ Backup automation
- ✅ Production-ready configurations
- ✅ Docker best practices

---

## 🚀 Production Deployment

**Not production-ready yet! Needs:**
- [ ] SSL/TLS certificates
- [ ] Authentication/Authorization
- [ ] Rate limiting
- [ ] Monitoring (Prometheus/Grafana)
- [ ] Centralized logging
- [ ] CI/CD pipeline
- [ ] Kubernetes deployment manifests

---

## 📚 References

- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Multi-Stage Builds](https://docs.docker.com/build/building/multi-stage/)
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

## ✨ Next Steps

1. Add authentication (JWT)
2. Implement caching (Redis)
3. Add monitoring
4. Create CI/CD pipeline
5. Deploy to cloud (AWS/GCP)

---

*Project created as part of Day 4 learning - Advanced Docker Concepts*
