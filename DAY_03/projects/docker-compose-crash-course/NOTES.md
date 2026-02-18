# 📝 Docker Compose Mini Project - Complete Guide

**Project:** Node.js + MongoDB + Mongo Express  
**Date:** February 18, 2026  
**Day:** 3  
**Status:** ✅ Working

---

## 🎯 Project Overview

### What This Project Does:
A complete full-stack application demonstrating Docker Compose orchestration with:
- **Frontend/Backend:** Node.js application
- **Database:** MongoDB
- **Admin UI:** Mongo Express (web-based MongoDB admin interface)

### Architecture:

```
┌─────────────────┐
│  User Browser   │
└────────┬────────┘
         │
         ├─────→ http://localhost:3000  (Node.js App)
         │
         └─────→ http://localhost:8081  (Mongo Express)
                        ↓
                  ┌──────────────┐
                  │   MongoDB    │
                  │  Port: 27017 │
                  └──────────────┘
```

---

## 📁 Project Structure

```
docker-compose-crash-course/
├── docker-compose.yaml     # Main orchestration file
├── Dockerfile              # Node.js app image definition
├── .env                    # Environment variables
├── app/                    # Node.js application code
│   ├── server.js
│   └── index.html
├── README.md               # Original instructions
├── docker_commands.md      # Docker commands reference
└── NOTES.md               # This file - Complete guide
```

---

## 🚀 How to Run This Project

### Prerequisites:
```bash
# 1. Ensure Docker Desktop is running
docker --version
docker compose version

# 2. Navigate to project directory
cd ~/Prathiksa/Python_Practice/24Nov/Devops_Roadmap/DAY_03/projects/docker-compose-crash-course
```

### Quick Start (Recommended):

```bash
# Start all services
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f

# Wait 10-15 seconds for all services to be ready
```

### Access the Application:

1. **Mongo Express (Admin UI):**
   - URL: http://localhost:8081
   - Username: admin
   - Password: password

2. **Create Database:**
   - Click "Create Database"
   - Name: `my-db`
   - Create

3. **Create Collection:**
   - Inside `my-db`, create collection: `my-collection`

4. **Add Document:**
   ```json
   {
     "myid": 1,
     "data": "some dynamic data loaded from db"
   }
   ```

5. **Access Node.js App:**
   - URL: http://localhost:3000
   - Should display data from MongoDB

### Stop the Application:

```bash
# Stop all services
docker compose down

# Stop and remove volumes (fresh start)
docker compose down -v
```

---

## 📋 Services Breakdown

### 1. MongoDB Service

```yaml
mongodb:
  image: mongo
  ports:
    - 27017:27017
  environment:
    - MONGO_INITDB_ROOT_USERNAME=${MONGO_ADMIN_USER}
    - MONGO_INITDB_ROOT_PASSWORD=${MONGO_ADMIN_PASS}
```

**Purpose:** Database server  
**Image:** Official MongoDB from Docker Hub  
**Port:** 27017 (MongoDB default)  
**Environment Variables:**
- `MONGO_INITDB_ROOT_USERNAME`: Admin username (from .env)
- `MONGO_INITDB_ROOT_PASSWORD`: Admin password (from .env)

---

### 2. Mongo Express Service

```yaml
mongo-express:
  image: mongo-express
  restart: always
  ports:
    - 8081:8081
  environment:
    - ME_CONFIG_MONGODB_ADMINUSERNAME=${MONGO_ADMIN_USER}
    - ME_CONFIG_MONGODB_ADMINPASSWORD=${MONGO_ADMIN_PASS}
    - ME_CONFIG_MONGODB_SERVER=mongodb
    - ME_CONFIG_BASICAUTH_USERNAME=${MONGO_ADMIN_USER}
    - ME_CONFIG_BASICAUTH_PASSWORD=${MONGO_ADMIN_PASS}
  depends_on:
    - mongodb
```

**Purpose:** Web-based MongoDB admin interface  
**Image:** Official Mongo Express  
**Port:** 8081  
**Restart Policy:** Always (auto-restart if crashes)  
**Dependencies:** Waits for MongoDB to start  
**Environment Variables:**
- `ME_CONFIG_MONGODB_SERVER`: Points to 'mongodb' service (container name)
- Admin credentials for MongoDB connection
- Basic auth for web interface

---

### 3. Node.js Application Service

```yaml
my-app:
  build: .
  ports:
    - 3000:3000
  environment:
    - MONGO_DB_USERNAME=${MONGO_ADMIN_USER}
    - MONGO_DB_PWD=${MONGO_ADMIN_PASS}
```

**Purpose:** Web application frontend/backend  
**Build:** Uses local Dockerfile  
**Port:** 3000  
**Environment Variables:**
- Credentials to connect to MongoDB

---

## 🔧 Environment Variables (.env)

```properties
MONGO_ADMIN_USER=admin
MONGO_ADMIN_PASS=password
```

**Purpose:**
- Centralized configuration
- Easy to change credentials
- Keeps secrets out of docker-compose.yaml
- Same values used across all services

**Security Note:** 
- ⚠️ Never commit real passwords to Git
- Use strong passwords in production
- Consider using Docker secrets for sensitive data

---

## 📝 Docker Compose Commands Used

### Basic Operations:

```bash
# Start services in background
docker compose up -d

# Start with rebuild
docker compose up -d --build

# View running services
docker compose ps

# View logs (all services)
docker compose logs

# View logs (specific service)
docker compose logs mongodb
docker compose logs -f my-app  # Follow logs

# Stop services
docker compose stop

# Stop and remove containers
docker compose down

# Stop, remove containers and volumes
docker compose down -v

# Restart a service
docker compose restart mongodb

# Execute command in service
docker compose exec mongodb mongosh
docker compose exec my-app sh
```

### Debugging Commands:

```bash
# Check service status
docker compose ps

# Inspect service
docker compose exec mongodb env

# View container details
docker inspect docker-compose-crash-course-mongodb-1

# Check networks
docker network ls
docker network inspect docker-compose-crash-course_default
```

---

## ⚠️ Common Issues & Solutions

### Issue 1: Port Already in Use

**Error:**
```
Error: bind: address already in use
Error: failed to create service: ports are not available: listen tcp 0.0.0.0:27017
```

**Cause:** Port 27017, 8081, or 3000 already occupied

**Solution:**
```bash
# Check what's using the port
lsof -i :27017
lsof -i :8081
lsof -i :3000

# Kill the process
kill -9 <PID>

# Or change ports in docker-compose.yaml
ports:
  - "27018:27017"  # Use different host port
```

---

### Issue 2: MongoDB Connection Failed

**Error:**
```
MongoServerError: Authentication failed
```

**Cause:** Incorrect credentials or MongoDB not ready

**Solution 1 - Check Environment Variables:**
```bash
# Verify .env file exists and has correct values
cat .env

# Check if variables are loaded
docker compose config
```

**Solution 2 - Wait for MongoDB:**
```bash
# MongoDB takes 5-10 seconds to start
docker compose logs mongodb

# Look for: "Waiting for connections"
```

**Solution 3 - Add Health Check:**
```yaml
mongodb:
  healthcheck:
    test: echo 'db.runCommand("ping").ok' | mongosh localhost:27017/test --quiet
    interval: 10s
    timeout: 5s
    retries: 5
```

---

### Issue 3: Mongo Express Not Loading

**Error:**
```
Cannot connect to MongoDB
```

**Cause:** MongoDB not ready or wrong server name

**Solution 1 - Check Service Name:**
```yaml
# Ensure ME_CONFIG_MONGODB_SERVER matches mongodb service name
environment:
  - ME_CONFIG_MONGODB_SERVER=mongodb  # Must match service name
```

**Solution 2 - Check Dependencies:**
```yaml
mongo-express:
  depends_on:
    - mongodb  # Ensures MongoDB starts first
```

**Solution 3 - Check Logs:**
```bash
docker compose logs mongo-express
```

---

### Issue 4: Node.js App Can't Connect to MongoDB

**Error:**
```
MongoNetworkError: failed to connect to server
```

**Cause:** Wrong connection string or MongoDB not ready

**Solution 1 - Use Correct Host:**
```javascript
// In Node.js app, use service name
const mongoUrl = 'mongodb://admin:password@mongodb:27017';
// NOT localhost, use 'mongodb' (service name)
```

**Solution 2 - Check Environment Variables:**
```bash
# Verify app receives correct credentials
docker compose exec my-app env | grep MONGO
```

**Solution 3 - Add Retry Logic:**
```javascript
const connectWithRetry = () => {
  mongoose.connect(mongoUrl, {
    useNewUrlParser: true,
    useUnifiedTopology: true
  })
  .then(() => console.log('MongoDB Connected'))
  .catch(err => {
    console.log('MongoDB connection failed, retrying in 5 seconds...');
    setTimeout(connectWithRetry, 5000);
  });
};
```

---

### Issue 5: Data Not Persisting

**Problem:** Data lost when containers restart

**Cause:** No volume defined for MongoDB

**Solution - Add Named Volume:**
```yaml
services:
  mongodb:
    image: mongo
    volumes:
      - mongo_data:/data/db  # Persist data

volumes:
  mongo_data:  # Named volume definition
```

**Verify:**
```bash
# List volumes
docker volume ls

# Inspect volume
docker volume inspect docker-compose-crash-course_mongo_data
```

---

### Issue 6: Services Start in Wrong Order

**Problem:** App tries to connect before MongoDB is ready

**Cause:** `depends_on` only ensures containers start, not that services are ready

**Solution 1 - Add Health Checks:**
```yaml
mongodb:
  healthcheck:
    test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
    interval: 10s
    timeout: 5s
    retries: 5

my-app:
  depends_on:
    mongodb:
      condition: service_healthy  # Wait for health check
```

**Solution 2 - Use Wait Scripts:**
```bash
# In app's entrypoint
#!/bin/sh
while ! nc -z mongodb 27017; do
  echo "Waiting for MongoDB..."
  sleep 1
done
echo "MongoDB is ready!"
node server.js
```

---

### Issue 7: Environment Variables Not Loading

**Problem:** Variables from .env not being used

**Cause:** .env file not in same directory as docker-compose.yaml

**Solution:**
```bash
# Ensure .env is in project root
ls -la .env

# Verify variables are loaded
docker compose config

# Explicitly specify env file
docker compose --env-file .env up
```

---

### Issue 8: Build Cache Issues

**Problem:** Changes not reflected in running app

**Cause:** Docker using cached layers

**Solution:**
```bash
# Rebuild without cache
docker compose build --no-cache

# Or rebuild specific service
docker compose build --no-cache my-app

# Then restart
docker compose up -d
```

---

## 🔒 Limitations & Considerations

### 1. **Security Limitations**

**Issue:** Credentials in plain text
```properties
# .env file
MONGO_ADMIN_USER=admin
MONGO_ADMIN_PASS=password
```

**Improvements:**
- Use Docker secrets (Swarm mode)
- Use environment variable injection at runtime
- Use secret management tools (Vault, AWS Secrets Manager)

---

### 2. **No Data Persistence by Default**

**Issue:** Data lost when containers removed

**Current State:**
```yaml
mongodb:
  image: mongo
  # No volumes defined
```

**Improvement:**
```yaml
mongodb:
  volumes:
    - mongo_data:/data/db

volumes:
  mongo_data:
```

---

### 3. **Network Isolation**

**Limitation:** All services on same network

**Default Behavior:**
```
docker-compose-crash-course_default (bridge network)
└── All 3 services can communicate
```

**Improvement for Production:**
```yaml
networks:
  frontend:  # Public-facing services
  backend:   # Internal services

services:
  my-app:
    networks:
      - frontend
      - backend
  
  mongodb:
    networks:
      - backend  # Not exposed to frontend
```

---

### 4. **No Health Checks**

**Issue:** Services marked as "running" even if not ready

**Solution:**
```yaml
mongodb:
  healthcheck:
    test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
    interval: 10s
    timeout: 5s
    retries: 5
    start_period: 40s
```

---

### 5. **Resource Limits Not Set**

**Issue:** Services can consume unlimited resources

**Solution:**
```yaml
my-app:
  deploy:
    resources:
      limits:
        cpus: '0.5'
        memory: 512M
      reservations:
        cpus: '0.25'
        memory: 256M
```

---

### 6. **No Logging Configuration**

**Issue:** Logs can fill up disk space

**Solution:**
```yaml
my-app:
  logging:
    driver: "json-file"
    options:
      max-size: "10m"
      max-file: "3"
```

---

### 7. **Development vs Production**

**Issue:** Same config for all environments

**Solution - Multiple Compose Files:**
```bash
# Base configuration
docker-compose.yaml

# Development overrides
docker-compose.dev.yaml

# Production overrides
docker-compose.prod.yaml

# Run with override
docker compose -f docker-compose.yaml -f docker-compose.prod.yaml up
```

---

## 🎓 Key Learnings

### 1. **Container Naming**
- Services can reference each other by service name
- `mongodb` service is accessible at `mongodb:27017` from other containers
- No need for IP addresses

### 2. **Environment Variables**
- Defined in `.env` file
- Referenced with `${VARIABLE_NAME}` in compose file
- Same variables shared across services

### 3. **Service Dependencies**
- `depends_on` ensures start order
- Doesn't wait for service to be "ready"
- Use health checks for readiness

### 4. **Networking**
- Docker Compose creates default network
- All services on same network can communicate
- External access via port mapping

### 5. **Volume Management**
- Named volumes for data persistence
- Bind mounts for development
- Volumes survive container recreation

---

## 📊 Performance Tips

### 1. **Use Multi-Stage Builds**
```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
CMD ["node", "server.js"]
```

### 2. **Cache Dependencies**
```dockerfile
# Copy package files first (cached if unchanged)
COPY package*.json ./
RUN npm install

# Then copy source (changes more frequently)
COPY . .
```

### 3. **Use Alpine Images**
```yaml
mongodb:
  image: mongo:7-alpine  # Smaller image size
```

---

## 🧪 Testing the Setup

### Test 1: Service Health
```bash
# Check all services running
docker compose ps

# Should show all services as "Up"
```

### Test 2: MongoDB Connection
```bash
# Connect to MongoDB shell
docker compose exec mongodb mongosh -u admin -p password

# Run test query
db.adminCommand({ ping: 1 })
```

### Test 3: Network Communication
```bash
# From app container, ping MongoDB
docker compose exec my-app ping mongodb

# Should resolve and respond
```

### Test 4: Data Persistence
```bash
# Create data in Mongo Express
# Stop containers
docker compose down

# Start again
docker compose up -d

# Check if data still exists
```

---

## 🔄 Workflow for Development

### Daily Workflow:
```bash
# Morning - Start everything
docker compose up -d

# Make code changes
# ... edit files ...

# Rebuild and restart specific service
docker compose build my-app
docker compose restart my-app

# View logs
docker compose logs -f my-app

# Evening - Stop everything
docker compose down
```

### Fresh Start:
```bash
# Remove everything (including volumes)
docker compose down -v

# Rebuild from scratch
docker compose up -d --build

# Recreate database and collection
```

---

## 📚 Additional Resources

### Docker Compose Documentation:
- [Official Docs](https://docs.docker.com/compose/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)
- [Environment Variables](https://docs.docker.com/compose/environment-variables/)

### MongoDB Resources:
- [MongoDB Docker Image](https://hub.docker.com/_/mongo)
- [Mongo Express](https://github.com/mongo-express/mongo-express)

### Best Practices:
- [Docker Security](https://docs.docker.com/engine/security/)
- [Production-Ready Compose](https://docs.docker.com/compose/production/)

---

## ✅ Success Checklist

After completing this project, you should be able to:

- [ ] Explain what Docker Compose does
- [ ] Write docker-compose.yaml files
- [ ] Use environment variables in Compose
- [ ] Understand service dependencies
- [ ] Debug multi-container applications
- [ ] Access containers via service names
- [ ] Manage volumes for persistence
- [ ] Handle common Docker Compose issues
- [ ] Implement health checks
- [ ] Configure networking between services

---

## 🎯 Next Steps

### Improvements to Make:
1. Add health checks to all services
2. Implement data persistence with volumes
3. Add resource limits
4. Configure logging
5. Create separate dev/prod compose files
6. Add backup strategy for MongoDB
7. Implement monitoring (Prometheus)
8. Add CI/CD integration

### Advanced Topics:
- Docker Swarm for orchestration
- Kubernetes migration path
- Service mesh integration
- Automated testing in containers
- Blue-green deployments

---

## 📝 Personal Notes

**Date Completed:** February 18, 2026  
**Time Spent:** _____ hours  
**Challenges Faced:**
- 

**Solutions Found:**
- 

**Key Takeaway:**
- 

**What I'll Do Differently:**
- 

---

**Status:** ✅ Project Complete & Documented  
**Next:** Move to Day 4 or build more complex projects
