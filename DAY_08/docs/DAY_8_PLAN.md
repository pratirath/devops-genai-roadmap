# Day 8: Advanced Kubernetes - Production-Ready Orchestration

> **Date:** February 22, 2026  
> **Focus:** StatefulSets, Persistent Volumes, Helm, Ingress, and Production Best Practices  
> **Duration:** 8 hours  
> **Goal:** Master advanced Kubernetes concepts and deploy production-grade stateful applications

---

## 📋 Learning Objectives

By the end of Day 8, you will:
- ✅ Master StatefulSets for stateful applications
- ✅ Configure Persistent Volumes and Storage Classes
- ✅ Deploy applications with Helm package manager
- ✅ Implement Ingress controllers for HTTP routing
- ✅ Use ConfigMaps and Secrets effectively
- ✅ Set up Horizontal Pod Autoscaling (HPA)
- ✅ Implement DaemonSets and Jobs
- ✅ Deploy a production-ready WordPress + MySQL stack

---

## 🎯 Why Advanced Kubernetes Skills Matter for 20+ LPA Roles

### **Market Demand:**
- 🔥 **85%** of enterprises use Kubernetes in production
- 💰 **K8s expertise** adds 20-30% salary premium to DevOps roles
- 🚀 **StatefulSets & Helm** are must-have production skills
- 📈 **CKA/CKAD certifications** directly lead to higher pay

### **Career Impact:**
- Kubernetes Administrator (CKA): **₹20-35 LPA**
- DevOps Engineer with K8s production exp: **₹22-42 LPA**
- SRE with Kubernetes: **₹25-50 LPA**
- Platform Engineer: **₹28-55 LPA**

### **Real-World Applications:**
- Databases (PostgreSQL, MySQL, MongoDB) on K8s
- Message queues (Kafka, RabbitMQ)
- Caching layers (Redis, Memcached)
- Logging/monitoring stacks
- CI/CD systems

---

## 📚 Session Breakdown

### **Morning Session (3 hours): StatefulSets & Persistent Storage**

#### **Hour 1: StatefulSets Deep Dive (9:00 AM - 10:00 AM)**

**Topics:**
1. StatefulSets vs Deployments
2. Stable network identities
3. Ordered deployment and scaling
4. Persistent storage per pod
5. Headless services

**Key Concepts:**

**When to Use StatefulSets:**
- ✅ Databases (MySQL, PostgreSQL, MongoDB)
- ✅ Message queues (Kafka, RabbitMQ)
- ✅ Distributed systems (Elasticsearch, Cassandra)
- ✅ Any app requiring stable network ID or persistent storage

**When to Use Deployments:**
- ✅ Stateless web applications
- ✅ Microservices APIs
- ✅ Frontend applications
- ✅ Worker processes (without state)

**Hands-On: Deploy MySQL StatefulSet**

1. **Create Namespace:**
```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: database
```

2. **Create Headless Service:**
```yaml
# mysql-headless-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql-headless
  namespace: database
  labels:
    app: mysql
spec:
  ports:
  - port: 3306
    name: mysql
  clusterIP: None  # Headless service
  selector:
    app: mysql
```

3. **Create StatefulSet:**
```yaml
# mysql-statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
  namespace: database
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
          value: "rootpassword123"  # Use Secret in production!
        - name: MYSQL_DATABASE
          value: "appdb"
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
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 10Gi
```

**Deploy and Test:**
```bash
# Apply resources
kubectl apply -f namespace.yaml
kubectl apply -f mysql-headless-service.yaml
kubectl apply -f mysql-statefulset.yaml

# Watch pods being created in order
kubectl get pods -n database -w

# Expected:
# mysql-0    1/1     Running
# mysql-1    1/1     Running  (after mysql-0 is ready)
# mysql-2    1/1     Running  (after mysql-1 is ready)

# Check PVCs (automatically created)
kubectl get pvc -n database

# Connect to MySQL pod
kubectl exec -it mysql-0 -n database -- mysql -uroot -prootpassword123

# Inside MySQL:
# CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100));
# INSERT INTO users VALUES (1, 'John Doe');
# SELECT * FROM users;
# exit

# Delete pod and watch it recreate with same data
kubectl delete pod mysql-0 -n database
kubectl get pods -n database -w

# Reconnect and verify data persisted
kubectl exec -it mysql-0 -n database -- mysql -uroot -prootpassword123 -e "USE appdb; SELECT * FROM users;"
```

**StatefulSet Features Demonstrated:**
- ✅ Pods get predictable names: mysql-0, mysql-1, mysql-2
- ✅ Pods created in order (0 → 1 → 2)
- ✅ Each pod gets own PVC (mysql-data-mysql-0, etc.)
- ✅ Pod identity maintained across restarts
- ✅ Headless service for direct pod access

---

#### **Hour 2: Persistent Volumes & Storage Classes (10:00 AM - 11:00 AM)**

**Topics:**
1. Persistent Volumes (PV)
2. Persistent Volume Claims (PVC)
3. Storage Classes
4. Dynamic provisioning
5. Volume modes and access modes

**Storage Hierarchy:**
```
StorageClass (defines type of storage)
     ↓
PersistentVolume (actual storage resource)
     ↓
PersistentVolumeClaim (request for storage)
     ↓
Pod (uses the storage)
```

**Hands-On: Storage Classes and Dynamic Provisioning**

1. **Create Storage Class:**
```yaml
# storageclass.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/no-provisioner  # For Minikube
volumeBindingMode: WaitForFirstConsumer
reclaimPolicy: Retain
```

For cloud providers:
```yaml
# AWS EBS Storage Class
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: aws-ebs-fast
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  iops: "3000"
  encrypted: "true"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

2. **Create Persistent Volume (Manual - for Minikube):**
```yaml
# pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-pv-1
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: fast-ssd
  hostPath:
    path: /mnt/data/pv-1
```

3. **Create Persistent Volume Claim:**
```yaml
# pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-storage
  namespace: default
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: fast-ssd
```

4. **Use PVC in Pod:**
```yaml
# pod-with-pvc.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-storage
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    volumeMounts:
    - name: data
      mountPath: /usr/share/nginx/html
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: app-storage
```

**Deploy and Test:**
```bash
# Create resources
kubectl apply -f storageclass.yaml
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
kubectl apply -f pod-with-storage.yaml

# Check PV binding
kubectl get pv
kubectl get pvc

# Write data to volume
kubectl exec app-with-storage -- sh -c "echo 'Hello from PV!' > /usr/share/nginx/html/index.html"

# Delete pod
kubectl delete pod app-with-storage

# Recreate pod
kubectl apply -f pod-with-storage.yaml

# Verify data persisted
kubectl exec app-with-storage -- cat /usr/share/nginx/html/index.html
# Output: Hello from PV!
```

**Access Modes:**
- **ReadWriteOnce (RWO):** Single node read-write
- **ReadOnlyMany (ROX):** Multiple nodes read-only
- **ReadWriteMany (RWX):** Multiple nodes read-write

**Reclaim Policies:**
- **Retain:** Manual cleanup (safe)
- **Delete:** Auto-delete when PVC deleted (risky)
- **Recycle:** Deprecated

---

#### **Hour 3: Helm Package Manager (11:00 AM - 12:00 PM)**

**Topics:**
1. Why Helm?
2. Charts, releases, repositories
3. Installing Helm
4. Using Helm charts
5. Creating custom charts

**Why Helm?**
- ✅ Package manager for Kubernetes
- ✅ Templating for YAML files
- ✅ Version control for deployments
- ✅ Easy rollbacks
- ✅ Reusable configurations

**Hands-On: Install and Use Helm**

1. **Install Helm (macOS):**
```bash
# Install Helm
brew install helm

# Verify installation
helm version

# Add popular chart repositories
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add stable https://charts.helm.sh/stable
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# Update repositories
helm repo update

# Search for charts
helm search repo wordpress
helm search repo mysql
helm search repo prometheus
```

2. **Deploy WordPress with Helm:**
```bash
# Install WordPress
helm install my-wordpress bitnami/wordpress \
  --set wordpressUsername=admin \
  --set wordpressPassword=password123 \
  --set service.type=NodePort \
  --set persistence.enabled=true \
  --set persistence.size=10Gi

# Watch deployment
kubectl get pods -w

# Get WordPress credentials
echo Username: admin
echo Password: $(kubectl get secret --namespace default my-wordpress -o jsonpath="{.data.wordpress-password}" | base64 -d)

# Get WordPress URL
export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services my-wordpress)
export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
echo "WordPress URL: http://$NODE_IP:$NODE_PORT/"

# If using Minikube:
minikube service my-wordpress
```

3. **Manage Helm Releases:**
```bash
# List installed releases
helm list

# Get release status
helm status my-wordpress

# Get release values
helm get values my-wordpress

# Upgrade release
helm upgrade my-wordpress bitnami/wordpress \
  --set replicaCount=2

# Rollback to previous version
helm rollback my-wordpress

# Uninstall release
helm uninstall my-wordpress
```

4. **Create Custom Helm Chart:**
```bash
# Create new chart
helm create my-app

# Chart structure:
# my-app/
# ├── Chart.yaml          # Chart metadata
# ├── values.yaml         # Default values
# ├── templates/          # K8s resource templates
# │   ├── deployment.yaml
# │   ├── service.yaml
# │   └── ingress.yaml
# └── charts/             # Dependencies

# Edit values.yaml
cat > my-app/values.yaml <<EOF
replicaCount: 2

image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
EOF

# Install your chart
helm install my-release ./my-app

# Package chart
helm package my-app

# Generated: my-app-0.1.0.tgz
```

---

### **Afternoon Session (3 hours): Ingress, ConfigMaps & Secrets**

#### **Hour 4: Ingress Controllers (1:00 PM - 2:00 PM)**

**Topics:**
1. Ingress vs Service
2. Ingress controllers (Nginx, Traefik)
3. Path-based routing
4. Host-based routing
5. TLS/SSL termination

**Why Ingress?**
- ✅ Single LoadBalancer for multiple services
- ✅ Path and host-based routing
- ✅ SSL/TLS termination
- ✅ Cost-effective (vs multiple LoadBalancers)

**Hands-On: Nginx Ingress Controller**

1. **Install Nginx Ingress (Minikube):**
```bash
# Enable ingress addon
minikube addons enable ingress

# Verify ingress controller
kubectl get pods -n ingress-nginx

# For other K8s clusters:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml
```

2. **Deploy Sample Applications:**
```yaml
# app1-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app1
spec:
  replicas: 2
  selector:
    matchLabels:
      app: app1
  template:
    metadata:
      labels:
        app: app1
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
        volumeMounts:
        - name: html
          mountPath: /usr/share/nginx/html
      volumes:
      - name: html
        configMap:
          name: app1-html
---
apiVersion: v1
kind: Service
metadata:
  name: app1-service
spec:
  selector:
    app: app1
  ports:
  - port: 80
    targetPort: 80
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app1-html
data:
  index.html: |
    <h1>Application 1</h1>
    <p>This is app1 served via Ingress!</p>
```

```yaml
# app2-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app2
spec:
  replicas: 2
  selector:
    matchLabels:
      app: app2
  template:
    metadata:
      labels:
        app: app2
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
        volumeMounts:
        - name: html
          mountPath: /usr/share/nginx/html
      volumes:
      - name: html
        configMap:
          name: app2-html
---
apiVersion: v1
kind: Service
metadata:
  name: app2-service
spec:
  selector:
    app: app2
  ports:
  - port: 80
    targetPort: 80
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app2-html
data:
  index.html: |
    <h1>Application 2</h1>
    <p>This is app2 served via Ingress!</p>
```

3. **Create Ingress Resource:**
```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: main-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: myapp.local  # Add to /etc/hosts
    http:
      paths:
      - path: /app1
        pathType: Prefix
        backend:
          service:
            name: app1-service
            port:
              number: 80
      - path: /app2
        pathType: Prefix
        backend:
          service:
            name: app2-service
            port:
              number: 80
  - host: app1.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app1-service
            port:
              number: 80
  - host: app2.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app2-service
            port:
              number: 80
```

**Deploy and Test:**
```bash
# Deploy applications
kubectl apply -f app1-deployment.yaml
kubectl apply -f app2-deployment.yaml
kubectl apply -f ingress.yaml

# Get Ingress IP
kubectl get ingress

# Add to /etc/hosts (macOS/Linux):
echo "$(minikube ip) myapp.local app1.local app2.local" | sudo tee -a /etc/hosts

# Test path-based routing:
curl http://myapp.local/app1
# Output: Application 1

curl http://myapp.local/app2
# Output: Application 2

# Test host-based routing:
curl http://app1.local
# Output: Application 1

curl http://app2.local
# Output: Application 2
```

4. **TLS/HTTPS Ingress:**
```bash
# Generate self-signed certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt \
  -subj "/CN=myapp.local/O=myapp"

# Create TLS secret
kubectl create secret tls myapp-tls \
  --cert=tls.crt \
  --key=tls.key

# Update Ingress with TLS:
cat > ingress-tls.yaml <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: main-ingress
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - myapp.local
    secretName: myapp-tls
  rules:
  - host: myapp.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app1-service
            port:
              number: 80
EOF

kubectl apply -f ingress-tls.yaml

# Test HTTPS
curl -k https://myapp.local
```

---

#### **Hour 5: ConfigMaps & Secrets (2:00 PM - 3:00 PM)**

**Topics:**
1. ConfigMaps for configuration
2. Secrets for sensitive data
3. Mounting as volumes vs environment variables
4. Best practices

**ConfigMaps:**
Store non-confidential configuration data

**Secrets:**
Store sensitive data (passwords, tokens, keys)

**Hands-On: ConfigMaps and Secrets**

1. **Create ConfigMap (Multiple Ways):**

**From literal values:**
```bash
kubectl create configmap app-config \
  --from-literal=APP_ENV=production \
  --from-literal=APP_DEBUG=false \
  --from-literal=LOG_LEVEL=info
```

**From file:**
```bash
# Create config file
cat > app.properties <<EOF
database.host=mysql-service
database.port=3306
database.name=appdb
cache.enabled=true
cache.ttl=3600
EOF

kubectl create configmap app-config-file \
  --from-file=app.properties
```

**From YAML:**
```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config-yaml
data:
  APP_ENV: "production"
  APP_DEBUG: "false"
  LOG_LEVEL: "info"
  app.properties: |
    database.host=mysql-service
    database.port=3306
    database.name=appdb
```

```bash
kubectl apply -f configmap.yaml
```

2. **Create Secrets (Multiple Ways):**

**From literal (base64 encoded automatically):**
```bash
kubectl create secret generic db-credentials \
  --from-literal=username=admin \
  --from-literal=password=supersecret123
```

**From file:**
```bash
echo -n 'admin' > username.txt
echo -n 'supersecret123' > password.txt

kubectl create secret generic db-credentials-file \
  --from-file=username=username.txt \
  --from-file=password=password.txt

rm username.txt password.txt
```

**From YAML (manually base64 encode):**
```bash
echo -n 'admin' | base64
# YWRtaW4=

echo -n 'supersecret123' | base64
# c3VwZXJzZWNyZXQxMjM=
```

```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials-yaml
type: Opaque
data:
  username: YWRtaW4=
  password: c3VwZXJzZWNyZXQxMjM=
```

```bash
kubectl apply -f secret.yaml
```

3. **Use ConfigMap and Secret in Pod:**

**As Environment Variables:**
```yaml
# pod-with-config.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-config
spec:
  containers:
  - name: app
    image: busybox
    command: ["sh", "-c", "while true; do env | grep -E 'APP_|DB_'; sleep 30; done"]
    env:
    # Individual env vars from ConfigMap
    - name: APP_ENV
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: APP_ENV
    - name: LOG_LEVEL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: LOG_LEVEL
    # Individual env vars from Secret
    - name: DB_USERNAME
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: username
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
    # All keys from ConfigMap as env vars
    envFrom:
    - configMapRef:
        name: app-config
    # All keys from Secret as env vars
    - secretRef:
        name: db-credentials
```

**As Mounted Files (Volumes):**
```yaml
# pod-with-volumes.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-volumes
spec:
  containers:
  - name: app
    image: nginx:1.21
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
    - name: secret-volume
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: config-volume
    configMap:
      name: app-config-file
  - name: secret-volume
    secret:
      secretName: db-credentials
```

**Deploy and Test:**
```bash
# Deploy pods
kubectl apply -f pod-with-config.yaml
kubectl apply -f pod-with-volumes.yaml

# Check env vars
kubectl logs app-with-config

# Check mounted files
kubectl exec app-with-volumes -- ls /etc/config
kubectl exec app-with-volumes -- cat /etc/config/app.properties

kubectl exec app-with-volumes -- ls /etc/secrets
kubectl exec app-with-volumes -- cat /etc/secrets/username
kubectl exec app-with-volumes -- cat /etc/secrets/password
```

**Best Practices:**
- ✅ Use Secrets for passwords, tokens, keys
- ✅ Use ConfigMaps for non-sensitive config
- ✅ Mount secrets as files (more secure than env vars)
- ✅ Use RBAC to control secret access
- ✅ Consider external secret managers (AWS Secrets Manager, HashiCorp Vault)
- ✅ Never commit secrets to Git
- ✅ Rotate secrets regularly

---

#### **Hour 6: DaemonSets, Jobs & CronJobs (3:00 PM - 4:00 PM)**

**Topics:**
1. DaemonSets - one pod per node
2. Jobs - run to completion
3. CronJobs - scheduled jobs
4. Use cases for each

**DaemonSets:**
Ensures a copy of pod runs on all (or some) nodes

**Use Cases:**
- Log collection (Fluentd, Logstash)
- Node monitoring (Prometheus Node Exporter)
- Storage daemons (Ceph, GlusterFS)
- Network plugins

**Hands-On: DaemonSet**

```yaml
# fluentd-daemonset.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  namespace: kube-system
  labels:
    app: fluentd
spec:
  selector:
    matchLabels:
      app: fluentd
  template:
    metadata:
      labels:
        app: fluentd
    spec:
      tolerations:
      # Allow on master node
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      containers:
      - name: fluentd
        image: fluent/fluentd:v1.14
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```

```bash
kubectl apply -f fluentd-daemonset.yaml

# Check DaemonSet
kubectl get daemonset -n kube-system

# Verify pod on each node
kubectl get pods -n kube-system -o wide | grep fluentd
```

**Jobs:**
Run a task to completion

**Use Cases:**
- Database migrations
- Batch processing
- Backup operations
- One-time tasks

```yaml
# database-migration-job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration
spec:
  template:
    spec:
      containers:
      - name: migrate
        image: migrate/migrate
        command: ["migrate", "-path=/migrations", "-database", "postgres://user:pass@host/db", "up"]
      restartPolicy: Never
  backoffLimit: 4  # Retry 4 times on failure
  activeDeadlineSeconds: 300  # Timeout after 5 minutes
```

**CronJobs:**
Scheduled recurring jobs

**Use Cases:**
- Database backups
- Report generation
- Cleanup tasks
- Health checks

```yaml
# backup-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: database-backup
spec:
  schedule: "0 2 * * *"  # Every day at 2 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: mysql:8.0
            command:
            - /bin/sh
            - -c
            - |
              mysqldump -h mysql-service -u root -p$MYSQL_PASSWORD appdb > /backup/backup-$(date +%Y%m%d).sql
            env:
            - name: MYSQL_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-credentials
                  key: password
            volumeMounts:
            - name: backup-volume
              mountPath: /backup
          restartPolicy: OnFailure
          volumes:
          - name: backup-volume
            persistentVolumeClaim:
              claimName: backup-storage
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
```

```bash
kubectl apply -f backup-cronjob.yaml

# List CronJobs
kubectl get cronjobs

# Manually trigger a job
kubectl create job --from=cronjob/database-backup manual-backup-1

# View job logs
kubectl logs job/manual-backup-1
```

---

### **Evening Session (2 hours): Production Project & Best Practices**

#### **Hour 7: Production WordPress Stack (4:00 PM - 5:00 PM)**

**Project: Complete WordPress + MySQL + Redis Stack**

**Architecture:**
```
Ingress (HTTPS)
    ↓
WordPress Service (ClusterIP)
    ↓
WordPress Deployment (2 replicas)
    ↓
    ├──→ MySQL StatefulSet (Persistent)
    └──→ Redis Deployment (Cache)
```

**Complete Deployment:**

1. **Namespace & Storage:**
```yaml
# 01-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: wordpress-prod
---
# 02-storageclass.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: wordpress-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
reclaimPolicy: Retain
```

2. **Secrets & ConfigMaps:**
```yaml
# 03-secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysql-secret
  namespace: wordpress-prod
type: Opaque
stringData:
  root-password: "rootpass123"
  database: "wordpress"
  user: "wpuser"
  password: "wppass123"
---
apiVersion: v1
kind: Secret
metadata:
  name: wordpress-secret
  namespace: wordpress-prod
type: Opaque
stringData:
  wp-admin-user: "admin"
  wp-admin-password: "admin123"
  wp-admin-email: "admin@example.com"
---
# 04-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: wordpress-config
  namespace: wordpress-prod
data:
  WORDPRESS_TABLE_PREFIX: "wp_"
  WORDPRESS_DEBUG: "0"
```

3. **MySQL StatefulSet:**
```yaml
# 05-mysql-statefulset.yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql
  namespace: wordpress-prod
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
  namespace: wordpress-prod
spec:
  serviceName: mysql
  replicas: 1
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
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: root-password
        - name: MYSQL_DATABASE
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: database
        - name: MYSQL_USER
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: user
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: password
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
        livenessProbe:
          exec:
            command: ["mysqladmin", "ping", "-h", "localhost"]
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          exec:
            command: ["mysqladmin", "ping", "-h", "localhost"]
          initialDelaySeconds: 5
          periodSeconds: 5
  volumeClaimTemplates:
  - metadata:
      name: mysql-data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

4. **Redis Cache:**
```yaml
# 06-redis-deployment.yaml
apiVersion: v1
kind: Service
metadata:
  name: redis
  namespace: wordpress-prod
spec:
  ports:
  - port: 6379
  selector:
    app: redis
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: wordpress-prod
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7-alpine
        ports:
        - containerPort: 6379
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
```

5. **WordPress Deployment:**
```yaml
# 07-wordpress-deployment.yaml
apiVersion: v1
kind: Service
metadata:
  name: wordpress
  namespace: wordpress-prod
spec:
  type: ClusterIP
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: wordpress
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
  namespace: wordpress-prod
spec:
  replicas: 2
  selector:
    matchLabels:
      app: wordpress
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - name: wordpress
        image: wordpress:6.4-apache
        ports:
        - containerPort: 80
        env:
        - name: WORDPRESS_DB_HOST
          value: mysql:3306
        - name: WORDPRESS_DB_NAME
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: database
        - name: WORDPRESS_DB_USER
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: user
        - name: WORDPRESS_DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: password
        - name: WORDPRESS_CONFIG_EXTRA
          value: |
            define('WP_REDIS_HOST', 'redis');
            define('WP_REDIS_PORT', 6379);
        envFrom:
        - configMapRef:
            name: wordpress-config
        volumeMounts:
        - name: wordpress-data
          mountPath: /var/www/html
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /wp-admin/install.php
            port: 80
          initialDelaySeconds: 60
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /wp-admin/install.php
            port: 80
          initialDelaySeconds: 30
          periodSeconds: 5
      volumes:
      - name: wordpress-data
        persistentVolumeClaim:
          claimName: wordpress-pvc
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: wordpress-pvc
  namespace: wordpress-prod
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
```

6. **Ingress:**
```yaml
# 08-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: wordpress-ingress
  namespace: wordpress-prod
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
spec:
  ingressClassName: nginx
  rules:
  - host: wordpress.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: wordpress
            port:
              number: 80
```

**Deploy Everything:**
```bash
# Deploy in order
for file in 01-namespace.yaml 02-storageclass.yaml 03-secrets.yaml 04-configmap.yaml 05-mysql-statefulset.yaml 06-redis-deployment.yaml 07-wordpress-deployment.yaml 08-ingress.yaml; do
  kubectl apply -f $file
done

# Watch deployment
kubectl get pods -n wordpress-prod -w

# Add to /etc/hosts
echo "$(minikube ip) wordpress.local" | sudo tee -a /etc/hosts

# Access WordPress
open http://wordpress.local
```

---

#### **Hour 8: Best Practices & Cleanup (5:00 PM - 6:00 PM)**

**Production Best Practices:**

1. **Resource Limits:**
```yaml
resources:
  requests:    # Minimum guaranteed
    memory: "256Mi"
    cpu: "250m"
  limits:      # Maximum allowed
    memory: "512Mi"
    cpu: "500m"
```

2. **Health Checks:**
```yaml
livenessProbe:   # Restart if unhealthy
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:  # Remove from service if not ready
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

3. **Pod Disruption Budgets:**
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: wordpress-pdb
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: wordpress
```

4. **Horizontal Pod Autoscaler:**
```bash
kubectl autoscale deployment wordpress \
  --cpu-percent=70 \
  --min=2 \
  --max=10 \
  -n wordpress-prod
```

5. **Network Policies:**
```yaml
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

**Cleanup:**
```bash
# Delete namespace (deletes everything inside)
kubectl delete namespace wordpress-prod

# Or delete individual resources
kubectl delete -f 08-ingress.yaml
kubectl delete -f 07-wordpress-deployment.yaml
kubectl delete -f 06-redis-deployment.yaml
kubectl delete -f 05-mysql-statefulset.yaml
kubectl delete -f 04-configmap.yaml
kubectl delete -f 03-secrets.yaml
kubectl delete -f 02-storageclass.yaml
kubectl delete -f 01-namespace.yaml
```

---

## ✅ Day 8 Checklist

### **Morning:**
- [ ] Deployed MySQL StatefulSet
- [ ] Understood stable network identities
- [ ] Configured PersistentVolumes
- [ ] Used dynamic provisioning
- [ ] Installed Helm
- [ ] Deployed app with Helm chart
- [ ] Created custom Helm chart

### **Afternoon:**
- [ ] Set up Nginx Ingress Controller
- [ ] Configured path-based routing
- [ ] Configured host-based routing
- [ ] Set up TLS/HTTPS
- [ ] Created ConfigMaps
- [ ] Created Secrets
- [ ] Used both as env vars and volumes

### **Evening:**
- [ ] Deployed production WordPress stack
- [ ] Configured StatefulSet for MySQL
- [ ] Added Redis caching
- [ ] Set up Ingress for WordPress
- [ ] Implemented resource limits
- [ ] Added health checks
- [ ] Tested complete workflow

---

## 📊 Success Metrics

By end of Day 8, you should have:
- ✅ **3 StatefulSet deployments** working
- ✅ **Persistent storage** configured and tested
- ✅ **Helm** installed and used
- ✅ **Ingress controller** routing traffic
- ✅ **Production WordPress** stack running
- ✅ **ConfigMaps & Secrets** properly used
- ✅ **Resource limits** on all pods
- ✅ **Health checks** implemented

**Time Investment:** 8 hours  
**Concepts Mastered:** 10+  
**Projects:** 1 production-grade application  
**Resume Value:** Very High! 🎯

---

## 🎯 Career Impact

### **Skills Gained Today:**
- ✅ StatefulSet management
- ✅ Persistent storage
- ✅ Helm package management
- ✅ Ingress configuration
- ✅ Production best practices
- ✅ Resource management
- ✅ Health monitoring

### **Interview Questions You Can Answer:**
1. When would you use a StatefulSet vs Deployment?
2. Explain the difference between PV and PVC
3. What is Helm and why use it?
4. How does Ingress differ from Service?
5. When should you use ConfigMap vs Secret?
6. What are health probes and why are they important?
7. How do you scale stateful applications on Kubernetes?

### **Resume Bullet Points:**
- "Deployed and managed stateful applications on Kubernetes using StatefulSets"
- "Implemented persistent storage solutions with PVs, PVCs, and Storage Classes"
- "Packaged and deployed applications using Helm charts with custom templates"
- "Configured Ingress controllers for HTTP/HTTPS routing and SSL termination"
- "Managed application configuration with ConfigMaps and Secrets"
- "Implemented production best practices including resource limits and health checks"
- "Deployed complete WordPress stack on Kubernetes with MySQL and Redis"

---

**🎯 Day 8 Complete!** You're now production-ready with Kubernetes! Tomorrow: Helm deep dive and monitoring with Prometheus/Grafana! 🚀
