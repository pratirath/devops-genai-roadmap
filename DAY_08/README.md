# Day 8: Advanced Kubernetes - Production-Ready Orchestration

**Progress:** 40% of 30-Day DevOps Roadmap  
**Date:** February 22, 2026  
**Status:** 🚀 Ready to Start  
**Duration:** 8 hours  

---

## 📌 Quick Overview

Today you'll master advanced Kubernetes concepts needed for production environments: StatefulSets for databases, persistent storage, Helm for package management, and Ingress for routing. You'll deploy a complete WordPress + MySQL + Redis stack that's production-ready.

---

## 🎯 Learning Objectives

### **What You'll Master:**
- ✅ StatefulSets for stateful applications
- ✅ Persistent Volumes & Storage Classes
- ✅ Helm package manager
- ✅ Ingress controllers (Nginx)
- ✅ ConfigMaps & Secrets
- ✅ DaemonSets, Jobs, CronJobs
- ✅ Horizontal Pod Autoscaling
- ✅ Production best practices

### **Why It Matters for Your Career:**
- 💰 Adds **₹5-8 LPA** to salary potential
- 🏆 Required for **CKA/CKAD** certifications
- 🚀 80% of DevOps roles require these skills
- 📈 Production K8s experience = Senior roles

---

## 📚 Today's Topics

### **Morning (3 hours):**
1. **StatefulSets** - Managing stateful applications
2. **Persistent Storage** - PV, PVC, Storage Classes
3. **Helm** - Kubernetes package manager

### **Afternoon (3 hours):**
4. **Ingress Controllers** - HTTP/HTTPS routing
5. **ConfigMaps & Secrets** - Configuration management
6. **DaemonSets & Jobs** - Special workload types

### **Evening (2 hours):**
7. **Production Project** - Complete WordPress stack
8. **Best Practices** - Resource limits, health checks, autoscaling

---

## 🚀 Quick Start (30 Minutes)

### **Prerequisites Check:**
```bash
# Verify Kubernetes cluster
kubectl cluster-info
kubectl get nodes

# Check from Day 6
kubectl get all --all-namespaces
```

### **Install Helm:**
```bash
# macOS
brew install helm

# Verify
helm version

# Add repositories
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

### **Enable Ingress (Minikube):**
```bash
minikube addons enable ingress

# Verify
kubectl get pods -n ingress-nginx
```

---

## 💻 Key Concepts

### **1. StatefulSets vs Deployments**

| Feature | Deployment | StatefulSet |
|---------|-----------|-------------|
| **Pod Names** | Random (app-xyz123) | Ordered (app-0, app-1) |
| **Identity** | Interchangeable | Unique & stable |
| **Storage** | Shared or none | Per-pod persistent |
| **Ordering** | Random | Sequential |
| **Use For** | Stateless apps | Databases, queues |

**When to Use StatefulSets:**
- 🗄️ Databases (MySQL, PostgreSQL, MongoDB)
- 📨 Message queues (Kafka, RabbitMQ)
- 🔍 Search engines (Elasticsearch)
- 💾 Distributed storage (Cassandra)

### **2. Storage Hierarchy**

```
StorageClass (type of storage: SSD, HDD, etc.)
      ↓
PersistentVolume (actual storage: 10GB)
      ↓
PersistentVolumeClaim (request: "I need 5GB")
      ↓
Pod (uses the storage)
```

### **3. Helm Components**

- **Chart:** Package of K8s resources (like npm package)
- **Release:** Running instance of a chart
- **Repository:** Collection of charts (like npm registry)
- **Values:** Configuration for a chart

**Helm Benefits:**
- ✅ One command to install complex apps
- ✅ Version control for deployments
- ✅ Easy rollbacks
- ✅ Templating for reusability

### **4. Ingress Routing**

**Without Ingress:**
```
User → LoadBalancer (app1) → Service → Pod
User → LoadBalancer (app2) → Service → Pod
User → LoadBalancer (app3) → Service → Pod
```
💸 **Cost:** 3 LoadBalancers @ $20/month = $60/month

**With Ingress:**
```
User → Ingress (one LB) → {
    /app1 → Service1 → Pods
    /app2 → Service2 → Pods
    /app3 → Service3 → Pods
}
```
💰 **Cost:** 1 LoadBalancer @ $20/month = **Save $40/month!**

---

## 📋 Essential Commands

### **StatefulSets:**
```bash
# Create StatefulSet
kubectl apply -f mysql-statefulset.yaml

# Watch pods created in order
kubectl get pods -w

# Check persistent volume claims
kubectl get pvc

# Scale StatefulSet
kubectl scale statefulset mysql --replicas=5

# Delete (in reverse order)
kubectl delete statefulset mysql
```

### **Helm:**
```bash
# Search for charts
helm search repo wordpress

# Install chart
helm install my-app bitnami/wordpress

# List releases
helm list

# Upgrade release
helm upgrade my-app bitnami/wordpress --set replicas=3

# Rollback
helm rollback my-app

# Uninstall
helm uninstall my-app

# Create custom chart
helm create my-chart
```

### **Ingress:**
```bash
# Create Ingress
kubectl apply -f ingress.yaml

# Get Ingress details
kubectl get ingress
kubectl describe ingress main-ingress

# Check Ingress controller logs
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```

### **ConfigMaps & Secrets:**
```bash
# Create ConfigMap
kubectl create configmap app-config --from-literal=ENV=prod

# Create Secret
kubectl create secret generic db-pass --from-literal=password=secret123

# View (base64 encoded)
kubectl get secret db-pass -o yaml

# Decode
kubectl get secret db-pass -o jsonpath='{.data.password}' | base64 -d

# Delete
kubectl delete configmap app-config
kubectl delete secret db-pass
```

### **Autoscaling:**
```bash
# Create HPA
kubectl autoscale deployment myapp --cpu-percent=70 --min=2 --max=10

# Check HPA status
kubectl get hpa

# Generate load (testing)
kubectl run -i --tty load-generator --image=busybox /bin/sh
# while true; do wget -q -O- http://myapp-service; done
```

---

## 🔧 Today's Projects

### **Project 1: MySQL StatefulSet with Persistent Storage**
- Deploy 3-node MySQL cluster
- Each pod gets own persistent volume
- Test data persistence across pod restarts
- Verify ordered scaling

**Technologies:** StatefulSet, PVC, Headless Service  
**Time:** 45 minutes  
**Difficulty:** Medium

### **Project 2: WordPress with Helm**
- Install WordPress using Helm chart
- Customize with values.yaml
- Expose via NodePort
- Upgrade and rollback

**Technologies:** Helm, Charts, Releases  
**Time:** 30 minutes  
**Difficulty:** Easy

### **Project 3: Multi-App Ingress Routing**
- Deploy 2 applications
- Set up path-based routing (/app1, /app2)
- Set up host-based routing (app1.local, app2.local)
- Configure HTTPS/TLS

**Technologies:** Ingress, Nginx, TLS  
**Time:** 1 hour  
**Difficulty:** Medium

### **Project 4: Production WordPress Stack**
- WordPress (2 replicas) + MySQL (StatefulSet) + Redis (cache)
- Ingress with HTTPS
- ConfigMaps for config
- Secrets for passwords
- Resource limits
- Health checks
- Autoscaling

**Technologies:** All Day 8 concepts combined  
**Time:** 2 hours  
**Difficulty:** Advanced  
**Resume Value:** ⭐⭐⭐⭐⭐

---

## 📖 Study Resources

### **Official Documentation:**
- [Kubernetes StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Helm Documentation](https://helm.sh/docs/)
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

### **Hands-On Practice:**
- [Katacoda Kubernetes](https://www.katacoda.com/courses/kubernetes)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
- [Kubernetes Challenges](https://kodekloud.com/courses/kubernetes-challenges/)

### **Video Tutorials:**
- [TechWorld with Nana - Helm](https://youtu.be/X48VuDVv0do)
- [KodeKloud - StatefulSets](https://youtu.be/ZW5hm6jd0nE)
- [Kubernetes Ingress Explained](https://youtu.be/VicH6KojwCI)

---

## ✅ Success Criteria

### **By End of Day, You Should Have:**
- [ ] **3 StatefulSets** deployed and tested
- [ ] **Persistent storage** working (data survives pod restarts)
- [ ] **Helm** installed with 2+ charts deployed
- [ ] **Ingress** routing multiple apps
- [ ] **TLS/HTTPS** configured
- [ ] **ConfigMaps & Secrets** in use
- [ ] **Production WordPress** stack running
- [ ] **All code** committed to GitHub

### **Skills Checklist:**
- [ ] Can explain StatefulSet vs Deployment
- [ ] Can configure PV, PVC, StorageClass
- [ ] Can install/upgrade apps with Helm
- [ ] Can create custom Helm charts
- [ ] Can configure Ingress routing (path & host)
- [ ] Can set up TLS certificates
- [ ] Can use ConfigMaps and Secrets
- [ ] Can implement resource limits
- [ ] Can configure health probes
- [ ] Can set up autoscaling

---

## 🎯 Interview Preparation

### **Common Questions:**

**Q1: When would you use StatefulSet instead of Deployment?**
- StatefulSets for: databases, message queues, distributed systems
- Need: stable network ID, ordered deployment, persistent storage per pod
- Deployments for: stateless apps, microservices, web frontends

**Q2: Explain PV vs PVC**
- **PV (PersistentVolume):** Actual storage resource (created by admin)
- **PVC (PersistentVolumeClaim):** Request for storage (created by developer)
- Analogy: PV = warehouse, PVC = order form

**Q3: What is Helm and why use it?**
- Package manager for Kubernetes
- Benefits: templating, version control, easy rollbacks, reusability
- Example: `helm install wordpress` vs 20+ kubectl commands

**Q4: How does Ingress save costs?**
- One LoadBalancer for multiple services
- Without: 10 services = 10 LBs @ $200/month
- With: 1 Ingress LB @ $20/month = **Save $180/month**

**Q5: ConfigMap vs Secret - when to use which?**
- **ConfigMap:** Non-sensitive config (database host, app settings)
- **Secret:** Sensitive data (passwords, API keys, tokens)
- Secrets are base64 encoded (not encrypted!)

---

## 📊 Progress Tracking

### **Day 8 Stats:**
- **Concepts:** 10+ advanced topics
- **Commands:** 50+ kubectl/helm commands
- **Projects:** 4 hands-on projects
- **Time:** 8 hours total
- **Resume Lines:** 6-8 bullet points
- **Salary Impact:** +₹5-8 LPA

### **Learning Path:**
```
✅ Day 6: Kubernetes Basics
✅ Day 7: AWS Fundamentals
🔄 Day 8: Advanced Kubernetes ← YOU ARE HERE
⬜ Day 9: Helm Deep Dive & Monitoring
⬜ Day 10: Kubernetes Networking
⬜ Day 14: Kubernetes Production (CKA prep)
```

---

## 🚀 Next Steps

### **After Completing Day 8:**
1. **Update Portfolio:**
   - Add WordPress stack project
   - Document architecture diagram
   - Include Helm charts

2. **Practice:**
   - Deploy 3 different StatefulSets
   - Create 2 custom Helm charts
   - Set up multi-tenant Ingress

3. **Certifications:**
   - Start CKA preparation (50% concepts covered)
   - Practice CKAD exercises

4. **Job Applications:**
   - Update resume with today's skills
   - Highlight production K8s experience
   - Share projects on LinkedIn

---

## 📝 Notes Section

Use `/DAY_08/notes/day-08-notes.md` for:
- Personal observations
- Troubleshooting steps
- Questions to research
- Interview prep notes
- Performance metrics

---

## 🎉 Motivation

> "Kubernetes is the future of application deployment. Master it, and you'll always be in demand."  
> — DevOps proverb

**You're 40% through the roadmap!** Advanced Kubernetes skills are what separate junior from senior DevOps engineers. Today's learnings are directly applicable to production environments at top companies.

**Keep going! You're building serious expertise! 💪🚀**

---

**📂 Files in This Folder:**
- `DAY_8_PLAN.md` - Detailed 8-hour schedule
- `README.md` - This overview
- `/notes/day-08-notes.md` - Your learning journal
- `/projects/` - Hands-on project guides

**Let's make Day 8 count! 🎯**
