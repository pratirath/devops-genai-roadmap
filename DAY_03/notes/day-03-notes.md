# 📝 Day 3 Learning Notes

**Date:** February 18, 2026  
**Focus:** Docker Compose & Multi-Container Applications  
**Duration:** 4+ hours

---

## 🎯 Today's Accomplishments

### What I Built:
- ✅ Multi-container application with Docker Compose
- ✅ Node.js + MongoDB + Mongo Express stack
- ✅ Complete orchestration with docker-compose.yaml
- ✅ Environment variable configuration
- ✅ Service dependencies and networking

### Skills Acquired:
- ✅ Writing docker-compose.yaml files
- ✅ Managing multiple services
- ✅ Container networking
- ✅ Environment variable management
- ✅ Service dependencies (depends_on)
- ✅ Debugging multi-container apps
- ✅ Volume management basics

---

## 💡 Key Concepts Learned

### 1. Docker Compose Fundamentals

**What is Docker Compose?**
- Tool for defining and running multi-container Docker applications
- Uses YAML files for configuration
- Single command to start/stop entire stack
- Automatic network creation between services

**Why Use Docker Compose?**
```bash
# Without Compose - Need multiple commands
docker network create app-network
docker run -d --name db --network app-network mongo
docker run -d --name backend --network app-network myapp
docker run -d --name frontend --network app-network nginx

# With Compose - One command
docker compose up -d
```

**Key Advantage:** Infrastructure as Code! 🚀

---

### 2. YAML Syntax

**Basic Structure:**
```yaml
version: '3'

services:           # Define containers
  service-name:
    image: image-name
    ports:
      - "host:container"
    environment:
      - KEY=value
    depends_on:
      - other-service

volumes:            # Optional: Named volumes
  volume-name:

networks:           # Optional: Custom networks
  network-name:
```

**Key Learnings:**
- Indentation matters! (2 spaces, not tabs)
- Use quotes for port mappings: `"8080:80"`
- Environment variables: `${VAR_NAME}` from .env file
- Service names become hostnames in network

---

### 3. Service Communication

**Container-to-Container:**
```yaml
services:
  my-app:
    # Can access MongoDB at 'mongodb:27017'
  
  mongodb:
    # Hostname is 'mongodb' (service name)
```

**Network Discovery:**
- Docker Compose creates default network
- Services reference each other by service name
- No need for IP addresses
- Automatic DNS resolution

**Example in Code:**
```javascript
// In Node.js app
const mongoUrl = 'mongodb://admin:password@mongodb:27017';
//                                          ^^^^^^^^
//                                      Service name!
```

**Aha Moment! 💡**  
Service names ARE the hostnames! No localhost needed for inter-container communication!

---

### 4. Environment Variables

**Three Ways to Define:**

1. **In docker-compose.yaml:**
```yaml
environment:
  - MONGO_USER=admin
  - MONGO_PASS=password
```

2. **From .env file:**
```yaml
# .env file
MONGO_ADMIN_USER=admin
MONGO_ADMIN_PASS=password

# docker-compose.yaml
environment:
  - MONGO_DB_USERNAME=${MONGO_ADMIN_USER}
  - MONGO_DB_PWD=${MONGO_ADMIN_PASS}
```

3. **External env_file:**
```yaml
env_file:
  - ./config/.env
```

**Best Practice:** Use .env for development, secrets management for production

---

### 5. Service Dependencies

**depends_on Keyword:**
```yaml
my-app:
  depends_on:
    - mongodb  # Ensures MongoDB starts first
```

**Important Limitation:**
- Only ensures START order
- Doesn't wait for service to be READY
- MongoDB might not accept connections yet!

**Solution - Health Checks:**
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
      condition: service_healthy  # Wait for health check!
```

---

## 💻 Project: Node.js + MongoDB + Mongo Express

### Architecture:

```
User Browser
    ↓
┌─────────────────────┐
│  Mongo Express UI   │ :8081
│  (Admin Interface)  │
└──────────┬──────────┘
           │
    ┌──────▼──────┐
    │   MongoDB   │ :27017
    │  (Database) │
    └──────▲──────┘
           │
    ┌──────┴──────┐
    │  Node.js    │ :3000
    │  (Web App)  │
    └─────────────┘
```

### Services Breakdown:

**1. MongoDB:**
- Official mongo image
- Port 27017
- Admin credentials from .env
- Stores application data

**2. Mongo Express:**
- Web-based admin UI
- Port 8081
- Connects to MongoDB
- Login: admin/password

**3. Node.js App:**
- Custom built from Dockerfile
- Port 3000
- Reads/writes to MongoDB
- Displays data in browser

---

## 🔧 Commands Mastered

### Basic Operations:
```bash
docker compose up -d           # Start all services in background
docker compose up --build      # Rebuild before starting
docker compose down            # Stop and remove containers
docker compose down -v         # Also remove volumes
```

### Monitoring:
```bash
docker compose ps              # List running services
docker compose logs            # View all logs
docker compose logs -f         # Follow logs (live)
docker compose logs mongodb    # Logs for one service
```

### Debugging:
```bash
docker compose exec mongodb mongosh  # Shell into MongoDB
docker compose exec my-app sh        # Shell into app
docker compose restart my-app        # Restart one service
docker compose config                # Validate YAML syntax
```

### Management:
```bash
docker compose stop            # Stop without removing
docker compose start           # Start stopped containers
docker compose pause           # Pause containers
docker compose unpause         # Resume containers
```

**Total Commands Learned:** 15+ ✅

---

## 💭 Challenges Faced & Solutions

### Challenge 1: MongoDB Not Ready

**Problem:**
```
Node.js app trying to connect while MongoDB still starting
Error: MongoNetworkError: failed to connect
```

**Why It Happened:**
- `depends_on` only ensures START order
- MongoDB takes 5-10 seconds to be ready
- App tries to connect immediately

**Solution 1 - Add Delays in App:**
```javascript
const connectWithRetry = () => {
  mongoose.connect(mongoUrl)
    .then(() => console.log('Connected!'))
    .catch(err => {
      console.log('Retrying in 5s...');
      setTimeout(connectWithRetry, 5000);
    });
};
```

**Solution 2 - Health Checks:**
```yaml
depends_on:
  mongodb:
    condition: service_healthy
```

**Lesson:** Services "running" ≠ Services "ready"

---

### Challenge 2: Port Conflicts

**Problem:**
```
Error: bind: address already in use
Port 27017 is already allocated
```

**Cause:**
- Another MongoDB instance running
- Or previous container not cleaned up

**Solution:**
```bash
# Find what's using the port
lsof -i :27017

# Kill the process
kill -9 <PID>

# Or use different port
ports:
  - "27018:27017"  # Changed host port
```

**Lesson:** Always clean up properly with `docker compose down`

---

### Challenge 3: Environment Variables Not Loading

**Problem:**
Variables undefined in containers

**Cause:**
- .env file not in same directory as docker-compose.yaml
- Typo in variable names
- Wrong syntax

**Solution:**
```bash
# Verify .env location
ls -la .env

# Check if loaded correctly
docker compose config

# Verify in container
docker compose exec my-app env | grep MONGO
```

**Lesson:** Docker Compose auto-loads .env from same directory

---

### Challenge 4: Data Lost on Restart

**Problem:**
All MongoDB data disappeared after `docker compose down`

**Cause:**
No volumes defined for data persistence

**Solution:**
```yaml
mongodb:
  volumes:
    - mongo_data:/data/db

volumes:
  mongo_data:  # Named volume
```

**Important:**
- `docker compose down` removes containers
- `docker compose down -v` removes volumes too!
- Use named volumes for persistence

**Lesson:** Always define volumes for databases!

---

### Challenge 5: Service Name Resolution

**Problem:**
App can't connect to MongoDB using 'localhost'

**Wrong:**
```javascript
const mongoUrl = 'mongodb://localhost:27017';  // ❌ Doesn't work
```

**Correct:**
```javascript
const mongoUrl = 'mongodb://mongodb:27017';   // ✅ Use service name
```

**Why:**
- 'localhost' refers to the container itself
- Not to other containers
- Use service name for inter-container communication

**Lesson:** Service names = DNS hostnames in Docker networks

---

## 🎓 Key Takeaways

### 1. **Compose Simplifies Multi-Container Apps**

**Before Compose:**
- Manual network creation
- Multiple docker run commands
- Hard to manage
- Error-prone

**After Compose:**
- Single YAML file
- One command to start/stop
- Easy to share
- Reproducible

**Impact:** 10+ commands → 1 command! 🚀

---

### 2. **Infrastructure as Code**

```yaml
# This docker-compose.yaml IS your infrastructure
# Version controlled
# Team can use exact same setup
# No "works on my machine" problems
```

**Benefits:**
- Consistent environments
- Easy onboarding
- Documentation built-in
- Disaster recovery

---

### 3. **Service Isolation with Communication**

- Each service in own container
- Isolated file systems
- Isolated processes
- BUT can communicate via network

**Best of Both Worlds:**
- Separation of concerns
- Easy to scale individual services
- Can replace one service without affecting others

---

### 4. **Environment-Based Configuration**

```bash
# Development
docker compose up

# Production (different compose file)
docker compose -f docker-compose.prod.yaml up
```

**Same Code, Different Configs:**
- Development: Local database, debug mode
- Production: Remote database, optimized build

---

### 5. **Docker Compose ≠ Production Orchestration**

**Good For:**
- Development ✅
- Testing ✅
- Small deployments ✅

**Not Ideal For:**
- Large scale production ❌
- Auto-scaling ❌
- Self-healing ❌
- Load balancing ❌

**Next Step:** Kubernetes for production orchestration

---

## 📊 Project Statistics

### What I Built:
- **Services Deployed:** 3 (Node.js, MongoDB, Mongo Express)
- **Networks Created:** 1 (automatic default network)
- **Environment Variables:** 5
- **Total Containers:** 3
- **Lines of YAML:** ~30
- **Docker Commands Used:** 20+

### Time Breakdown:
- Learning Compose concepts: 60 min
- Setting up project: 30 min
- Troubleshooting issues: 45 min
- Testing and verification: 30 min
- Documentation: 45 min
- **Total:** ~4 hours

### Files Created:
- docker-compose.yaml
- .env
- Dockerfile
- NOTES.md (comprehensive guide)
- Updated project README

---

## 🔍 Understanding Check

### Questions I Can Now Answer:

**Q: What's the difference between `docker run` and `docker compose`?**  
**A:** `docker run` starts single containers. `docker compose` orchestrates multiple containers defined in YAML file.

**Q: How do containers communicate in Compose?**  
**A:** Via service names as hostnames on the default network created by Compose.

**Q: What does `depends_on` do?**  
**A:** Ensures start order, but NOT that services are ready. Use health checks for readiness.

**Q: How to persist database data?**  
**A:** Define named volumes and mount them to data directories.

**Q: Where do environment variables come from?**  
**A:** .env file in same directory, or defined directly in compose file.

---

## 💡 Aha Moments! 

### 1. "Service Names ARE the Hostnames!"
When I realized MongoDB is accessible at `mongodb:27017` (service name), not `localhost`, everything clicked!

### 2. "One File to Rule Them All"
docker-compose.yaml defines ENTIRE infrastructure. Version control this = Infrastructure as Code!

### 3. "Compose is Docker on Easy Mode"
What took 10+ commands is now just `docker compose up`. Mind = Blown! 🤯

### 4. "Health Checks Matter"
`depends_on` without health checks = race conditions. Always use health checks for databases!

### 5. "Volumes for Persistence"
Containers are ephemeral. Volumes are permanent. Database MUST use volumes!

---

## 🔜 What's Next?

### Tomorrow (Day 4) Options:

**Option 1: Advanced Docker**
- Multi-stage builds
- Docker security
- Optimization techniques
- Production best practices

**Option 2: Linux Fundamentals**
- Command line mastery
- File system navigation
- Permissions and users
- Shell scripting basics

**Option 3: More Docker Projects**
- Full-stack app (React + Express + Postgres)
- Microservices architecture
- CI/CD integration

**My Choice:** ________________

---

## 📝 Self-Assessment

### Understanding Level (1-10):
- **Docker Compose Basics:** 9/10 ✅
- **YAML Syntax:** 8/10 ✅
- **Service Networking:** 9/10 ✅
- **Environment Variables:** 8/10 ✅
- **Debugging:** 7/10 ⚠️ (need more practice)
- **Production Ready:** 6/10 ⚠️ (need to learn more)

### Can I...?
- ✅ Write docker-compose.yaml from scratch? **YES!**
- ✅ Debug multi-container apps? **YES!**
- ✅ Explain Compose to someone? **YES!**
- ✅ Use in real projects? **YES!**
- ⚠️ Deploy to production? **Almost! Need Kubernetes**

### Confidence Level:
- **Building multi-container apps:** 9/10 💪
- **Troubleshooting issues:** 8/10 ✅
- **Ready for interviews:** 8/10 ✅
- **Production deployment:** 6/10 ⚠️

---

## 🌟 Reflections

### What Went Well:
- ✅ Completed full project start to finish
- ✅ All services working together
- ✅ Understood networking clearly
- ✅ Solved all issues encountered
- ✅ Created comprehensive documentation

### What Could Be Better:
- ⚠️ Spent too much time on port conflicts
- ⚠️ Should have used health checks from start
- ⚠️ Need to practice YAML syntax more

### Most Exciting Part:
Seeing all 3 services communicate seamlessly! When I typed in Mongo Express and saw data appear in my Node.js app - THAT was magical! ✨

### Biggest Challenge:
Understanding why MongoDB wouldn't connect. Learned that "running" doesn't mean "ready"!

### How I Overcame It:
Added retry logic in app + learned about health checks. Problem solved! 💪

---

## 📈 Progress Toward Goal

**Target:** 20+ LPA DevOps Engineer by August 2026  
**Day:** 3/180 (1.7% complete)  
**Feeling:** Gaining momentum! 🚀

**Skills Checklist:**
- ✅ Git/GitHub
- ✅ Docker basics
- ✅ Dockerfile creation
- ✅ Docker Compose
- ✅ Multi-container apps
- ⏳ Kubernetes (coming soon!)
- ⏳ CI/CD (Week 10+)

**What Employers Will See:**
- Public GitHub with daily commits
- Real projects, not just tutorials
- Problem-solving documentation
- Continuous learning proof

**Confidence in reaching goal:** 95% 💪

---

## 📚 Resources Used

### Videos Watched:
1. Docker Compose Tutorial - TechWorld with Nana
2. Docker Compose Crash Course

### Documentation Read:
1. Docker Compose Official Docs
2. MongoDB Docker Hub page
3. Mongo Express documentation

### Practice:
- Built complete 3-tier application
- Debugged multiple issues
- Tested all scenarios

---

## 🎯 Tomorrow's Preparation

### Before Day 4:
- [ ] Review Docker networking in depth
- [ ] Read about Docker security
- [ ] Check out Kubernetes basics
- [ ] Decide next learning path
- [ ] Update LinkedIn with Day 3 progress
- [ ] Commit all code to GitHub

### Optional Reading:
- Docker production best practices
- 12-factor app methodology
- Microservices architecture patterns

---

## ✅ Day 3 Checklist

- [x] Learned Docker Compose fundamentals
- [x] Built multi-container application
- [x] All 3 services working together
- [x] Debugged and solved all issues
- [x] Created comprehensive documentation
- [x] Tested data persistence
- [x] Understood networking
- [x] Mastered environment variables
- [x] Can explain to others
- [x] Ready for Day 4!

---

## 💪 Motivational Note to Future Me

**Hey Future Pratirath!**

Today you orchestrated MULTIPLE containers! 🎉

Just 3 days ago:
- Day 1: "What is Docker?"
- Day 2: "I can run a container!"
- Day 3: "I can orchestrate entire applications!"

This is EXPONENTIAL growth!

In 3 days you went from zero to building production-ready architectures!

Imagine where you'll be in:
- 30 days? (Kubernetes deployments)
- 90 days? (Full CI/CD pipelines)
- 180 days? (20+ LPA DevOps role!)

**Every day you're getting closer!**

Keep this momentum. Keep learning. Keep building.

**Your future DevOps Engineer self is proud! 💪🚀**

---

**Date Completed:** February 18, 2026  
**Status:** ✅ Day 3 CRUSHED IT!  
**Next:** Day 4 - TBD  
**Feeling:** Excited and confident! 🔥

---

*These notes represent 4+ hours of focused learning, multiple aha moments, and real-world problem-solving. This is the foundation of a DevOps career!*

**End of Day 3 Notes**
