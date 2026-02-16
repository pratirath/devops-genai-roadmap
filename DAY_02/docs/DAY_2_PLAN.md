# 📅 Day 2 Action Plan - Docker Deep Dive

**Date:** February 16, 2026  
**Focus:** Docker Fundamentals & Hands-on Practice  
**Goal:** Master basic Docker commands and concepts

---

## ✅ Yesterday's Wins (Day 1)
- ✅ Created complete learning roadmap
- ✅ Set up GitHub repository
- ✅ Made repository public
- ✅ Organized documentation
- ✅ Posted on LinkedIn (if done!)

**Great start! Now let's build on it! 🚀**

---

## 🎯 Today's Schedule

### **Morning Session (6:00 - 8:00 AM) - 2 hours**

#### 6:00 - 7:30 AM: Docker Tutorial (90 min)
**Watch & Follow Along:**
- [Docker Tutorial for Beginners - freeCodeCamp](https://www.youtube.com/watch?v=fqMOX6JJhGo)
- Watch sections: Introduction, Images, Containers, Volumes
- Take notes in a markdown file

**Your Notes Structure:**
```bash
cd ~/DevOps-Projects
mkdir docker-learning
cd docker-learning
touch docker-notes.md
```

**What to Note:**
- Key concepts you learn
- Important commands
- Questions that arise
- Aha moments!

#### 7:30 - 8:00 AM: Morning Practice (30 min)
Practice the commands you just learned!

---

### **Evening Session (8:00 - 10:00 PM) - 2 hours**

#### 8:00 - 9:30 PM: Hands-on Docker Practice (90 min)
Complete all exercises below

#### 9:30 - 10:00 PM: Documentation & GitHub (30 min)
- Update progress tracker
- Commit today's work
- Plan tomorrow

---

## 💻 Hands-On Exercises (Do All!)

### **Exercise 1: Basic Container Operations** (15 min)

```bash
# 1. Pull nginx image
docker pull nginx

# 2. Run nginx container
docker run -d -p 8080:80 --name my-nginx nginx

# 3. Check running containers
docker ps

# 4. View logs
docker logs my-nginx

# 5. Stop container
docker stop my-nginx

# 6. Start it again
docker start my-nginx

# 7. Remove container
docker stop my-nginx
docker rm my-nginx

# 8. Remove image
docker rmi nginx
```

**✅ Checkpoint:** Can you start and stop containers? Good! Move on.

---

### **Exercise 2: Working with Multiple Containers** (15 min)

```bash
# 1. Run nginx
docker run -d -p 8080:80 --name web nginx

# 2. Run Redis
docker run -d --name cache redis

# 3. Run MongoDB
docker run -d --name database mongo

# 4. List all running containers
docker ps

# 5. Check resource usage
docker stats --no-stream

# 6. Stop all
docker stop web cache database

# 7. Remove all
docker rm web cache database
```

**✅ Checkpoint:** Multiple containers running? Great! Continue.

---

### **Exercise 3: Custom HTML in Nginx** (20 min)

```bash
# 1. Create a directory for your project
cd ~/DevOps-Projects
mkdir docker-nginx-demo
cd docker-nginx-demo

# 2. Create index.html
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My First Docker App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        h1 { font-size: 3rem; }
        p { font-size: 1.5rem; }
    </style>
</head>
<body>
    <h1>🚀 Hello from Docker!</h1>
    <p>Day 2: Learning Docker</p>
    <p>Container is running successfully!</p>
</body>
</html>
EOF

# 3. Run nginx with your custom HTML
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html --name my-web nginx

# 4. Visit in browser
open http://localhost:8080

# 5. Make changes to index.html (edit it)
# Refresh browser - see instant changes!

# 6. Clean up
docker stop my-web && docker rm my-web
```

**✅ Checkpoint:** See your custom page in browser? Awesome! 🎉

---

### **Exercise 4: Docker Exec & Interactive Mode** (15 min)

```bash
# 1. Run Ubuntu container
docker run -it --name my-ubuntu ubuntu bash

# Inside container:
apt-get update
apt-get install -y curl
curl --version
exit

# 2. Run container in background
docker run -d --name bg-ubuntu ubuntu sleep infinity

# 3. Execute commands in running container
docker exec bg-ubuntu ls -la
docker exec bg-ubuntu pwd
docker exec -it bg-ubuntu bash  # Interactive shell

# Inside: try some commands, then exit

# 4. Clean up
docker stop bg-ubuntu && docker rm bg-ubuntu
```

**✅ Checkpoint:** Comfortable with docker exec? Perfect!

---

### **Exercise 5: Understanding Docker Images** (15 min)

```bash
# 1. Search for images
docker search python

# 2. Pull different versions
docker pull python:3.9
docker pull python:3.11
docker pull python:alpine

# 3. List all images
docker images

# 4. Inspect an image
docker inspect python:3.11

# 5. Check image history
docker history python:3.11

# 6. Tag an image
docker tag python:3.11 my-python:latest

# 7. Remove images
docker rmi python:3.9
docker rmi python:alpine
docker rmi my-python:latest
```

**✅ Checkpoint:** Understand images vs containers? Excellent!

---

### **Exercise 6: Create Your First Dockerfile** (30 min)

```bash
# 1. Create project directory
cd ~/DevOps-Projects
mkdir my-first-docker-app
cd my-first-docker-app

# 2. Create a simple Python app
cat > app.py << 'EOF'
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Docker App</title>
            <style>
                body {{
                    font-family: Arial;
                    text-align: center;
                    padding: 50px;
                    background: #667eea;
                    color: white;
                }}
            </style>
        </head>
        <body>
            <h1>🐳 My First Dockerized App!</h1>
            <p>Current time: {datetime.now()}</p>
            <p>Running inside a Docker container</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    print('Server running on port 8080...')
    server.serve_forever()
EOF

# 3. Create Dockerfile
cat > Dockerfile << 'EOF'
# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application
COPY app.py .

# Expose port
EXPOSE 8080

# Run application
CMD ["python", "app.py"]
EOF

# 4. Build the image
docker build -t my-python-app:v1 .

# 5. Run the container
docker run -d -p 8080:8080 --name my-app my-python-app:v1

# 6. Test it
open http://localhost:8080

# 7. View logs
docker logs my-app

# 8. Stop and remove
docker stop my-app && docker rm my-app
```

**✅ Checkpoint:** Built your first Docker image? YOU'RE A DOCKER DEVELOPER NOW! 🎉

---

## 📝 Documentation Time (30 min)

### 1. Create Learning Notes (15 min)

```bash
cd ~/DevOps-Projects/docker-learning

# Create your notes file
cat > docker-notes-day2.md << 'EOF'
# Day 2: Docker Deep Dive Notes

## Date: Feb 16, 2026

## Key Concepts Learned

### 1. Docker Architecture
- Write what you learned about Docker architecture

### 2. Images vs Containers
- Write the difference you understood

### 3. Docker Commands
List the commands you used:
- `docker run`
- `docker ps`
- `docker exec`
- etc.

## Challenges Faced
- Write any issues you encountered
- How did you solve them?

## Aha Moments! 💡
- What clicked for you today?
- What was the coolest thing?

## Questions for Tomorrow
- What are you still confused about?
- What do you want to explore next?

## Tomorrow's Plan
- Docker Networking
- Docker Volumes in depth
- Start multi-container project
EOF

# Open and fill it in
open docker-notes-day2.md
```

### 2. Update Progress Tracker (5 min)

```bash
cd ~/DevOps-Projects/../Devops_Roadmap
open docs/PROGRESS_TRACKER.md
```

**Mark these as complete:**
- [x] Day 2: Docker tutorial watched
- [x] Docker commands practiced
- [x] First Dockerfile created
- [x] Built and ran custom container

### 3. Commit to GitHub (10 min)

```bash
cd ~/Prathiksa/Python_Practice/24Nov/Devops_Roadmap

# Add new files
git add .

# Commit with clear message
git commit -m "Day 2: Completed Docker fundamentals

- Watched 90min Docker tutorial
- Practiced 20+ Docker commands
- Created first custom Dockerfile
- Built and ran Python app in container
- Completed 6 hands-on exercises

Skills gained:
- Container lifecycle management
- Docker images and volumes
- Building custom images
- Interactive container sessions

Next: Docker networking and multi-container apps"

# Push to GitHub
git push origin main
```

---

## 🎯 Success Criteria (Check All!)

By end of Day 2, you should be able to:

- [ ] Explain what Docker is and why we use it
- [ ] Pull images from Docker Hub
- [ ] Run containers from images
- [ ] Start, stop, and remove containers
- [ ] List running and stopped containers
- [ ] View container logs
- [ ] Execute commands inside containers
- [ ] Mount volumes to containers
- [ ] Create a simple Dockerfile
- [ ] Build an image from Dockerfile
- [ ] Run your custom image
- [ ] Understand basic Docker networking

**If you checked 10+, you're CRUSHING IT! 🔥**

---

## 📚 Additional Resources (If Time Permits)

### Quick Reads (15 min each):
- [Docker Overview](https://docs.docker.com/get-started/overview/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

### Practice Platforms:
- [Play with Docker](https://labs.play-with-docker.com/) - Free browser-based Docker playground
- [KillerCoda Docker Labs](https://killercoda.com/docker)

---

## 🎉 End of Day Celebration!

### When You Complete Everything:

1. **Take a Screenshot** of your running container
2. **Update LinkedIn** with a progress post:
   ```
   Day 2 ✅ 
   
   Just completed Docker fundamentals!
   - Built my first Dockerfile
   - Ran custom Python app in container
   - Practiced 20+ Docker commands
   
   6 months to go! 🚀
   
   #DevOps #Docker #Learning #100DaysOfCode
   ```

3. **Pat yourself on the back** - You're 2 days in and already building with Docker!

---

## 🔥 Tomorrow's Preview (Day 3)

**Day 3: Multi-Container Apps & Docker Compose**
- Learn Docker Compose
- Create multi-tier application
- Connect containers together
- Start Project #1: Dockerized 3-Tier App

**Get excited! Tomorrow you'll build something REAL! 🚀**

---

## 💪 Motivational Note

**"Two days ago, you had just an idea. Today, you're building containerized applications. That's PROGRESS!"**

You're not just learning Docker. You're building the foundation for:
- Kubernetes (coming soon!)
- Cloud deployments
- CI/CD pipelines
- Your 20+ LPA career

**Keep going! You're doing AMAZING! 🔥**

---

## 📊 Day 2 Stats Tracker

Fill this in before sleeping:

- **Hours spent learning:** _____ / 4 hours
- **Exercises completed:** _____ / 6
- **Docker commands learned:** _____ 
- **Containers created:** _____
- **Images built:** _____
- **Feeling (1-10):** _____
- **Energy level (1-10):** _____

**Most exciting thing today:** ________________________________

**Biggest challenge:** ________________________________

**How I overcame it:** ________________________________

---

## ✅ Before Sleep Checklist

- [ ] All exercises completed
- [ ] Notes documented
- [ ] Progress tracker updated
- [ ] GitHub commit pushed
- [ ] Reviewed tomorrow's plan
- [ ] Set alarm for tomorrow's learning session

**Sleep well! Tomorrow is another exciting day! 🌟**

---

**Remember: Consistency > Intensity. Show up every day, even if just for 30 minutes!**

**You got this! 💪🚀**
