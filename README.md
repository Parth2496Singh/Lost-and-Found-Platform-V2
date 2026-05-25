# 🚀 Lost & Found Platform (V4 GitOps Edition)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) ![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white) ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white) ![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white) ![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

A full-stack Lost & Found web application with a modern, enterprise-grade GitOps workflow featuring Jenkins CI, ArgoCD, automated image updating, and DevSecOps integrations.

---

## 📑 Table of Contents

1. [Project Overview](#project-overview)  
2. [Features & Version History](#features)  
3. [Tech Stack](#tech-stack)  
4. [Dual-Repo Architecture Structure](#project-structure)  
5. [Installation & Setup](#installation--setup)  
   - Local Development (Docker Compose) 💻  
   - Continuous Delivery (GitOps via ArgoCD) 🚀  
6. [API Endpoints](#api-endpoints)  
7. [Screenshots](#screenshots)  
8. [Known Issues & Future Improvements](#known-issues--limitations)  

---

## 📌 Project Overview

The **Lost & Found Platform** is a full-stack web application that enables users to report lost and found items, claim items, and track their submissions efficiently.

### ⚙️ The GitOps Upgrade (V4)

This project utilizes a **Dual-Repository GitOps Architecture**. To prevent CI/CD infinite build loops, the application source code and the Kubernetes/Helm infrastructure manifests are entirely separated. 
* **Continuous Integration (Jenkins):** Handles code cloning, DevSecOps scanning (Trivy & OWASP), SonarQube quality gates, and building/pushing dynamic SemVer Docker images.
* **Continuous Delivery (ArgoCD):** Monitors the secondary GitOps repository, utilizing the ArgoCD Image Updater to automatically track new DockerHub images, update the Helm values, and sync the Kubernetes cluster securely while sending real-time email notifications.

---

## ✨ Features

### 🧩 V1 & V2 (Application Base)
- 🔐 JWT Authentication (Login / Signup)
- 📦 Full claim system (claim found items, approve/reject workflow)
- 👤 User-specific dashboard (lost & found tracking)
- 🎨 Dynamic API-driven frontend using Vanilla JavaScript

### 🚀 V3 (Containerization & Orchestration)
- Fully containerized using **Docker & Docker Compose**
- Production routing via **Nginx reverse proxy**
- Kubernetes manifests (Deployments, Services, HPA, Gateway API)
- Custom **Helm chart** for dynamic Kubernetes deployments

### 🔄 V4 (DevSecOps & GitOps Automation)
- 🏗️ **Dual-Repo Architecture:** Clean separation of Source Code and Deployment Manifests.
- 🛡️ **DevSecOps CI Pipeline (Jenkins):** Automated Trivy filesystem scans, OWASP dependency checks, and SonarQube code quality gates.
- 🐙 **Continuous Delivery (ArgoCD):** Deploys Helm charts dynamically via `ApplicationSet`.
- 🤖 **ArgoCD Image Updater:** Automatically detects new Docker images (`v1.0.X`), writes the new tags back to the GitOps repository, and triggers a sync.
- 📧 **Automated Alerts:** ArgoCD Notifications configured via ConfigMap and Gmail SMTP to send email alerts on successful deployments or degraded cluster health.
- ⚖️ **HPA Compatibility:** ArgoCD ignores replica differences to allow the Horizontal Pod Autoscaler to manage scaling seamlessly.

---

## 🧰 Tech Stack

**Backend & Frontend:** Python 🐍, Django, REST Framework, SQLite, Bootstrap 5, Vanilla JS  
**DevSecOps & CI:** Jenkins, SonarQube, Trivy, OWASP Dependency Check  
**GitOps & CD:** ArgoCD, ArgoCD Image Updater, ArgoCD Notifications  
**Infrastructure:** Docker, Kubernetes (KIND), Helm, AWS EC2, Nginx Reverse Proxy  

---

## 📁 Project Structure (Dual-Repo Architecture)

### 1. Source Code Repository (This Repo)
```text
accounts/           # User models and authentication logic
api/                # REST API endpoints and serializers
frontend/           # HTML templates + static frontend assets
nginx/              # Nginx reverse proxy configuration
reports/            # Lost & Found item models and logic
LostFoundProject/   # Django project settings and configuration
screenshots/        # Project UI and architecture screenshots
JenkinsFile         # Declarative CI pipeline (Build, Scan, QA, Push)
Dockerfile          # Django app containerization
docker-compose.yml  # Multi-container local setup
manage.py           # Django management utility
requirements.txt    # Python dependencies
```

### 2. GitOps Infrastructure Repository (`Lost-and-Found-GitOps`)
```text
gitops/
├── configmap-argocd-noti.yml    # ArgoCD SMTP Email Notification Config
├── list.yml                     # ArgoCD ApplicationSet deployment config
└── lostfound-image-updater.yaml # ArgoCD Image Updater write-back config
helm/
└── lostfound/                   # Helm charts (Chart.yaml, values.yaml, templates)
```

---

## ⚙️ Installation & Setup

### 💻 Local Development (For Writing Code)
For local testing and development, we use Docker Compose to spin up the application and database quickly without needing a Kubernetes cluster.

1. Clone the repository
   ```bash
   git clone [https://github.com/Parth2496Singh/Lost-and-Found-Platform-V2.git](https://github.com/Parth2496Singh/Lost-and-Found-Platform-V2.git)
   cd Lost-and-Found-Platform-V2
   ```
2. Build and run containers
   ```bash
   docker-compose up -d --build
   ```
3. Access the application at `http://localhost`

---

### 🚀 Production Deployment (GitOps via ArgoCD)
This project uses a fully automated GitOps workflow. Manual deployments (`kubectl apply` or `helm install`) are deprecated in V4 in favor of Continuous Delivery.

**Prerequisites:** A running Kubernetes cluster, Jenkins CI server, and ArgoCD installed.

1. **Trigger the CI Pipeline (Jenkins):**
   - Push code to the `main` branch of this Source Code repository.
   - Jenkins will automatically run DevSecOps scans (Trivy, OWASP, SonarQube), build the image, and push it to DockerHub (`parthsingh2496/lost-found-ultra:v1.0.X`).

2. **Deploy GitOps Infrastructure:**
   Ensure your cluster has ArgoCD, ArgoCD Image Updater, and ArgoCD Notifications installed.
   ```bash
   # Clone the GitOps Repository
   git clone [https://github.com/Parth2496Singh/Lost-and-Found-GitOps.git](https://github.com/Parth2496Singh/Lost-and-Found-GitOps.git)
   cd Lost-and-Found-GitOps

   # Apply the ArgoCD Notifications ConfigMap (Ensure SMTP secrets are set in your cluster)
   kubectl apply -f gitops/configmap-argocd-noti.yml

   # Apply the Image Updater config
   kubectl apply -f gitops/lostfound-image-updater.yaml

   # Apply the ApplicationSet to initialize the GitOps sync
   kubectl apply -f gitops/list.yml
   ```

3. **Observe the Automation:**
   - ArgoCD will deploy the infrastructure from the GitOps repository.
   - The **Image Updater** will detect the new `v1.0.X` image generated by Jenkins, commit the change back to the GitOps repository, and trigger ArgoCD to sync the new pods automatically.

---

## 🔌 API Endpoints (High-Level)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/lost-items/` | GET / POST | List or create lost items |
| `/api/found-items/` | GET / POST | List or create found items |
| `/api/claims/` | GET / POST | List or create claims |
| `/api/claims/<id>/approve/` | POST | Approve a claim |
| `/api/token/` | POST | Login (JWT token) |

*(All protected endpoints require `Authorization: Bearer <access_token>`)*

---

## 📸 Screenshots

### Home Page
<img width="2876" height="1496" alt="Screenshot from 2026-05-09 18-57-45" src="https://github.com/user-attachments/assets/87b0156f-7ad1-402f-b358-f80ea3f34a67" />

### Login Page
<img width="2876" height="1485" alt="Screenshot from 2026-05-09 18-59-04" src="https://github.com/user-attachments/assets/ee137737-8cd7-488e-8956-01baec977bdd" />

### User Dashboard
<img width="2876" height="1496" alt="Screenshot from 2026-05-09 18-58-13" src="https://github.com/user-attachments/assets/65031713-3534-4d70-9d71-748a34257178" />

### API
<img width="2876" height="986" alt="Screenshot from 2026-05-09 18-58-42" src="https://github.com/user-attachments/assets/b2c3ab75-7d68-4213-9af9-47f117c31e91" />

### Kubernetes Pods
<img width="2854" height="765" alt="Screenshot from 2026-05-09 19-04-35" src="https://github.com/user-attachments/assets/278577f1-e5d9-424c-a03f-7516d8e4131a" />

### Grafana Monitoring
<img width="2872" height="1505" alt="Screenshot from 2026-05-09 19-14-36" src="https://github.com/user-attachments/assets/5f3aaacb-588e-4b9d-a673-309d23a4765f" />

---

## ⚠️ Known Issues / Limitations
- 📱 Mobile UI is not fully optimized for all screen sizes.
- 📧 No email verification during signup.
- 🔐 No rate limiting or account lockout mechanisms yet.

## 🚀 Future Improvements
- ⚙️ Transition CI pipeline from Jenkins to GitHub Actions.
- 🖼️ S3 Integration for image upload support for lost/found items.
- 🔍 Advanced search filters (category, location, date).

---

## 🤝 Contributing & License
1. Fork the repository
2. Create a new feature branch
3. Make your changes and open a Pull Request.

*This project is open-source and intended for educational purposes only.*
