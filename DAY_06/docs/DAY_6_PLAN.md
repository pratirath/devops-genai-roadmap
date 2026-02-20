# 📅 Day 6 Action Plan - Kubernetes Fundamentals

**Date:** February 21, 2026  
**Focus:** Kubernetes Architecture, Pods, Deployments, Services  
**Goal:** Understand K8s basics and deploy your first application

---

## ✅ Previous Days' Achievements

**Day 1-2:** Docker Fundamentals ✅
- Mastered containers and Dockerfiles

**Day 3:** Docker Compose ✅
- Multi-container orchestration

**Day 4:** Production Readiness ✅
- Volumes, multi-stage builds, optimization

**Day 5:** Networking & Security ✅
- Network isolation, secrets, security hardening

**Today: Level up to Kubernetes! 🚀**

---

## 🎯 Today's Learning Objectives

By end of Day 6, you will:
- ✅ Understand Kubernetes architecture (Master + Worker nodes)
- ✅ Install and configure Minikube/Kind locally
- ✅ Master kubectl command-line tool
- ✅ Create and manage Pods
- ✅ Use Deployments for application management
- ✅ Expose applications with Services
- ✅ Understand namespaces and labels
- ✅ Deploy a multi-tier application to Kubernetes

---

## 🎯 Today's Schedule

### **Morning Session (6:00 - 9:00 AM) - 3 hours**

#### 6:00 - 7:00 AM: Kubernetes Architecture & Setup (60 min)

**Why Kubernetes?**

**Docker Compose limitations:**
- ❌ Single-host only (no multi-server)
- ❌ No auto-scaling
- ❌ No self-healing
- ❌ Limited load balancing
- ❌ No rolling updates
- ❌ No resource scheduling

**Kubernetes solves:**
- ✅ Multi-host orchestration
- ✅ Auto-scaling (horizontal & vertical)
- ✅ Self-healing (restart failed containers)
- ✅ Load balancing & service discovery
- ✅ Rolling updates & rollbacks
- ✅ Resource management & scheduling
- ✅ Declarative configuration

**Watch:**
- [Kubernetes in 100 Seconds](https://www.youtube.com/watch?v=PziYflu8cW8) - 2 min
- [Kubernetes Explained in 15 Minutes](https://www.youtube.com/watch?v=VnvRFRk_51k) - 15 min
- [Kubernetes Architecture](https://www.youtube.com/watch?v=8C_SCDbUJTg) - 20 min

**Kubernetes Architecture:**

```
┌─────────────────────────────────────────────────────────┐
│                    CONTROL PLANE                         │
│  ┌──────────────┐  ┌─────────────┐  ┌──────────────┐   │
│  │  API Server  │  │  Scheduler  │  │   etcd DB    │   │
│  │ (kubectl →)  │  │ (Pod → Node)│  │  (State DB)  │   │
│  └──────────────┘  └─────────────┘  └──────────────┘   │
│  ┌────────────────────────────────────────────────┐     │
│  │        Controller Manager                      │     │
│  │  (Deployments, ReplicaSets, Services, etc.)   │     │
│  └────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼─────────┐  ┌──────▼────────┐  ┌──────▼────────┐
│  WORKER NODE 1  │  │ WORKER NODE 2 │  │ WORKER NODE 3 │
│                 │  │               │  │               │
│  ┌──────────┐  │  │  ┌──────────┐ │  │  ┌──────────┐ │
│  │ Kubelet  │  │  │  │ Kubelet  │ │  │  │ Kubelet  │ │
│  └──────────┘  │  │  └──────────┘ │  │  └──────────┘ │
│  ┌──────────┐  │  │  ┌──────────┐ │  │  ┌──────────┐ │
│  │Kube-proxy│  │  │  │Kube-proxy│ │  │  │Kube-proxy│ │
│  └──────────┘  │  │  └──────────┘ │  │  └──────────┘ │
│  ┌──────────┐  │  │  ┌──────────┐ │  │  ┌──────────┐ │
│  │Container │  │  │  │Container │ │  │  │Container │ │
│  │ Runtime  │  │  │  │ Runtime  │ │  │  │ Runtime  │ │
│  │ (Docker) │  │  │  │ (Docker) │ │  │  │ (Docker) │ │
│  └──────────┘  │  │  └──────────┘ │  │  └──────────┘ │
│                 │  │               │  │               │
│  [POD] [POD]   │  │  [POD] [POD]  │  │  [POD]        │
└─────────────────┘  └───────────────┘  └───────────────┘
```

**Components Explained:**

**Control Plane (Master):**
1. **API Server:** Entry point for all commands (kubectl talks to this)
2. **etcd:** Database storing cluster state
3. **Scheduler:** Decides which node runs which Pod
4. **Controller Manager:** Manages controllers (Deployments, Services, etc.)

**Worker Nodes:**
1. **Kubelet:** Agent running on each node, manages Pods
2. **Kube-proxy:** Network proxy, handles Service networking
3. **Container Runtime:** Docker/containerd to run containers

**Install Kubernetes Locally:**

**Option 1: Minikube (Recommended for beginners)**
```bash
# macOS
brew install minikube

# Start Minikube
minikube start --driver=docker

# Verify
minikube status

# Expected:
# minikube: Running
# cluster: Running
# kubectl: Configured
```

**Option 2: Kind (Kubernetes in Docker)**
```bash
# macOS
brew install kind

# Create cluster
kind create cluster --name dev-cluster

# Verify
kind get clusters

# Expected: dev-cluster
```

**Install kubectl (Kubernetes CLI):**
```bash
# macOS
brew install kubectl

# Verify
kubectl version --client

# Expected: Client Version: v1.29.x
```

**Configure kubectl:**
```bash
# For Minikube (auto-configured)
minikube start

# For Kind
kind get kubeconfig --name dev-cluster > ~/.kube/config

# Verify connection
kubectl cluster-info

# Expected: Kubernetes control plane is running at...
```

---

#### 7:00 - 8:00 AM: Pods - The Smallest K8s Unit (60 min)

**What is a Pod?**
- Smallest deployable unit in Kubernetes
- Wrapper around one or more containers
- Shares network namespace (localhost between containers)
- Shares storage volumes
- Ephemeral (can be destroyed/recreated anytime)

**Pod vs Container:**
```
Container: Single app process
Pod:       1+ containers that share resources
```

**Create Your First Pod:**

**Method 1: Imperative (Quick testing)**
```bash
# Run nginx Pod
kubectl run nginx --image=nginx:alpine

# List Pods
kubectl get pods

# Detailed info
kubectl get pods -o wide

# Expected:
# NAME    READY   STATUS    RESTARTS   AGE   IP           NODE
# nginx   1/1     Running   0          10s   172.17.0.3   minikube
```

**Method 2: Declarative (Production way)**

Create `pod.yaml`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
    tier: frontend
spec:
  containers:
  - name: nginx
    image: nginx:1.25-alpine
    ports:
    - containerPort: 80
    resources:
      requests:
        memory: "64Mi"
        cpu: "100m"
      limits:
        memory: "128Mi"
        cpu: "200m"
```

**Apply the Pod:**
```bash
# Create Pod from YAML
kubectl apply -f pod.yaml

# Verify
kubectl get pods

# Describe Pod (detailed info)
kubectl describe pod nginx-pod

# View logs
kubectl logs nginx-pod

# Follow logs (like tail -f)
kubectl logs -f nginx-pod
```

**Interact with Pod:**
```bash
# Execute command in Pod
kubectl exec nginx-pod -- ls /usr/share/nginx/html

# Interactive shell
kubectl exec -it nginx-pod -- sh

# Inside Pod:
# cd /usr/share/nginx/html
# echo "Hello from K8s!" > index.html
# exit

# Port forwarding (access from localhost)
kubectl port-forward pod/nginx-pod 8080:80

# Open browser: http://localhost:8080
```

**Multi-Container Pod:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    ports:
    - containerPort: 80
  
  - name: sidecar
    image: busybox
    command: ['sh', '-c', 'while true; do echo "Sidecar running"; sleep 30; done']
```

**Apply and test:**
```bash
kubectl apply -f multi-container-pod.yaml

# View logs from specific container
kubectl logs multi-container-pod -c nginx
kubectl logs multi-container-pod -c sidecar

# Exec into specific container
kubectl exec -it multi-container-pod -c nginx -- sh
```

**Pod Lifecycle:**
```bash
# Delete Pod
kubectl delete pod nginx-pod

# Delete using YAML
kubectl delete -f pod.yaml

# Delete all Pods
kubectl delete pods --all
```

**Key Pod Concepts:**
- Each Pod gets unique IP
- Containers in same Pod share localhost
- Pods are ephemeral (mortal, not resurrected)
- Use labels for organization
- Resource requests & limits prevent resource hogging

---

#### 8:00 - 9:00 AM: Deployments - Managing Pods (60 min)

**Why Deployments?**

**Problems with bare Pods:**
- ❌ If Pod dies, it's gone (no auto-restart)
- ❌ No scaling (can't run multiple copies)
- ❌ No rolling updates
- ❌ No rollback capability

**Deployments provide:**
- ✅ Desired state management (want 3 Pods? Always have 3)
- ✅ Auto-healing (Pod crashes? New one created)
- ✅ Scaling (up/down with single command)
- ✅ Rolling updates (zero-downtime updates)
- ✅ Rollback (undo bad deployments)

**Deployment → ReplicaSet → Pods:**
```
Deployment
    ├─ ReplicaSet (manages Pod replicas)
    │   ├─ Pod 1
    │   ├─ Pod 2
    │   └─ Pod 3
```

**Create Deployment:**

**Method 1: Imperative**
```bash
# Create Deployment
kubectl create deployment nginx --image=nginx:alpine --replicas=3

# List Deployments
kubectl get deployments

# List ReplicaSets (auto-created)
kubectl get rs

# List Pods (3 created automatically)
kubectl get pods

# Expected: 3 Pods named nginx-<hash>-<hash>
```

**Method 2: Declarative (Recommended)**

Create `deployment.yaml`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
```

**Apply Deployment:**
```bash
# Create Deployment
kubectl apply -f deployment.yaml

# Watch Pods being created
kubectl get pods -w

# Check Deployment status
kubectl rollout status deployment/nginx-deployment

# Expected: deployment "nginx-deployment" successfully rolled out
```

**Scaling:**
```bash
# Scale up to 5 replicas
kubectl scale deployment nginx-deployment --replicas=5

# Verify
kubectl get pods

# Scale down to 2
kubectl scale deployment nginx-deployment --replicas=2

# Alternative: Edit YAML and reapply
# Change replicas: 2 in deployment.yaml
kubectl apply -f deployment.yaml
```

**Auto-Healing Demo:**
```bash
# List Pods
kubectl get pods

# Delete one Pod
kubectl delete pod <pod-name>

# Watch new Pod being created automatically
kubectl get pods -w

# Deployment maintains desired state (3 replicas)
```

**Updates (Rolling Update):**
```bash
# Update image version
kubectl set image deployment/nginx-deployment nginx=nginx:1.26-alpine

# Watch rollout
kubectl rollout status deployment/nginx-deployment

# Check rollout history
kubectl rollout history deployment/nginx-deployment

# Expected: Revision 1, 2, etc.
```

**Rollback:**
```bash
# Rollback to previous version
kubectl rollout undo deployment/nginx-deployment

# Rollback to specific revision
kubectl rollout undo deployment/nginx-deployment --to-revision=1

# Check status
kubectl rollout status deployment/nginx-deployment
```

**Deployment Strategies:**

**1. Rolling Update (Default):**
```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # Max extra Pods during update
      maxUnavailable: 0  # Max Pods down during update
```

**2. Recreate (All at once):**
```yaml
spec:
  strategy:
    type: Recreate  # Kill all old Pods, then create new
```

---

### **Afternoon Session (12:00 - 3:00 PM) - 3 hours**

#### 12:00 - 1:00 PM: Services - Exposing Applications (60 min)

**Why Services?**

**Problems without Services:**
- ❌ Pod IPs change when Pods restart
- ❌ Can't load balance across multiple Pods
- ❌ Can't expose apps outside cluster

**Services provide:**
- ✅ Stable IP/DNS name
- ✅ Load balancing across Pods
- ✅ Service discovery
- ✅ External access (when needed)

**Service Types:**

**1. ClusterIP (Default):**
- Internal only
- Accessible within cluster
- Use case: Backend APIs, databases

**2. NodePort:**
- Exposes on each node's IP
- Accessible from outside cluster
- Use case: Development, testing

**3. LoadBalancer:**
- Cloud provider load balancer
- Public IP assigned
- Use case: Production external services

**4. ExternalName:**
- Maps to external DNS name
- Use case: External services

**Create ClusterIP Service:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP
  selector:
    app: nginx  # Matches Pod labels
  ports:
  - port: 80          # Service port
    targetPort: 80    # Container port
    protocol: TCP
```

**Apply Service:**
```bash
# Create Service
kubectl apply -f service-clusterip.yaml

# List Services
kubectl get svc

# Expected:
# NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)
# nginx-service   ClusterIP   10.96.123.45    <none>        80/TCP

# Describe Service
kubectl describe svc nginx-service

# Test from within cluster
kubectl run test-pod --image=busybox --rm -it -- sh

# Inside test pod:
wget -qO- nginx-service:80
# Should see nginx welcome page
```

**Create NodePort Service:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080  # Port on node (30000-32767)
```

**Apply and test:**
```bash
kubectl apply -f service-nodeport.yaml

# Get service
kubectl get svc nginx-nodeport

# Expected:
# NAME             TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)
# nginx-nodeport   NodePort   10.96.123.46    <none>        80:30080/TCP

# For Minikube, get URL
minikube service nginx-nodeport --url

# Expected: http://192.168.49.2:30080

# Access in browser or:
curl $(minikube service nginx-nodeport --url)
```

**Create LoadBalancer Service (Cloud only):**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
```

**Note:** LoadBalancer works in cloud (AWS, GCP, Azure). In Minikube, use `minikube tunnel` to simulate.

**Service Discovery:**
```bash
# Services get DNS names automatically
# Format: <service-name>.<namespace>.svc.cluster.local

# From any Pod, you can access:
curl nginx-service  # Same namespace
curl nginx-service.default.svc.cluster.local  # Full FQDN
```

---

#### 1:00 - 2:00 PM: Labels, Selectors & Namespaces (60 min)

**Labels:**
Key-value pairs attached to objects (Pods, Services, etc.)

```yaml
metadata:
  labels:
    app: nginx
    tier: frontend
    env: production
    version: v1
```

**Label Operations:**
```bash
# Show labels
kubectl get pods --show-labels

# Filter by label
kubectl get pods -l app=nginx
kubectl get pods -l tier=frontend,env=production

# Add label to existing Pod
kubectl label pod nginx-pod env=dev

# Update label
kubectl label pod nginx-pod env=production --overwrite

# Remove label
kubectl label pod nginx-pod env-
```

**Selectors:**
Used by Services, Deployments to match Pods

```yaml
# Service selector
spec:
  selector:
    app: nginx
    tier: frontend

# Deployment selector
spec:
  selector:
    matchLabels:
      app: nginx
    matchExpressions:
    - key: tier
      operator: In
      values:
      - frontend
      - backend
```

**Namespaces:**
Virtual clusters within physical cluster

```bash
# List namespaces
kubectl get namespaces

# Default namespaces:
# default      - Default namespace
# kube-system  - Kubernetes system components
# kube-public  - Publicly readable
# kube-node-lease - Node heartbeats

# Create namespace
kubectl create namespace dev
kubectl create namespace staging
kubectl create namespace production

# Create from YAML
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: test
EOF

# List resources in namespace
kubectl get pods -n dev
kubectl get all -n kube-system

# Set default namespace
kubectl config set-context --current --namespace=dev

# Create resource in namespace
kubectl apply -f deployment.yaml -n dev

# Or specify in YAML:
# metadata:
#   namespace: dev
```

**Namespace Use Cases:**
- **Environment separation:** dev, staging, prod
- **Team separation:** team-a, team-b
- **Resource quotas:** Limit CPU/memory per namespace
- **RBAC:** Role-based access control per namespace

---

#### 2:00 - 3:00 PM: Project - Deploy Blog App to K8s (60 min)

**Project:** Multi-tier blog application (Frontend + Backend + Database)

**Architecture:**
```
Internet
    |
[NodePort Service] → [Frontend Pods]
                          |
                     [ClusterIP Service]
                          |
                     [Backend Pods]
                          |
                     [ClusterIP Service]
                          |
                     [Database Pod]
                          |
                     [PersistentVolume]
```

**Create project structure:**
```bash
mkdir -p ~/DevOps-Roadmap/DAY_06/projects/k8s-blog-app
cd ~/DevOps-Roadmap/DAY_06/projects/k8s-blog-app

mkdir manifests
touch manifests/{namespace.yaml,database.yaml,backend.yaml,frontend.yaml}
```

**1. Namespace (`namespace.yaml`):**
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: blog-app
```

**2. Database (`database.yaml`):**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres
  namespace: blog-app
spec:
  type: ClusterIP
  selector:
    app: postgres
  ports:
  - port: 5432
    targetPort: 5432
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
  namespace: blog-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        env:
        - name: POSTGRES_DB
          value: blogdb
        - name: POSTGRES_USER
          value: bloguser
        - name: POSTGRES_PASSWORD
          value: blogpass123  # Use Secrets in production!
        ports:
        - containerPort: 5432
        resources:
          requests:
            memory: "256Mi"
            cpu: "200m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

**3. Backend (`backend.yaml`):**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend
  namespace: blog-app
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
  - port: 8080
    targetPort: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  namespace: blog-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: node:20-alpine
        workingDir: /app
        command: ['sh', '-c']
        args:
        - |
          cat > server.js <<'EOF'
          const http = require('http');
          const server = http.createServer((req, res) => {
            res.writeHead(200, {'Content-Type': 'application/json'});
            res.end(JSON.stringify({
              message: 'Backend API running',
              hostname: require('os').hostname(),
              timestamp: new Date().toISOString()
            }));
          });
          server.listen(8080, () => console.log('Backend on 8080'));
          EOF
          node server.js
        ports:
        - containerPort: 8080
        env:
        - name: DB_HOST
          value: postgres
        - name: DB_NAME
          value: blogdb
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
```

**4. Frontend (`frontend.yaml`):**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend
  namespace: blog-app
spec:
  type: NodePort
  selector:
    app: frontend
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: blog-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "100m"
        volumeMounts:
        - name: html
          mountPath: /usr/share/nginx/html
      initContainers:
      - name: setup
        image: busybox
        command:
        - sh
        - -c
        - |
          cat > /html/index.html <<'EOF'
          <!DOCTYPE html>
          <html>
          <head><title>K8s Blog</title></head>
          <body>
            <h1>Blog App on Kubernetes</h1>
            <button onclick="fetchBackend()">Test Backend</button>
            <div id="result"></div>
            <script>
              function fetchBackend() {
                fetch('/api')
                  .then(r => r.json())
                  .then(d => {
                    document.getElementById('result').innerHTML = 
                      '<pre>' + JSON.stringify(d, null, 2) + '</pre>';
                  });
              }
            </script>
          </body>
          </html>
          EOF
        volumeMounts:
        - name: html
          mountPath: /html
      volumes:
      - name: html
        emptyDir: {}
```

**Deploy the application:**
```bash
# Create namespace
kubectl apply -f manifests/namespace.yaml

# Deploy all components
kubectl apply -f manifests/database.yaml
kubectl apply -f manifests/backend.yaml
kubectl apply -f manifests/frontend.yaml

# Watch Pods starting
kubectl get pods -n blog-app -w

# Check all resources
kubectl get all -n blog-app

# Expected:
# 1 postgres Pod
# 2 backend Pods
# 2 frontend Pods
# 3 Services (postgres, backend, frontend)
```

**Test the application:**
```bash
# Get frontend URL
minikube service frontend -n blog-app --url

# Expected: http://192.168.49.2:30080

# Access in browser
open $(minikube service frontend -n blog-app --url)

# Or curl
curl $(minikube service frontend -n blog-app --url)
```

---

### **Evening Session (7:00 - 9:00 PM) - 2 hours**

#### 7:00 - 8:00 PM: kubectl Mastery & Debugging (60 min)

**Essential kubectl Commands:**

**Get Resources:**
```bash
# All resource types
kubectl api-resources

# Pods
kubectl get pods
kubectl get pods -o wide
kubectl get pods -o yaml
kubectl get pods -o json

# All resources
kubectl get all
kubectl get all -n blog-app

# Watch (real-time updates)
kubectl get pods -w

# Sort by
kubectl get pods --sort-by=.metadata.creationTimestamp
```

**Describe (Detailed info):**
```bash
kubectl describe pod <pod-name>
kubectl describe deployment <deployment-name>
kubectl describe service <service-name>
kubectl describe node minikube
```

**Logs:**
```bash
# View logs
kubectl logs <pod-name>

# Follow logs
kubectl logs -f <pod-name>

# Previous container (if crashed)
kubectl logs <pod-name> --previous

# Multi-container Pod
kubectl logs <pod-name> -c <container-name>

# All Pods in Deployment
kubectl logs -l app=nginx

# Last 50 lines
kubectl logs <pod-name> --tail=50

# Since 1 hour ago
kubectl logs <pod-name> --since=1h
```

**Exec:**
```bash
# Interactive shell
kubectl exec -it <pod-name> -- sh
kubectl exec -it <pod-name> -- bash

# Single command
kubectl exec <pod-name> -- ls /app
kubectl exec <pod-name> -- env

# Multi-container
kubectl exec -it <pod-name> -c <container> -- sh
```

**Port Forward:**
```bash
# Forward local port to Pod
kubectl port-forward pod/<pod-name> 8080:80

# Forward to Service
kubectl port-forward svc/<service-name> 8080:80

# Forward to Deployment
kubectl port-forward deployment/<name> 8080:80
```

**Copy Files:**
```bash
# Copy to Pod
kubectl cp local-file.txt <pod-name>:/path/in/pod

# Copy from Pod
kubectl cp <pod-name>:/path/in/pod local-file.txt
```

**Edit Resources:**
```bash
# Edit live (opens editor)
kubectl edit deployment nginx-deployment

# Opens YAML in editor, save to apply changes
```

**Delete Resources:**
```bash
# Delete Pod
kubectl delete pod <pod-name>

# Delete Deployment
kubectl delete deployment <name>

# Delete using YAML
kubectl delete -f deployment.yaml

# Delete all Pods
kubectl delete pods --all

# Force delete
kubectl delete pod <name> --force --grace-period=0
```

**Debugging Commands:**
```bash
# Events (cluster-wide)
kubectl get events --sort-by=.metadata.creationTimestamp

# Events for namespace
kubectl get events -n blog-app

# Check node resources
kubectl top nodes
kubectl describe node minikube

# Check Pod resources
kubectl top pods
kubectl top pods -n blog-app

# Check cluster info
kubectl cluster-info
kubectl cluster-info dump

# API versions
kubectl api-versions

# Explain resources
kubectl explain pod
kubectl explain pod.spec
kubectl explain pod.spec.containers
```

**Troubleshooting Scenarios:**

**1. Pod not starting:**
```bash
# Check status
kubectl get pods

# If Pending:
kubectl describe pod <pod-name>
# Look for: Insufficient resources, node selector issues

# If CrashLoopBackOff:
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
# Fix application code/config

# If ImagePullBackOff:
kubectl describe pod <pod-name>
# Check image name, credentials, network
```

**2. Service not accessible:**
```bash
# Check Service
kubectl get svc

# Check endpoints (should match Pods)
kubectl get endpoints <service-name>

# If no endpoints:
# - Check selector matches Pod labels
# - Check Pods are Running

# Test from within cluster
kubectl run test --image=busybox --rm -it -- sh
wget -qO- <service-name>:<port>
```

**3. Networking issues:**
```bash
# Check Pod IPs
kubectl get pods -o wide

# Check Service ClusterIP
kubectl get svc

# DNS test
kubectl run test --image=busybox --rm -it -- nslookup <service-name>

# Connectivity test
kubectl run test --image=busybox --rm -it -- wget -qO- <service-name>
```

---

#### 8:00 - 9:00 PM: Advanced Topics & Best Practices (60 min)

**ConfigMaps (External Configuration):**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "postgres://postgres:5432/mydb"
  log_level: "info"
  config.json: |
    {
      "feature_flags": {
        "new_ui": true
      }
    }
```

**Use in Pod:**
```yaml
spec:
  containers:
  - name: app
    image: myapp
    env:
    - name: DATABASE_URL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database_url
    volumeMounts:
    - name: config
      mountPath: /etc/config
  volumes:
  - name: config
    configMap:
      name: app-config
```

**Secrets (Sensitive Data):**
```bash
# Create secret from literal
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=secret123

# Create from file
kubectl create secret generic tls-secret \
  --from-file=tls.crt=cert.crt \
  --from-file=tls.key=cert.key

# List secrets
kubectl get secrets

# Describe (values are hidden)
kubectl describe secret db-secret
```

**Use Secret in Pod:**
```yaml
spec:
  containers:
  - name: app
    image: myapp
    env:
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: username
    - name: DB_PASS
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password
```

**Resource Quotas (Namespace limits):**
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: dev
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
    pods: "20"
```

**LimitRange (Default limits):**
```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: dev
spec:
  limits:
  - default:
      cpu: 200m
      memory: 256Mi
    defaultRequest:
      cpu: 100m
      memory: 128Mi
    type: Container
```

**Best Practices:**

**1. Always use Deployments (not bare Pods)**
```bash
# ❌ Don't
kubectl run nginx --image=nginx

# ✅ Do
kubectl create deployment nginx --image=nginx
```

**2. Set resource requests/limits**
```yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "100m"
  limits:
    memory: "256Mi"
    cpu: "200m"
```

**3. Use liveness/readiness probes**
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 15
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

**4. Use namespaces for organization**
```bash
# Environments
kubectl create namespace dev
kubectl create namespace staging
kubectl create namespace production
```

**5. Label everything**
```yaml
labels:
  app: myapp
  tier: frontend
  env: production
  version: v1.2.3
```

**6. Use declarative YAML (not imperative commands)**
```bash
# ❌ Imperative (hard to track)
kubectl create deployment nginx --image=nginx
kubectl scale deployment nginx --replicas=3
kubectl set image deployment/nginx nginx=nginx:1.26

# ✅ Declarative (version controlled)
kubectl apply -f deployment.yaml
# Edit deployment.yaml
kubectl apply -f deployment.yaml
```

---

## 📝 Today's Deliverables

**By end of Day 6, you must have:**

1. ✅ **Minikube/Kind cluster running**
   - kubectl configured
   - Cluster info verified

2. ✅ **Blog App deployed to K8s**
   - Namespace created
   - Database, Backend, Frontend running
   - Services configured
   - Application accessible

3. ✅ **kubectl skills**
   - Created Pods, Deployments, Services
   - Scaled applications
   - Performed rolling updates
   - Debugged issues

4. ✅ **Documentation**
   - Notes on K8s concepts
   - Commands practiced
   - Issues and solutions

5. ✅ **GitHub update**
   - Push DAY_06 manifests
   - Update main README

---

## 📚 Resources for Today

### Videos:
- [Kubernetes in 100 Seconds](https://www.youtube.com/watch?v=PziYflu8cW8)
- [Kubernetes Crash Course](https://www.youtube.com/watch?v=s_o8dwzRlu4)
- [kubectl Commands Guide](https://www.youtube.com/watch?v=azuwXALfyRg)

### Documentation:
- [Kubernetes Docs](https://kubernetes.io/docs/home/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)

### Interactive Learning:
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
- [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/)

---

## ✅ End of Day Checklist

- [ ] Minikube/Kind installed and running
- [ ] kubectl installed and configured
- [ ] Created Pods (imperative & declarative)
- [ ] Created Deployments
- [ ] Scaled Deployments
- [ ] Created Services (ClusterIP, NodePort)
- [ ] Deployed multi-tier blog app
- [ ] Practiced kubectl commands
- [ ] Debugged issues
- [ ] Used namespaces and labels
- [ ] Documented learnings
- [ ] Updated GitHub

---

## 🎯 Success Metrics

**Knowledge:**
- [ ] Explain K8s architecture
- [ ] Difference between Pod and Deployment
- [ ] Service types and use cases
- [ ] kubectl basic commands
- [ ] Troubleshooting workflow

**Practical:**
- [ ] Deploy applications to K8s
- [ ] Scale applications
- [ ] Expose services
- [ ] Debug Pod issues
- [ ] Use namespaces

---

## 🚀 Tomorrow's Preview (Day 7)

**Focus:** Advanced Kubernetes
- StatefulSets for databases
- DaemonSets for node services
- Jobs and CronJobs
- Persistent Volumes
- Helm package manager
- Deploy complex multi-tier app

**Get ready for production K8s! 🔥**

---

## 💪 Motivational Reminder

**Day 6 Progress:**
```
████████████░░░░░░░░░░ 30% Complete
```

**What you've mastered:**
- ✅ Docker fundamentals
- ✅ Multi-container apps
- ✅ Security & networking
- ✅ Kubernetes basics (today!)

**You're now in the orchestration league! 🎯**

Kubernetes = Enterprise-level skill = 25+ LPA potential! 💰

---

**Ready to orchestrate? Let's Kubernetes! ☸️**

*Remember: Companies pay premium for K8s skills. You're building those skills RIGHT NOW! Keep pushing! 💪*
