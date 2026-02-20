# 🚀 Blog App on Kubernetes

A multi-tier blog application demonstrating Kubernetes fundamentals: Pods, Deployments, Services, and Namespaces.

---

## 🏗️ Architecture

```
Internet
    |
    v
[NodePort Service :30080]
    |
    v
[Frontend Deployment]
 ├─ nginx Pod 1
 └─ nginx Pod 2
    |
    v
[ClusterIP Service :80]
    |
    v
[Backend Deployment]
 ├─ Node.js API Pod 1
 └─ Node.js API Pod 2
    |
    v
[ClusterIP Service :8080]
    |
    v
[Database Deployment]
 └─ PostgreSQL Pod
```

### Components

| Component | Type | Replicas | Service Type | Port |
|-----------|------|----------|--------------|------|
| **Frontend** | Deployment | 2 | NodePort | 80 → 30080 |
| **Backend** | Deployment | 2 | ClusterIP | 8080 |
| **Database** | Deployment | 1 | ClusterIP | 5432 |

---

## 🚀 Quick Start

### Prerequisites
```bash
# Minikube or Kind cluster running
minikube status
# OR
kubectl cluster-info

# kubectl installed
kubectl version --client
```

### Deploy Application

**1. Navigate to project:**
```bash
cd ~/DevOps-Roadmap/DAY_06/projects/k8s-blog-app
```

**2. Deploy all components:**
```bash
# Create namespace
kubectl apply -f manifests/namespace.yaml

# Deploy database
kubectl apply -f manifests/database.yaml

# Deploy backend
kubectl apply -f manifests/backend.yaml

# Deploy frontend
kubectl apply -f manifests/frontend.yaml

# Or deploy all at once:
kubectl apply -f manifests/
```

**3. Watch Pods starting:**
```bash
kubectl get pods -n blog-app -w
```

**4. Verify all components:**
```bash
kubectl get all -n blog-app
```

Expected output:
```
NAME                            READY   STATUS    RESTARTS   AGE
pod/backend-xxx-xxx             1/1     Running   0          1m
pod/backend-xxx-xxx             1/1     Running   0          1m
pod/frontend-xxx-xxx            1/1     Running   0          1m
pod/frontend-xxx-xxx            1/1     Running   0          1m
pod/postgres-xxx-xxx            1/1     Running   0          1m

NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)
service/backend    ClusterIP   10.96.100.1     <none>        8080/TCP
service/frontend   NodePort    10.96.100.2     <none>        80:30080/TCP
service/postgres   ClusterIP   10.96.100.3     <none>        5432/TCP

NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/backend    2/2     2            2           1m
deployment.apps/frontend   2/2     2            2           1m
deployment.apps/postgres   1/1     1            1           1m
```

**5. Access application:**
```bash
# Get URL (Minikube)
minikube service frontend -n blog-app --url

# Expected: http://192.168.49.2:30080

# Open in browser
open $(minikube service frontend -n blog-app --url)

# Or curl
curl $(minikube service frontend -n blog-app --url)
```

---

## 🧪 Testing

### Frontend
```bash
# Get frontend URL
minikube service frontend -n blog-app --url

# Test homepage
curl http://<minikube-ip>:30080

# Expected: HTML with "Blog App on Kubernetes"
```

### Backend API
```bash
# Test backend from within cluster
kubectl run test -n blog-app --image=busybox --rm -it -- sh

# Inside test pod:
wget -qO- backend:8080

# Expected:
# {
#   "message": "Backend API running",
#   "hostname": "backend-xxx-xxx",
#   "timestamp": "2026-02-21T..."
# }
```

### Database
```bash
# Connect to PostgreSQL
kubectl exec -it -n blog-app deployment/postgres -- psql -U bloguser -d blogdb

# Inside psql:
# \dt        -- List tables
# \l         -- List databases
# \q         -- Quit
```

### Service Discovery
```bash
# Test DNS resolution
kubectl run test -n blog-app --image=busybox --rm -it -- sh

# Inside pod:
nslookup backend
nslookup postgres
nslookup frontend

# Expected: All resolve to ClusterIP addresses
```

---

## 📊 Monitoring

### View Logs
```bash
# Frontend logs
kubectl logs -n blog-app deployment/frontend

# Backend logs
kubectl logs -n blog-app deployment/backend -f

# Database logs
kubectl logs -n blog-app deployment/postgres

# All Pods with label
kubectl logs -n blog-app -l app=backend
```

### Resource Usage
```bash
# Pod resource usage (requires metrics-server)
kubectl top pods -n blog-app

# Node usage
kubectl top nodes
```

### Events
```bash
# Namespace events
kubectl get events -n blog-app --sort-by='.lastTimestamp'

# Watch events
kubectl get events -n blog-app -w
```

---

## 🔧 Management

### Scaling

**Scale Frontend:**
```bash
# Scale to 3 replicas
kubectl scale deployment frontend -n blog-app --replicas=3

# Verify
kubectl get pods -n blog-app -l app=frontend

# Scale back to 2
kubectl scale deployment frontend -n blog-app --replicas=2
```

**Scale Backend:**
```bash
# Scale to 5 replicas
kubectl scale deployment backend -n blog-app --replicas=5

# Watch scaling
kubectl get pods -n blog-app -w
```

### Updates

**Update Frontend Image:**
```bash
# Update to newer nginx
kubectl set image deployment/frontend -n blog-app \
  nginx=nginx:1.26-alpine

# Watch rollout
kubectl rollout status deployment/frontend -n blog-app

# Check history
kubectl rollout history deployment/frontend -n blog-app
```

**Rollback:**
```bash
# Rollback frontend
kubectl rollout undo deployment/frontend -n blog-app

# Rollback to specific revision
kubectl rollout undo deployment/frontend -n blog-app --to-revision=1
```

### Debugging

**Pod not starting:**
```bash
# Describe pod
kubectl describe pod <pod-name> -n blog-app

# Check logs
kubectl logs <pod-name> -n blog-app

# Check events
kubectl get events -n blog-app | grep <pod-name>
```

**Service not accessible:**
```bash
# Check service
kubectl get svc frontend -n blog-app

# Check endpoints
kubectl get endpoints frontend -n blog-app

# If no endpoints:
# 1. Check selector matches pod labels
kubectl describe svc frontend -n blog-app
kubectl get pods -n blog-app --show-labels
```

**Container errors:**
```bash
# Interactive debugging
kubectl exec -it -n blog-app deployment/backend -- sh

# Inside container:
# env              -- Check environment variables
# ls /app          -- Check files
# ps aux           -- Check processes
# netstat -tlnp    -- Check ports
```

---

## 🛠️ Customization

### Change NodePort

Edit `manifests/frontend.yaml`:
```yaml
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 80
    nodePort: 31000  # Change this (30000-32767)
```

Apply:
```bash
kubectl apply -f manifests/frontend.yaml
```

### Add Environment Variables

Edit `manifests/backend.yaml`:
```yaml
env:
- name: DB_HOST
  value: postgres
- name: LOG_LEVEL      # Add this
  value: debug         # Add this
- name: API_VERSION    # Add this
  value: v1            # Add this
```

Apply and restart:
```bash
kubectl apply -f manifests/backend.yaml
kubectl rollout restart deployment/backend -n blog-app
```

### Change Resource Limits

Edit any deployment manifest:
```yaml
resources:
  requests:
    memory: "256Mi"    # Increase this
    cpu: "200m"        # Increase this
  limits:
    memory: "512Mi"    # Increase this
    cpu: "500m"        # Increase this
```

---

## 🧹 Cleanup

### Delete Application
```bash
# Delete all resources
kubectl delete -f manifests/

# Or delete namespace (deletes everything inside)
kubectl delete namespace blog-app

# Verify deletion
kubectl get all -n blog-app
# Expected: No resources found
```

### Stop Minikube
```bash
# Stop cluster (keeps data)
minikube stop

# Delete cluster (removes everything)
minikube delete
```

---

## 📁 Project Structure

```
k8s-blog-app/
├── README.md                 # This file
└── manifests/
    ├── namespace.yaml        # blog-app namespace
    ├── database.yaml         # PostgreSQL deployment + service
    ├── backend.yaml          # Node.js API deployment + service
    └── frontend.yaml         # Nginx deployment + NodePort service
```

---

## 📚 Learning Outcomes

After completing this project, you understand:

### Kubernetes Basics:
- ✅ How to create namespaces for resource isolation
- ✅ Deployments for managing application lifecycle
- ✅ ReplicaSets for maintaining desired Pod count
- ✅ Services for exposing applications
- ✅ Service types (ClusterIP vs NodePort)

### Service Discovery:
- ✅ DNS-based service discovery (service-name works within cluster)
- ✅ How Services load balance across Pods
- ✅ Endpoints and how they track Pods

### Scaling:
- ✅ Horizontal scaling (add more Pods)
- ✅ kubectl scale command
- ✅ Auto-healing (Pods recreated when deleted)

### Updates:
- ✅ Rolling updates with zero downtime
- ✅ Rollout history tracking
- ✅ Rollback capability

---

## 🎯 Interview Questions You Can Answer

**1. "How do you deploy an application to Kubernetes?"**
- Create Deployment with desired replicas
- Define Pod template (image, ports, resources)
- Apply with kubectl
- Kubernetes schedules Pods on nodes

**2. "How do Services work in Kubernetes?"**
- Service selects Pods using labels
- Creates stable endpoint (ClusterIP)
- Load balances traffic across Pods
- DNS name for service discovery

**3. "What's the difference between ClusterIP and NodePort?"**
- ClusterIP: Internal only, default type
- NodePort: External access via Node:Port
- LoadBalancer: Cloud provider LB (production)

**4. "How do you scale an application?"**
- kubectl scale deployment <name> --replicas=N
- Or edit deployment.yaml and reapply
- Kubernetes creates/deletes Pods to match

**5. "How do you troubleshoot a Pod that won't start?"**
- kubectl describe pod - check events
- kubectl logs pod - check application logs
- kubectl get events - cluster events
- Check resources, image, node status

---

## 🚀 Next Steps

**Extend this project:**

1. **Add Persistent Storage (Day 7):**
   - Use PersistentVolume for database
   - Data survives Pod restarts

2. **Add ConfigMaps:**
   - Externalize configuration
   - Config files as volumes

3. **Add Secrets:**
   - Store database password
   - Mount as environment variables

4. **Add Ingress (Day 7):**
   - Replace NodePort with Ingress
   - Path-based routing

5. **Add Health Checks:**
   - Liveness probes (restart if unhealthy)
   - Readiness probes (remove from service if not ready)

6. **Use Helm (Day 7):**
   - Package application as Helm chart
   - Templating and versioning

---

## 💡 Best Practices Demonstrated

- ✅ **Namespaces:** Resource isolation and organization
- ✅ **Labels:** Organize and select resources
- ✅ **Declarative YAML:** Version-controlled manifests
- ✅ **Multiple Replicas:** High availability
- ✅ **Resource Requests:** Proper scheduling
- ✅ **ClusterIP for Internal:** Backend/DB not exposed externally
- ✅ **Descriptive Names:** Clear resource naming

---

## 🆘 Troubleshooting Guide

### Issue: Pods in Pending state

**Symptoms:**
```bash
kubectl get pods -n blog-app
# NAME              READY   STATUS    RESTARTS   AGE
# frontend-xxx      0/1     Pending   0          1m
```

**Diagnosis:**
```bash
kubectl describe pod frontend-xxx -n blog-app
# Look for: Insufficient cpu, Insufficient memory
```

**Solution:**
- Free up resources: `kubectl delete pod <other-pod>`
- Increase Minikube resources: `minikube delete && minikube start --cpus=4 --memory=8192`

---

### Issue: Service has no endpoints

**Symptoms:**
```bash
kubectl get endpoints frontend -n blog-app
# NAME       ENDPOINTS   AGE
# frontend   <none>      1m
```

**Diagnosis:**
```bash
# Check service selector
kubectl describe svc frontend -n blog-app

# Check pod labels
kubectl get pods -n blog-app --show-labels
```

**Solution:**
- Ensure service selector matches pod labels exactly
- Example: If service has `app: frontend`, pods must have same label

---

### Issue: Cannot access NodePort

**Symptoms:**
- Browser shows "connection refused"
- curl times out

**Diagnosis:**
```bash
# Check service type
kubectl get svc frontend -n blog-app

# Get Minikube IP
minikube ip

# Check port
kubectl get svc frontend -n blog-app -o jsonpath='{.spec.ports[0].nodePort}'
```

**Solution:**
- Use correct URL: `http://<minikube-ip>:<nodePort>`
- For Minikube: `minikube service frontend -n blog-app --url`
- Check firewall/VPN not blocking

---

## 📈 Real-World Applications

This architecture pattern is used in:

- **Microservices:** Each service as separate Deployment
- **12-Factor Apps:** Stateless frontend/backend, data in DB
- **Dev/Staging/Prod:** Same manifests, different namespaces
- **SaaS Platforms:** Multi-tenant with namespace isolation

**Companies using similar patterns:**
- Spotify (microservices on K8s)
- Airbnb (namespaces for environments)
- Uber (service mesh over K8s)
- Netflix (hundreds of microservices)

---

## 🎉 Congratulations!

You've deployed your first multi-tier application to Kubernetes! 🚀

**Skills demonstrated:**
- ✅ Kubernetes cluster usage
- ✅ Declarative configuration
- ✅ Service discovery
- ✅ Load balancing
- ✅ Scaling
- ✅ Troubleshooting

**Resume-worthy! 💼**

---

**Built by DevOps learners for DevOps learners! 🎯**
