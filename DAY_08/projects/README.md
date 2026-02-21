# Day 8 Projects - Advanced Kubernetes

**Focus:** Hands-on production-ready Kubernetes deployments  
**Difficulty:** Medium to Advanced  
**Time Required:** 4-5 hours total  

---

## 📋 Project Overview

Today's projects build production skills:
1. **StatefulSet MySQL Cluster** - Database with persistent storage
2. **Helm-Packaged Application** - Create custom Helm chart
3. **Multi-App Ingress** - Advanced routing scenarios
4. **Production WordPress Stack** - Complete 3-tier application

---

## 🎯 Project 1: MySQL StatefulSet with Persistent Storage

### **Objective:**
Deploy a 3-node MySQL cluster using StatefulSet with persistent volumes

### **Learning Goals:**
- ✅ Understand StatefulSet pod naming
- ✅ Configure persistent storage per pod
- ✅ Use headless services
- ✅ Test data persistence
- ✅ Practice ordered scaling

### **Architecture:**
```
Headless Service (mysql-headless)
    ↓
StatefulSet: mysql-0, mysql-1, mysql-2
    ↓
PVCs: mysql-data-mysql-0, mysql-data-mysql-1, mysql-data-mysql-2
    ↓
PVs: 10Gi each
```

### **Files to Create:**

**1. Namespace:**
```yaml
# 01-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: mysql-cluster
```

**2. Headless Service:**
```yaml
# 02-headless-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql-headless
  namespace: mysql-cluster
spec:
  ports:
  - port: 3306
    name: mysql
  clusterIP: None
  selector:
    app: mysql
```

**3. StatefulSet:**
```yaml
# 03-mysql-statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
  namespace: mysql-cluster
spec:
  serviceName: mysql-headless
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        ports:
        - containerPort: 3306
          name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: "rootpass123"
        - name: MYSQL_DATABASE
          value: "testdb"
        volumeMounts:
        - name: mysql-data
          mountPath: /var/lib/mysql
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
  volumeClaimTemplates:
  - metadata:
      name: mysql-data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

### **Deployment Steps:**
```bash
# 1. Create resources
kubectl apply -f 01-namespace.yaml
kubectl apply -f 02-headless-service.yaml
kubectl apply -f 03-mysql-statefulset.yaml

# 2. Watch pods being created in ORDER
kubectl get pods -n mysql-cluster -w
# You'll see: mysql-0 → mysql-1 → mysql-2

# 3. Check PVCs (automatically created)
kubectl get pvc -n mysql-cluster
# mysql-data-mysql-0, mysql-data-mysql-1, mysql-data-mysql-2

# 4. Check PVs
kubectl get pv
```

### **Testing Persistence:**
```bash
# 1. Connect to mysql-0
kubectl exec -it mysql-0 -n mysql-cluster -- mysql -uroot -prootpass123

# 2. Inside MySQL:
CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100));
INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob');
SELECT * FROM users;
exit

# 3. Delete the pod
kubectl delete pod mysql-0 -n mysql-cluster

# 4. Wait for pod to recreate (watch)
kubectl get pods -n mysql-cluster -w

# 5. Reconnect and verify data
kubectl exec -it mysql-0 -n mysql-cluster -- mysql -uroot -prootpass123 -e "USE testdb; SELECT * FROM users;"
# Data should still be there! ✅
```

### **Testing Ordered Scaling:**
```bash
# Scale down (from 3 to 1)
kubectl scale statefulset mysql --replicas=1 -n mysql-cluster
kubectl get pods -n mysql-cluster -w
# Deletes in REVERSE: mysql-2 → mysql-1 (mysql-0 remains)

# Scale up (from 1 to 5)
kubectl scale statefulset mysql --replicas=5 -n mysql-cluster
kubectl get pods -n mysql-cluster -w
# Creates in ORDER: mysql-1 → mysql-2 → mysql-3 → mysql-4
```

### **Cleanup:**
```bash
kubectl delete namespace mysql-cluster
# This deletes namespace, statefulset, pods, services
# PVCs are deleted, but PVs might remain (check reclaim policy)
kubectl get pv  # Verify cleanup
```

### **Success Criteria:**
- [ ] 3 MySQL pods running with unique names
- [ ] 3 PVCs created automatically
- [ ] Data persists after pod deletion
- [ ] Pods scale in order (0→1→2)
- [ ] Each pod has own storage

### **Resume Bullet:**
> "Deployed highly available MySQL cluster on Kubernetes using StatefulSets with persistent storage and ordered scaling"

---

## 🎯 Project 2: Custom Helm Chart for Node.js App

### **Objective:**
Create a reusable Helm chart for deploying Node.js applications

### **Learning Goals:**
- ✅ Understand Helm chart structure
- ✅ Use templates and values
- ✅ Create ConfigMaps from Helm
- ✅ Parameterize deployments
- ✅ Install and upgrade releases

### **Step 1: Create Chart Structure**
```bash
# Create new chart
helm create nodejs-app

# Chart structure:
# nodejs-app/
# ├── Chart.yaml          # Chart metadata
# ├── values.yaml         # Default configuration
# ├── templates/
# │   ├── deployment.yaml
# │   ├── service.yaml
# │   ├── ingress.yaml
# │   └── configmap.yaml
# └── charts/             # Dependencies

cd nodejs-app
```

### **Step 2: Edit Chart.yaml**
```yaml
# Chart.yaml
apiVersion: v2
name: nodejs-app
description: A Helm chart for Node.js applications
type: application
version: 0.1.0
appVersion: "1.0.0"
maintainers:
  - name: Your Name
    email: your.email@example.com
```

### **Step 3: Edit values.yaml**
```yaml
# values.yaml
replicaCount: 2

image:
  repository: node
  tag: "18-alpine"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 3000

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: nodejs-app.local
      paths:
        - path: /
          pathType: Prefix
  tls: []

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

config:
  nodeEnv: production
  appPort: 3000
  logLevel: info

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
```

### **Step 4: Create ConfigMap Template**
```yaml
# templates/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "nodejs-app.fullname" . }}-config
  labels:
    {{- include "nodejs-app.labels" . | nindent 4 }}
data:
  NODE_ENV: {{ .Values.config.nodeEnv | quote }}
  APP_PORT: {{ .Values.config.appPort | quote }}
  LOG_LEVEL: {{ .Values.config.logLevel | quote }}
```

### **Step 5: Update Deployment Template**
```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "nodejs-app.fullname" . }}
  labels:
    {{- include "nodejs-app.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "nodejs-app.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "nodejs-app.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
        ports:
        - name: http
          containerPort: {{ .Values.service.port }}
          protocol: TCP
        envFrom:
        - configMapRef:
            name: {{ include "nodejs-app.fullname" . }}-config
        livenessProbe:
          httpGet:
            path: /health
            port: http
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: http
          initialDelaySeconds: 5
          periodSeconds: 5
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
```

### **Step 6: Create HPA Template**
```yaml
# templates/hpa.yaml
{{- if .Values.autoscaling.enabled }}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: {{ include "nodejs-app.fullname" . }}
  labels:
    {{- include "nodejs-app.labels" . | nindent 4 }}
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {{ include "nodejs-app.fullname" . }}
  minReplicas: {{ .Values.autoscaling.minReplicas }}
  maxReplicas: {{ .Values.autoscaling.maxReplicas }}
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: {{ .Values.autoscaling.targetCPUUtilizationPercentage }}
{{- end }}
```

### **Step 7: Install Chart**
```bash
# From parent directory
# Lint chart (check for errors)
helm lint nodejs-app

# Dry run (see what would be created)
helm install my-nodejs-app nodejs-app --dry-run --debug

# Install chart
helm install my-nodejs-app nodejs-app

# Check release
helm list
kubectl get all -l app.kubernetes.io/instance=my-nodejs-app

# Get ConfigMap
kubectl get configmap
kubectl describe configmap my-nodejs-app-nodejs-app-config
```

### **Step 8: Upgrade Chart**
```bash
# Change values
helm upgrade my-nodejs-app nodejs-app \
  --set replicaCount=3 \
  --set config.nodeEnv=staging

# Or create custom values file
cat > custom-values.yaml <<EOF
replicaCount: 5
config:
  nodeEnv: development
  logLevel: debug
ingress:
  hosts:
    - host: dev.nodejs-app.local
      paths:
        - path: /
          pathType: Prefix
EOF

helm upgrade my-nodejs-app nodejs-app -f custom-values.yaml

# Check revision history
helm history my-nodejs-app
```

### **Step 9: Rollback**
```bash
# Rollback to previous version
helm rollback my-nodejs-app

# Or specific revision
helm rollback my-nodejs-app 1
```

### **Step 10: Package Chart**
```bash
# Package for distribution
helm package nodejs-app
# Creates: nodejs-app-0.1.0.tgz

# Install from package
helm install another-release nodejs-app-0.1.0.tgz
```

### **Cleanup:**
```bash
helm uninstall my-nodejs-app
```

### **Success Criteria:**
- [ ] Helm chart created with proper structure
- [ ] Templates use values from values.yaml
- [ ] ConfigMap created from Helm
- [ ] Deployment parameterized
- [ ] Autoscaling configured
- [ ] Can install/upgrade/rollback
- [ ] Chart packaged successfully

### **Resume Bullet:**
> "Created reusable Helm charts with templating, parameterization, and automated deployments for Node.js applications"

---

## 🎯 Project 3: Multi-App Ingress Routing

### **Objective:**
Deploy multiple applications with advanced Ingress routing (path-based and host-based)

### **Learning Goals:**
- ✅ Path-based routing (/app1, /app2)
- ✅ Host-based routing (app1.local, app2.local)
- ✅ TLS/HTTPS configuration
- ✅ Ingress annotations
- ✅ URL rewriting

### **Architecture:**
```
Internet
    ↓
Ingress (Nginx)
    ├─ myapp.local/app1 → App1 Service → App1 Pods
    ├─ myapp.local/app2 → App2 Service → App2 Pods
    ├─ app1.local → App1 Service → App1 Pods
    └─ app2.local → App2 Service → App2 Pods
```

### **Prerequisites:**
```bash
# Enable Ingress (Minikube)
minikube addons enable ingress

# Verify
kubectl get pods -n ingress-nginx
```

### **Complete Project Files:**

See the detailed Ingress setup in `DAY_8_PLAN.md` Session 4.

Key files:
- `app1-deployment.yaml`
- `app2-deployment.yaml`
- `ingress.yaml`
- `ingress-tls.yaml`

### **Testing:**
```bash
# Add to /etc/hosts
echo "$(minikube ip) myapp.local app1.local app2.local" | sudo tee -a /etc/hosts

# Test path-based
curl http://myapp.local/app1
curl http://myapp.local/app2

# Test host-based
curl http://app1.local
curl http://app2.local

# Test HTTPS (after TLS setup)
curl -k https://myapp.local
```

### **Success Criteria:**
- [ ] Two apps deployed
- [ ] Path-based routing working
- [ ] Host-based routing working
- [ ] TLS certificate created
- [ ] HTTPS working
- [ ] All routes accessible

### **Resume Bullet:**
> "Configured Nginx Ingress controller with path and host-based routing, TLS termination for multi-tenant Kubernetes applications"

---

## 🎯 Project 4: Production WordPress Stack (CAPSTONE)

### **Objective:**
Deploy complete production-ready WordPress application with MySQL, Redis, Ingress, and all best practices

### **Learning Goals:**
- ✅ Multi-tier application deployment
- ✅ StatefulSet for database
- ✅ Caching layer (Redis)
- ✅ Secrets management
- ✅ ConfigMaps
- ✅ Resource limits
- ✅ Health probes
- ✅ Ingress with TLS
- ✅ Horizontal autoscaling

### **Architecture:**
```
Internet (HTTPS)
    ↓
Ingress (wordpress.local)
    ↓
WordPress Service (ClusterIP)
    ↓
WordPress Deployment (2 replicas, autoscale 2-10)
    ├─ Resources: 256Mi-512Mi, 250m-500m CPU
    ├─ Health: Liveness & Readiness probes
    ├─ Config: From ConfigMap
    └─ Secrets: From Secret
    ↓
    ├──→ MySQL StatefulSet (1 replica)
    │    ├─ Persistent Volume (10Gi)
    │    ├─ Resources: 512Mi-1Gi, 500m-1000m CPU
    │    └─ Health probes
    │
    └──→ Redis Deployment (1 replica)
         ├─ For object caching
         └─ Resources: 128Mi-256Mi, 100m-200m CPU
```

### **Complete Deployment:**

See detailed WordPress stack deployment in `DAY_8_PLAN.md` Session 7.

8 files total:
1. `01-namespace.yaml`
2. `02-storageclass.yaml`
3. `03-secrets.yaml`
4. `04-configmap.yaml`
5. `05-mysql-statefulset.yaml`
6. `06-redis-deployment.yaml`
7. `07-wordpress-deployment.yaml`
8. `08-ingress.yaml`

### **Deployment Commands:**
```bash
# Deploy all (in order)
kubectl apply -f 01-namespace.yaml
kubectl apply -f 02-storageclass.yaml
kubectl apply -f 03-secrets.yaml
kubectl apply -f 04-configmap.yaml
kubectl apply -f 05-mysql-statefulset.yaml
kubectl apply -f 06-redis-deployment.yaml
kubectl apply -f 07-wordpress-deployment.yaml
kubectl apply -f 08-ingress.yaml

# Or use loop
for i in {01..08}; do
  kubectl apply -f 0$i-*.yaml
done

# Watch everything
kubectl get all -n wordpress-prod -w
```

### **Add to /etc/hosts:**
```bash
echo "$(minikube ip) wordpress.local" | sudo tee -a /etc/hosts
```

### **Access WordPress:**
```bash
# Open in browser
open http://wordpress.local

# Get admin credentials
kubectl get secret wordpress-secret -n wordpress-prod -o jsonpath='{.data.wp-admin-user}' | base64 -d
kubectl get secret wordpress-secret -n wordpress-prod -o jsonpath='{.data.wp-admin-password}' | base64 -d
```

### **Testing Checklist:**

**1. Database Connectivity:**
```bash
# Check MySQL pod
kubectl get pods -n wordpress-prod | grep mysql

# Connect to MySQL
kubectl exec -it mysql-0 -n wordpress-prod -- mysql -uroot -prootpass123 -e "SHOW DATABASES;"

# Should see 'wordpress' database
```

**2. Data Persistence:**
```bash
# Create a WordPress post
# Go to: http://wordpress.local/wp-admin
# Create a post

# Delete WordPress pod
kubectl delete pod -n wordpress-prod -l app=wordpress

# Wait for new pod
kubectl get pods -n wordpress-prod -w

# Refresh browser - post should still be there! ✅
```

**3. Redis Caching:**
```bash
# Check Redis connection
kubectl exec -it -n wordpress-prod deployment/redis -- redis-cli PING
# Should return: PONG

# Install Redis Object Cache plugin in WordPress
# Admin → Plugins → Add New → "Redis Object Cache"
# Install and activate
# Settings → Redis → Enable Object Cache

# Verify cache hits
kubectl exec -it -n wordpress-prod deployment/redis -- redis-cli INFO stats
# Look for: keyspace_hits
```

**4. Autoscaling:**
```bash
# Check HPA
kubectl get hpa -n wordpress-prod

# Generate load (optional)
kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh
# while sleep 0.01; do wget -q -O- http://wordpress.wordpress-prod; done

# Watch pods scale up
kubectl get pods -n wordpress-prod -w
```

**5. Resource Monitoring:**
```bash
# Check resource usage
kubectl top pods -n wordpress-prod

# Check events
kubectl get events -n wordpress-prod --sort-by='.lastTimestamp'
```

### **Production Enhancements:**

**1. Add PodDisruptionBudget:**
```yaml
# pdb.yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: wordpress-pdb
  namespace: wordpress-prod
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: wordpress
```

**2. Add NetworkPolicy:**
```yaml
# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: mysql-network-policy
  namespace: wordpress-prod
spec:
  podSelector:
    matchLabels:
      app: mysql
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: wordpress
    ports:
    - protocol: TCP
      port: 3306
```

**3. Add Resource Quotas:**
```yaml
# quota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: wordpress-quota
  namespace: wordpress-prod
spec:
  hard:
    requests.cpu: "4"
    requests.memory: "8Gi"
    limits.cpu: "8"
    limits.memory: "16Gi"
    persistentvolumeclaims: "5"
```

### **Cleanup:**
```bash
# Delete namespace (removes everything)
kubectl delete namespace wordpress-prod

# Verify PVs cleaned up
kubectl get pv
# Manually delete if needed
kubectl delete pv <pv-name>

# Remove from /etc/hosts
sudo sed -i '' '/wordpress.local/d' /etc/hosts
```

### **Success Criteria:**
- [ ] All pods running (WordPress, MySQL, Redis)
- [ ] WordPress accessible via Ingress
- [ ] Database connection working
- [ ] Data persists after pod restarts
- [ ] Redis caching enabled
- [ ] Resource limits set
- [ ] Health probes working
- [ ] Autoscaling configured
- [ ] TLS/HTTPS working (optional)
- [ ] Can create posts and they persist

### **Documentation:**

Create `ARCHITECTURE.md`:
```markdown
# WordPress on Kubernetes - Architecture

## Overview
Production-grade WordPress deployment on Kubernetes

## Components
1. **WordPress** (2 replicas, autoscale to 10)
2. **MySQL** (1 replica StatefulSet, 10Gi persistent storage)
3. **Redis** (1 replica, object cache)
4. **Ingress** (Nginx, HTTP routing)

## Resource Allocation
- Total CPU: ~2 cores
- Total Memory: ~3GB
- Total Storage: 30GB (10GB MySQL + 10GB WordPress + overhead)

## High Availability
- WordPress: 2+ replicas
- MySQL: StatefulSet with persistent storage
- Redis: Can be scaled if needed

## Security
- Secrets for passwords
- ConfigMaps for config
- NetworkPolicies (optional)

## Monitoring
- Health probes on all pods
- Resource limits enforced
- HPA for auto-scaling

## Cost Estimate (AWS)
- 2x t3.medium nodes: ~$60/month
- 30GB EBS: ~$3/month
- Load Balancer: ~$20/month
**Total: ~$83/month**
```

### **Resume Bullets:**
> "Deployed production-grade multi-tier WordPress application on Kubernetes with StatefulSet MySQL, Redis caching, Nginx Ingress, autoscaling, and comprehensive monitoring"

> "Implemented DevOps best practices including resource quotas, pod disruption budgets, network policies, and persistent storage for Kubernetes applications"

> "Achieved 99.9% uptime with horizontal pod autoscaling, health probes, and automated failover for stateful workloads"

---

## 📊 Projects Summary

| Project | Difficulty | Time | Resume Value | Key Skills |
|---------|-----------|------|--------------|-----------|
| 1. MySQL StatefulSet | Medium | 45 min | ⭐⭐⭐⭐ | StatefulSets, PV/PVC |
| 2. Custom Helm Chart | Medium | 1 hour | ⭐⭐⭐⭐⭐ | Helm, Templating |
| 3. Multi-App Ingress | Medium | 1 hour | ⭐⭐⭐⭐ | Ingress, Routing, TLS |
| 4. WordPress Stack | Advanced | 2 hours | ⭐⭐⭐⭐⭐ | All Day 8 concepts |

**Total Time:** ~5 hours  
**Total Skills:** 15+ production concepts  
**Salary Impact:** +₹8-12 LPA (with all projects)  

---

## ✅ Completion Checklist

- [ ] Project 1: MySQL StatefulSet completed
- [ ] Project 2: Custom Helm chart created
- [ ] Project 3: Multi-app Ingress working
- [ ] Project 4: WordPress stack deployed
- [ ] All code committed to GitHub
- [ ] Architecture diagrams created
- [ ] README files updated
- [ ] Screenshots taken
- [ ] Portfolio updated with projects

---

**🎯 Complete all 4 projects to unlock maximum learning and career impact! 🚀**
