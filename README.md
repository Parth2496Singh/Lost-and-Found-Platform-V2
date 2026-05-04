# 🚀 Lost & Found Platform (V2 & DevOps Updates)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![Docker Compose](https://img.shields.io/badge/Docker_Compose-003F8C?style=for-the-badge&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) ![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

A full-stack Lost & Found web application with modern DevOps integration including Docker, Nginx, Kubernetes, and Helm support.

---

## 📑 Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Project Structure](#project-structure)  
5. [Installation & Setup](#installation--setup)  
   - Method 1: Local Development  
   - Method 2: Docker & Docker Compose  
   - Method 3: Automated EC2 Deployment  
   - Method 4: Kubernetes & Helm (KIND)  
6. [Usage](#usage)  
7. [API Endpoints](#api-endpoints)  
8. [Known Issues / Limitations](#known-issues--limitations)  
9. [Future Improvements](#future-improvements)  
10. [Contributing](#contributing)  
11. [License](#license)

---

## 📌 Project Overview

The **Lost & Found Platform** is a full-stack web application that enables users to report lost and found items, claim items, and track their submissions efficiently.

### ⚙️ Recent DevOps Upgrade (V2+)

This project now includes modern DevOps practices:

- Fully containerized application using **Docker**
- Production-ready routing using **Nginx reverse proxy**
- Automated deployment on **AWS EC2 via Bash script**
- Kubernetes manifests for orchestration
- Custom **Helm chart** for local KIND cluster deployments

This project was built for hands-on learning of:
- Django backend development
- REST API design
- Cloud-native DevOps workflows
- Container orchestration systems

---

## ✨ Features

### 🧩 V1 (Base Version)
- Report lost items
- Report found items
- Dashboard for viewing lost/found items
- Basic item cards and UI

---

### ⚡ V2 (Application Upgrade)
- 🔐 JWT Authentication (Login / Signup)
- 📦 Full claim system (claim found items)
- ✅ Approve / ❌ Reject claims workflow
- 🔔 In-app notifications for claim updates
- 👤 User-specific dashboard (lost & found tracking)
- 🎨 Dynamic frontend using Vanilla JavaScript (API-driven UI)

---

### 🚀 V3 (DevOps & Infrastructure Enhancements)

#### 🐳 Containerization
- Complete Docker setup using `Dockerfile`
- Multi-service orchestration using `docker-compose`

#### 🌐 Reverse Proxy
- Nginx configured as a reverse proxy
- Secure routing of traffic to application (port 80)

#### ☁️ AWS EC2 Automation
- Automated EC2 deployment via `deploy.sh`
- Installs Docker automatically
- Clones repository and runs application via Docker Compose

#### ☸️ Kubernetes Support
- Full Kubernetes manifests included:
  - Namespace
  - Deployment
  - Service
  - Horizontal Pod Autoscaler (HPA)
  - HTTPRoute & Gateway API resources

#### 📦 Helm Integration
- Custom Helm chart (`helm/lostfound`)
- Ready for deployment on local KIND cluster

---

## 🧰 Tech Stack

### 🖥️ Backend
- Python 🐍
- Django
- Django REST Framework

### 🎨 Frontend
- HTML5
- CSS3
- Bootstrap 5
- Vanilla JavaScript (API-driven UI)

### 🗄️ Database
- SQLite (Development)

### ⚙️ DevOps & Infrastructure
- Docker
- Docker Compose
- Nginx (Reverse Proxy)
- Bash scripting (EC2 automation)

### ☸️ Orchestration
- Kubernetes (KIND cluster)
- Helm Charts
- Gateway API

### 🔧 Version Control
- Git
- GitHub


## 📁 Project Structure

```
accounts/           # User models and authentication logic
api/                # REST API endpoints and serializers
frontend/           # HTML templates + static frontend assets
helm/               # Helm chart (generated using `helm create`)
k8s/                # Kubernetes manifests (Deployment, Service, HPA, etc.)
nginx/              # Nginx reverse proxy configuration
reports/            # Lost & Found item models and logic
LostFoundProject/   # Django project settings and configuration

deploy.sh           # Automated EC2 deployment script
docker-compose.yml  # Multi-container Docker setup
Dockerfile          # Django app containerization instructions
manage.py           # Django management utility
requirements.txt    # Python dependencies

```

## ⚙️ Installation & Setup

You can run this project using any of the following methods:

---

## 🏠 Method 1: Local Development

1. Clone the repository  
`git clone https://github.com/Parth2496Singh/Lost-and-Found-Platform-V2.git`  
`cd Lost-and-Found-Platform-V2`

2. Create virtual environment  
`python -m venv env`

3. Activate environment  
- Windows: `env\Scripts\activate`  
- Linux/Mac: `source env/bin/activate`

4. Install dependencies  
`pip install -r requirements.txt`

5. Apply migrations  
`python manage.py migrate`

6. Run server  
`python manage.py runserver`

---

## 🐳 Method 2: Docker & Docker Compose

1. Clone repository  
`git clone https://github.com/Parth2496Singh/Lost-and-Found-Platform-V2.git`  
`cd Lost-and-Found-Platform-V2`

2. Build and run containers  
`docker-compose up -d --build`

3. Open application  
http://localhost

---

## ☁️ Method 3: Automated EC2 Deployment

1. SSH into EC2 instance

2. Run deployment script  
`bash deploy.sh`

3. Access application  
http://<EC2-PUBLIC-IP>

What happens:
- Docker gets installed
- Repo is cloned
- Containers are built and started

---

## ☸️ Method 4: Kubernetes & Helm (KIND Cluster)

1. Create cluster  
`kind create cluster --name lostfound-cluster`

2. Apply Kubernetes manifests  
`kubectl apply -f k8s/`

3. Deploy using Helm  
`cd helm/lostfound`  
`helm install lostfound-release .`


## 🚀 Usage

1. Sign up for an account  
2. Log in to access the dashboard  
3. Report lost or found items  
4. View your submitted items  
5. Claim a found item if it matches your lost item  
6. Approve or reject claims (for item owners)  
7. Receive in-app notifications for updates  

---

## 🔌 API Endpoints (High-Level)

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/lost-items/ | GET / POST | List or create lost items |
| /api/found-items/ | GET / POST | List or create found items |
| /api/lost-items/<id>/matches/ | GET | Get matching found items |
| /api/claims/ | GET / POST | List or create claims |
| /api/claims/<id>/approve/ | POST | Approve a claim |
| /api/claims/<id>/reject/ | POST | Reject a claim |
| /api/token/ | POST | Login (JWT token) |
| /api/token/refresh/ | POST | Refresh JWT token |

📌 Note:  
All protected endpoints require:  
`Authorization: Bearer <access_token>`

---

## ⚠️ Known Issues / Limitations

- 📱 Mobile UI is not fully optimized for all screen sizes  
- 📧 No email verification during signup (fake accounts possible)  
- 🔍 Limited search and filtering options  
- 🔔 Notifications are only in-app (no email/push notifications)  
- 🔐 No rate limiting or account lockout mechanisms yet  

---

## 🚀 Future Improvements

- 📱 Fully responsive mobile UI redesign  
- 📧 Email verification system for authentication  
- 🔍 Advanced search filters (category, location, date)  
- 🔔 Email + push notifications system  
- 🔐 Security upgrades (rate limiting, account lockout, JWT improvements)  
- 🖼️ Image upload support for lost/found items  
- ⚙️ CI/CD pipeline using GitHub Actions  
- 📦 Automated Docker image publishing  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a new feature branch  
3. Make your changes  
4. Commit and push your branch  
5. Open a pull request  

---

## 📄 License

This project is open-source and intended for educational purposes only.
