# 📅 Day 6 - Kubernetes Fundamentals

**Date:** February 21, 2026  
**Focus:** Kubernetes architecture, Pods, Deployments, Services  
**Duration:** 8 hours (split across morning, afternoon, evening)

---

## 🎯 Learning Objectives

By the end of Day 6, you will be able to:

### Kubernetes Core:
- ✅ Understand Kubernetes architecture (Control Plane + Worker Nodes)
- ✅ Explain the role of API Server, etcd, Scheduler, Controllers
- ✅ Install and configure local Kubernetes (Minikube/Kind)
- ✅ Master kubectl command-line tool

### Workloads:
- ✅ Create and manage Pods (smallest deployable units)
- ✅ Use Deployments for application lifecycle management
- ✅ Scale applications horizontally
- ✅ Perform rolling updates and rollbacks
- ✅ Configure resource requests and limits

### Networking:
- ✅ Expose applications with Services (ClusterIP, NodePort, LoadBalancer)
- ✅ Understand service discovery and DNS
- ✅ Configure load balancing across Pods

### Organization:
- ✅ Use namespaces for resource isolation
- ✅ Apply labels and selectors for organization
- ✅ Debug and troubleshoot Kubernetes applications

---

## 📚 Topics Covered

### Morning Session (6:00 - 9:00 AM)
1. **Kubernetes Architecture & Setup**
   - Why Kubernetes? (vs Docker Compose)
   - Control Plane components (API Server, etcd, Scheduler, Controllers)
   - Worker Node components (Kubelet, Kube-proxy, Container Runtime)
   - Install Minikube/Kind
   - Configure kubectl

2. **Pods - The Smallest K8s Unit**
   - What is a Pod?
   - Imperative vs Declarative creation
   - Multi-container Pods
   - Pod lifecycle and operations
   - Interacting with Pods (exec, logs, port-forward)

3. **Deployments - Managing Pods**
   - Why Deployments over bare Pods?
   - ReplicaSets and desired state
   - Creating and managing Deployments
   - Scaling applications
   - Auto-healing demonstration
   - Rolling updates and rollbacks
   - Deployment strategies

### Afternoon Session (12:00 - 3:00 PM)
4. **Services - Exposing Applications**
   - Service types (ClusterIP, NodePort, LoadBalancer)
   - Service selectors and endpoints
   - Load balancing
   - Service discovery with DNS
   - Testing connectivity

5. **Labels, Selectors & Namespaces**
   - Labels as key-value metadata
   - Selector operations
   - Namespace isolation
   - Resource organization

6. **Hands-On Project: Blog App on K8s**
   - Multi-tier application (Frontend + Backend + Database)
   - Namespace setup
   - Service communication
   - NodePort for external access

### Evening Session (7:00 - 9:00 PM)
7. **kubectl Mastery & Debugging**
   - Essential kubectl commands
   - Viewing resources (get, describe, logs)
   - Interacting with resources (exec, port-forward, cp)
   - Troubleshooting common issues
   - Debugging workflows

8. **Advanced Topics & Best Practices**
   - ConfigMaps for configuration
   - Secrets for sensitive data
   - Resource quotas and limits
   - Production best practices

---

## 🏗️ Project Structure

```
DAY_06/
├── README.md                          # This file
├── docs/
│   └── DAY_6_PLAN.md                 # Detailed 8-hour schedule
├── notes/
│   └── day-06-notes.md               # Your learning notes
└── projects/
    └── k8s-blog-app/                  # Main project
        ├── README.md
        └── manifests/
            ├── namespace.yaml         # Blog app namespace
            ├── database.yaml          # PostgreSQL deployment + service
            ├── backend.yaml           # Node.js API deployment + service
            └── frontend.yaml          # Nginx deployment + NodePort service
```

---

## 🚀 Quick Start

### Prerequisites
```bash
# Install Homebrew (if not already installed - macOS)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Docker Desktop running (required for Minikube)
docker --version
```

### Install Kubernetes Tools

**1. Install kubectl:**
```bash
# macOS
brew install kubectl

# Verify
kubectl version --client
```

**2. Install Minikube:**
```bash
# macOS
brew install minikube

# Start Minikube
minikube start --driver=docker

# Verify
minikube status
kubectl cluster-info
```

**Alternative: Install Kind:**
```bash
# macOS
brew install kind

# Create cluster
kind create cluster --name dev-cluster

# Verify
kubectl cluster-info
```

### Get Started
```bash
# Navigate to Day 6
cd ~/DevOps-Roadmap/DAY_06

# Review the action plan
cat docs/DAY_6_PLAN.md

# Verify cluster is running
kubectl get nodes

# Create your first Pod
kubectl run nginx --image=nginx:alpine

# Check Pod status
kubectl get pods

# Start the blog app project (afternoon)
cd projects/k8s-blog-app
kubectl apply -f manifests/
```

---

## 🛠️ Essential Commands Reference

### Cluster Management
```bash
# Start Minikube
minikube start

# Stop Minikube
minikube stop

# Delete cluster
minikube delete

# Cluster information
kubectl cluster-info
kubectl get nodes
```

### Pod Commands
```bash
# Create Pod (imperative)
kubectl run nginx --image=nginx:alpine

# Create Pod (declarative)
kubectl apply -f pod.yaml

# List Pods
kubectl get pods
kubectl get pods -o wide
kubectl get pods -w  # Watch mode

# Describe Pod
kubectl describe pod <pod-name>

# View logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>  # Follow

# Execute command
kubectl exec <pod-name> -- ls /app
kubectl exec -it <pod-name> -- sh

# Port forward
kubectl port-forward pod/<pod-name> 8080:80

# Delete Pod
kubectl delete pod <pod-name>
```

### Deployment Commands
```bash
# Create Deployment
kubectl create deployment nginx --image=nginx:alpine --replicas=3

# From YAML
kubectl apply -f deployment.yaml

# List Deployments
kubectl get deployments
kubectl get deploy  # Short form

# Scale Deployment
kubectl scale deployment nginx --replicas=5

# Update image
kubectl set image deployment/nginx nginx=nginx:1.26-alpine

# Rollout status
kubectl rollout status deployment/nginx

# Rollout history
kubectl rollout history deployment/nginx

# Rollback
kubectl rollout undo deployment/nginx

# Delete Deployment
kubectl delete deployment nginx
```

### Service Commands
```bash
# Expose Deployment
kubectl expose deployment nginx --port=80 --type=NodePort

# From YAML
kubectl apply -f service.yaml

# List Services
kubectl get services
kubectl get svc  # Short form

# Describe Service
kubectl describe svc <service-name>

# Get endpoints
kubectl get endpoints <service-name>

# Get Minikube service URL
minikube service <service-name> --url

# Delete Service
kubectl delete svc <service-name>
```

### Namespace Commands
```bash
# List namespaces
kubectl get namespaces
kubectl get ns  # Short form

# Create namespace
kubectl create namespace dev

# Set default namespace
kubectl config set-context --current --namespace=dev

# List resources in namespace
kubectl get all -n dev

# Delete namespace
kubectl delete namespace dev
```

### General Commands
```bash
# Get all resources
kubectl get all

# Get events
kubectl get events --sort-by=.metadata.creationTimestamp

# API resources
kubectl api-resources

# Explain resource
kubectl explain pod
kubectl explain deployment.spec

# Edit resource
kubectl edit deployment nginx

# Delete resources
kubectl delete -f deployment.yaml
kubectl delete all --all  # Delete all resources
```

---

## 📖 Key Concepts

### Kubernetes Architecture

| Component | Location | Purpose |
|-----------|----------|---------|
| **API Server** | Control Plane | Entry point for all commands |
| **etcd** | Control Plane | Key-value store for cluster state |
| **Scheduler** | Control Plane | Assigns Pods to Nodes |
| **Controller Manager** | Control Plane | Manages controllers (Deployments, ReplicaSets) |
| **Kubelet** | Worker Node | Manages Pods on node |
| **Kube-proxy** | Worker Node | Network proxy for Services |
| **Container Runtime** | Worker Node | Runs containers (Docker, containerd) |

### Workload Hierarchy

```
Deployment
    ├─ ReplicaSet (manages replicas)
    │   ├─ Pod 1
    │   ├─ Pod 2
    │   └─ Pod 3
```

### Service Types

| Type | Use Case | Accessibility | IP |
|------|----------|---------------|-----|
| **ClusterIP** | Internal services | Cluster only | Internal |
| **NodePort** | Development/testing | External via Node:Port | Internal + Node |
| **LoadBalancer** | Production external | Internet (cloud) | External |
| **ExternalName** | External DNS | Maps to external | None |

### Resource Types

| Resource | Purpose | Use Case |
|----------|---------|----------|
| **Pod** | Container wrapper | Temporary workloads |
| **Deployment** | Stateless apps | Web apps, APIs |
| **StatefulSet** | Stateful apps | Databases (Day 7) |
| **DaemonSet** | Node-level services | Logging, monitoring (Day 7) |
| **Job** | One-time tasks | Batch processing (Day 7) |
| **CronJob** | Scheduled tasks | Backups, reports (Day 7) |

---

## 🎯 Learning Milestones

### By End of Morning Session:
- [ ] Minikube/Kind cluster running
- [ ] kubectl configured and working
- [ ] Understand K8s architecture
- [ ] Created Pods (imperative & declarative)
- [ ] Created Deployments
- [ ] Scaled applications
- [ ] Performed rolling updates

### By End of Afternoon Session:
- [ ] Created Services (ClusterIP, NodePort)
- [ ] Tested service discovery
- [ ] Used namespaces
- [ ] Applied labels and selectors
- [ ] Deployed multi-tier blog app
- [ ] Accessed app via NodePort

### By End of Evening Session:
- [ ] Mastered kubectl commands
- [ ] Debugged Pod issues
- [ ] Used ConfigMaps
- [ ] Created Secrets
- [ ] Understood best practices
- [ ] Documented learnings

---

## 📊 Progress Tracker

**Overall Roadmap Progress:**
```
Day 1-2: Docker Basics         ✅ 100%
Day 3: Docker Compose          ✅ 100%
Day 4: Production Ready        ✅ 100%
Day 5: Network & Security      ✅ 100%
Day 6: Kubernetes Basics       🔄 In Progress
Day 7-30: Advanced Topics      ⏳ Upcoming
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
- [Kubernetes Docs](https://kubernetes.io/docs/home/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [Minikube Docs](https://minikube.sigs.k8s.io/docs/)

### Video Tutorials:
- [Kubernetes in 100 Seconds](https://www.youtube.com/watch?v=PziYflu8cW8) - 2 min
- [Kubernetes Explained in 15 Minutes](https://www.youtube.com/watch?v=VnvRFRk_51k) - 15 min
- [Kubernetes Crash Course](https://www.youtube.com/watch?v=s_o8dwzRlu4) - 2 hrs

### Interactive Learning:
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
- [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/)
- [Katacoda Kubernetes](https://www.katacoda.com/courses/kubernetes)

### Books:
- Kubernetes Up & Running (O'Reilly)
- The Kubernetes Book (Nigel Poulton)

---

## 🎓 Mini-Challenges

Want extra practice? Try these:

### Challenge 1: Multi-Environment Deployment (30 min)
Deploy same app to 3 namespaces:
- dev (1 replica)
- staging (2 replicas)
- production (3 replicas)

### Challenge 2: Service Discovery (20 min)
Create 3 services:
- Frontend → Backend → Database
Test DNS resolution between services

### Challenge 3: Rolling Update (30 min)
Deploy app v1:
- Update to v2 with zero downtime
- Rollback if issues found
- Document the process

---

## 🏆 Success Criteria

You've successfully completed Day 6 if you can:

### Knowledge Check:
- [ ] Draw Kubernetes architecture diagram
- [ ] Explain Control Plane components
- [ ] Difference between Pod and Deployment
- [ ] When to use each Service type
- [ ] How service discovery works

### Practical Skills:
- [ ] Install and configure local K8s cluster
- [ ] Create Pods and Deployments
- [ ] Scale applications
- [ ] Expose services
- [ ] Debug common issues
- [ ] Use namespaces effectively

### Deliverables:
- [ ] Blog app running on K8s
- [ ] All services accessible
- [ ] Namespaces configured
- [ ] YAML manifests documented
- [ ] Code pushed to GitHub
- [ ] Notes completed

---

## 🚀 Next Steps (Day 7)

**Preview: Advanced Kubernetes**
- StatefulSets for stateful applications
- DaemonSets for node-level services
- Jobs and CronJobs for batch processing
- Persistent Volumes and Claims
- Helm package manager
- Ingress controllers
- Monitoring with Prometheus

*Get ready for production Kubernetes! 🎯*

---

## 💡 Pro Tips

1. **Use Declarative YAML:** Always prefer YAML files over imperative commands
2. **Version Control:** Keep all manifests in Git
3. **Dry Run:** Test changes with `kubectl apply --dry-run=client -f file.yaml`
4. **Watch Mode:** Use `-w` flag to watch resources: `kubectl get pods -w`
5. **Context Switching:** Use kubectx/kubens tools for easy context/namespace switching
6. **Aliases:** Create kubectl alias: `alias k=kubectl`
7. **Tab Completion:** Enable kubectl autocompletion for faster typing

**Add to ~/.zshrc:**
```bash
alias k=kubectl
source <(kubectl completion zsh)
```

---

## 📝 Notes Section

Use `notes/day-06-notes.md` to document:
- Key concepts learned
- Commands practiced
- Architecture diagrams
- Issues encountered and solutions
- Questions for further research

---

## 🆘 Troubleshooting

### Minikube Issues:
```bash
# Minikube won't start
minikube delete
minikube start --driver=docker

# Insufficient resources
minikube start --cpus=4 --memory=8192

# Check logs
minikube logs

# SSH into Minikube
minikube ssh
```

### Pod Issues:
```bash
# Pod pending
kubectl describe pod <pod-name>
# Look for: resource constraints, node issues

# Pod CrashLoopBackOff
kubectl logs <pod-name>
kubectl logs <pod-name> --previous

# Pod ImagePullBackOff
kubectl describe pod <pod-name>
# Check: image name, registry access, credentials
```

### Service Issues:
```bash
# Service has no endpoints
kubectl get endpoints <service-name>
# Check: selector matches Pod labels

# Can't access service
kubectl run test --image=busybox --rm -it -- sh
# Inside: wget -qO- <service-name>:<port>
```

### General Issues:
```bash
# Check cluster health
kubectl get componentstatuses
kubectl get nodes
kubectl cluster-info

# Check events
kubectl get events --all-namespaces --sort-by='.lastTimestamp'

# Reset everything
minikube delete
minikube start
```

---

## 📈 Career Impact

**Skills Added Today:**
- ✅ Kubernetes fundamentals
- ✅ Container orchestration
- ✅ kubectl command-line
- ✅ Service mesh basics
- ✅ Cloud-native architecture

**Market Value:**
```
Docker skills:        15-18 LPA
+ Kubernetes:         22-28 LPA ⭐
+ Production K8s:     30-40 LPA (Day 7+)
```

**Companies Hiring:**
- Google, Amazon, Microsoft
- Netflix, Uber, Airbnb
- Startups (YC companies, unicorns)
- Every cloud-native company

---

## 💼 Resume Updates

**Add these bullets after today:**

```
✅ Deployed containerized applications to Kubernetes using Deployments,
   Services, and ConfigMaps

✅ Managed local Kubernetes clusters using Minikube with kubectl CLI
   for workload orchestration

✅ Implemented service discovery and load balancing across multiple
   Pod replicas in production-like environments

✅ Configured horizontal scaling and rolling updates for zero-downtime
   deployments

✅ Troubleshot Kubernetes applications using kubectl debugging
   commands and cluster event analysis
```

**Skills to add:**
- Kubernetes (K8s)
- kubectl
- Container Orchestration
- Minikube/Kind
- Service Discovery
- Cloud-Native Architecture

---

**Keep pushing! Kubernetes is the industry standard. You're learning what Fortune 500 companies use! 🚀**

*"Docker gets you started. Kubernetes gets you hired." 💰*
