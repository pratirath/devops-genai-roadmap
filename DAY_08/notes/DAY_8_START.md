# Day 8 Quick Start Guide

**🚀 Get started with Advanced Kubernetes in 30 minutes!**

---

## ⚡ Pre-Flight Check (5 minutes)

```bash
# 1. Verify Kubernetes cluster
kubectl version --short
kubectl get nodes
# ✅ Should show your cluster nodes

# 2. Check Day 6 cleanup
kubectl get all --all-namespaces
# 🧹 Clean up old resources if needed

# 3. Check available storage
kubectl get pv
kubectl get pvc --all-namespaces
# 📦 Note: We'll create new storage today
```

---

## 🛠️ Essential Setup (10 minutes)

### **1. Install Helm (2 minutes)**
```bash
# macOS
brew install helm

# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Windows (PowerShell as Admin)
choco install kubernetes-helm

# Verify
helm version
# ✅ Version 3.x or higher
```

### **2. Add Helm Repositories (2 minutes)**
```bash
# Add popular repos
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add stable https://charts.helm.sh/stable
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# Update
helm repo update

# Search test
helm search repo wordpress
# ✅ Should show WordPress charts
```

### **3. Enable Ingress (3 minutes)**
```bash
# Minikube
minikube addons enable ingress

# Verify ingress controller
kubectl get pods -n ingress-nginx
# ✅ Wait for ingress-nginx-controller pod to be Running

# For other K8s (kind, k3s, cloud):
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml

# Wait for ready
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=120s
```

### **4. Create Working Directory (1 minute)**
```bash
cd ~/Prathiksa/Python_Practice/24Nov/Devops_Roadmap/DAY_08
mkdir -p manifests/{statefulset,helm,ingress,production}
cd manifests
```

---

## 🎯 Quick Wins (15 minutes)

### **Quick Win 1: Deploy WordPress with Helm (5 minutes)**

```bash
# Install WordPress (one command!)
helm install my-wordpress bitnami/wordpress \
  --set service.type=NodePort \
  --set wordpressUsername=admin \
  --set wordpressPassword=admin123

# Watch deployment
kubectl get pods -w
# Press Ctrl+C when wordpress pod is Running

# Get WordPress URL
echo "WordPress URL: http://$(minikube ip):$(kubectl get svc my-wordpress -o jsonpath='{.spec.ports[0].nodePort}')"

# Or use minikube service
minikube service my-wordpress --url

# Login credentials:
echo "Username: admin"
echo "Password: admin123"

# 🎉 Success! You deployed WordPress in 30 seconds!

# Cleanup
helm uninstall my-wordpress
```

**What you learned:** Helm can deploy complex apps with one command!

---

### **Quick Win 2: StatefulSet with Persistent Storage (5 minutes)**

```bash
cd ~/Prathiksa/Python_Practice/24Nov/Devops_Roadmap/DAY_08/manifests/statefulset

# Create quick MySQL StatefulSet
cat > mysql-quick.yaml <<'EOF'
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  ports:
  - port: 3306
  clusterIP: None
  selector:
    app: mysql
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: mysql
  replicas: 2
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
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: "password123"
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
EOF

# Deploy
kubectl apply -f mysql-quick.yaml

# Watch pods created IN ORDER
kubectl get pods -w
# You'll see: mysql-0 (Running) → mysql-1 (Creating)

# Check PVCs (auto-created)
kubectl get pvc
# data-mysql-0, data-mysql-1

# 🎉 Success! StatefulSet with persistent storage!

# Cleanup
kubectl delete -f mysql-quick.yaml
kubectl delete pvc --all
```

**What you learned:** StatefulSets create ordered pods with persistent storage!

---

### **Quick Win 3: Ingress Routing (5 minutes)**

```bash
cd ~/Prathiksa/Python_Practice/24Nov/Devops_Roadmap/DAY_08/manifests/ingress

# Create 2 apps + Ingress
cat > ingress-quick.yaml <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: app1
  labels:
    app: app1
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    command: ["/bin/sh", "-c"]
    args:
      - echo "<h1>App 1</h1>" > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'
---
apiVersion: v1
kind: Service
metadata:
  name: app1-svc
spec:
  selector:
    app: app1
  ports:
  - port: 80
---
apiVersion: v1
kind: Pod
metadata:
  name: app2
  labels:
    app: app2
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    command: ["/bin/sh", "-c"]
    args:
      - echo "<h1>App 2</h1>" > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'
---
apiVersion: v1
kind: Service
metadata:
  name: app2-svc
spec:
  selector:
    app: app2
  ports:
  - port: 80
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-app
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: myapps.local
    http:
      paths:
      - path: /app1
        pathType: Prefix
        backend:
          service:
            name: app1-svc
            port:
              number: 80
      - path: /app2
        pathType: Prefix
        backend:
          service:
            name: app2-svc
            port:
              number: 80
EOF

# Deploy
kubectl apply -f ingress-quick.yaml

# Add to /etc/hosts
echo "$(minikube ip) myapps.local" | sudo tee -a /etc/hosts

# Test routing
curl http://myapps.local/app1
# Output: <h1>App 1</h1>

curl http://myapps.local/app2
# Output: <h1>App 2</h1>

# 🎉 Success! One Ingress routing to two apps!

# Cleanup
kubectl delete -f ingress-quick.yaml
sudo sed -i '' '/myapps.local/d' /etc/hosts
```

**What you learned:** Ingress can route to multiple services from one entry point!

---

## 📚 What's Next?

### **Follow the Full Day 8 Plan:**

1. **Morning (3 hours):**
   - Read `DAY_8_PLAN.md` Sessions 1-3
   - Complete MySQL StatefulSet project
   - Create custom Helm chart

2. **Afternoon (3 hours):**
   - Read `DAY_8_PLAN.md` Sessions 4-6
   - Set up advanced Ingress routing
   - Work with ConfigMaps & Secrets

3. **Evening (2 hours):**
   - Read `DAY_8_PLAN.md` Sessions 7-8
   - Deploy production WordPress stack
   - Implement best practices

### **Projects in `/projects/README.md`:**
- [ ] Project 1: MySQL StatefulSet (45 min)
- [ ] Project 2: Custom Helm Chart (1 hour)
- [ ] Project 3: Multi-App Ingress (1 hour)
- [ ] Project 4: WordPress Stack (2 hours) ⭐ Capstone

### **Take Notes:**
Use `/notes/day-08-notes.md` to document:
- Commands that worked
- Errors you encountered
- Solutions you found
- Key learnings

---

## 🎯 Success Metrics

By end of today, you should have:
- ✅ Helm installed and used
- ✅ 2+ StatefulSets deployed
- ✅ Persistent storage working
- ✅ Ingress routing configured
- ✅ 1 production-ready application

**Time:** 8 hours  
**Skills:** 10+ advanced K8s concepts  
**Career Impact:** +₹5-8 LPA  

---

## 🆘 Quick Troubleshooting

### **Helm not found:**
```bash
# macOS
brew install helm

# Verify PATH
echo $PATH | grep -o '/usr/local/bin'
```

### **Ingress not working:**
```bash
# Check ingress controller
kubectl get pods -n ingress-nginx

# If not running, re-enable
minikube addons disable ingress
minikube addons enable ingress
```

### **Pods stuck in Pending (PVC issue):**
```bash
# Check PVCs
kubectl get pvc

# Check PVs
kubectl get pv

# For Minikube, ensure provisioner available
minikube addons enable storage-provisioner
minikube addons enable default-storageclass
```

### **Can't access via minikube ip:**
```bash
# Get IP
minikube ip

# Test connectivity
ping $(minikube ip)

# If using Docker driver, may need tunnel
minikube service <service-name> --url
```

### **Clean slate (if things are broken):**
```bash
# Delete all resources
kubectl delete all --all
kubectl delete pvc --all

# Or restart Minikube
minikube stop
minikube delete
minikube start
```

---

## 📖 Essential Commands Reference

### **Helm:**
```bash
helm search repo <keyword>      # Search charts
helm install <name> <chart>     # Install
helm list                       # List releases
helm upgrade <name> <chart>     # Upgrade
helm rollback <name>            # Rollback
helm uninstall <name>           # Uninstall
```

### **StatefulSets:**
```bash
kubectl get statefulset         # List
kubectl scale sts <name> --replicas=N  # Scale
kubectl delete sts <name>       # Delete
```

### **PV/PVC:**
```bash
kubectl get pv                  # List volumes
kubectl get pvc                 # List claims
kubectl describe pvc <name>     # Details
kubectl delete pvc <name>       # Delete
```

### **Ingress:**
```bash
kubectl get ingress             # List
kubectl describe ingress <name> # Details
kubectl logs -n ingress-nginx <pod>  # Controller logs
```

---

## ✅ Quick Start Complete!

You now have:
- ✅ Helm installed and tested
- ✅ Ingress controller ready
- ✅ 3 quick wins completed
- ✅ Understanding of key concepts

**Next Step:** Open `DAY_8_PLAN.md` and start Session 1! 🚀

---

**Questions?** Check `/docs/DAY_8_PLAN.md` or `README.md`  
**Issues?** See troubleshooting section above  
**Ready?** Let's master Advanced Kubernetes! 💪
