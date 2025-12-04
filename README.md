# Lost & Found Platform (V2) ![Status](https://img.shields.io/badge/status-active-brightgreen) ![Version](https://img.shields.io/badge/version-2.0-blue)


## Table of Contents

1. Project Overview
2. Features
3. Tech Stack
4. Project Structure
5. Installation & Setup
6. Usage
7. API Endpoints
8. Known Issues / Limitations
9. Future Improvements
10. Contributing
11. License

---

## 1. Project Overview

Lost & Found Platform is a full-stack web application that allows users to report lost and found items, claim items, and track their own lost/found items.

**V2 Introduces:**

* JWT-based authentication (login/signup)

* Claims system to match lost and found items

* User dashboard for managing reports and notifications

This platform was designed for educational purposes and hands-on experience with Django, Django REST Framework, and modern frontend interactivity

## 2. Features

**V1 (Base version):**

* Report lost items

* Report found items

* Basic item cards and UI

**V2 (Current version):**

* JWT authentication (login/signup)

* Full claims system (claim a found item, approve/reject claims)

* Notifications for claims

* User-specific dashboard with lost/found items

* Dynamic frontend with vanilla JS for fetching API data

* Polished UI with floating triangle animations, responsive cards, gradient buttons

## 3. Tech Stack

* **Backend:** Django, Django REST Framework  
* **Frontend:** HTML, CSS, Bootstrap 5 (fully AI-generated)  
* **Database:** SQLite (development)  
* **Version Control:** Git, GitHub

## 4. Project Structure

```
accounts/       # User models and authentication
api/            # API endpoints and serializers
frontend/       # AI-generated frontend templates & static files
reports/        # Lost/Found item models
LostFoundProject/  # Django project settings & URLs
manage.py       # Django management script
requirements.txt # Python dependencies
```

---

## 5. Installation & Setup

1. Clone the repository:

```bash
git clone <repo-url>
cd Lost-and-Found-Platform-V1
```

2. Create a virtual environment:

```bash
python -m venv env
```

3. Activate the environment:

* **Windows:** `env\Scripts\activate`  
* **Linux/Mac:** `source env/bin/activate`

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Start the server:

```bash
python manage.py runserver
```

---

## 6. Usage

1. Sign up for an account

2. Log in to access the dashboard

3. Report lost or found items

4. View your lost/found items and claims

5. Claim a found item if it matches your lost item

6. Approve or reject claims on your found items

7. Receive notifications for claims


## 7. API Endpoints (High-Level)

| Endpoint                       | Method     | Description                    |
|--------------------------------|-----------|--------------------------------|
| /api/lost-items/               | GET/POST  | List/Create lost items         |
| /api/found-items/              | GET/POST  | List/Create found items        |
| /api/lost-items/<id>/matches/  | GET       | Get matching found items       |
| /api/claims/                   | GET/POST  | List/Create claims             |
| /api/claims/<id>/approve/      | POST      | Approve a claim                |
| /api/claims/<id>/reject/       | POST      | Reject a claim                 |
| /api/token/                    | POST      | Login (returns JWT)            |
| /api/token/refresh/            | POST      | Refresh JWT                    |

> **Note:** All endpoints except login/signup require `Authorization: Bearer <access_token>`


## 8. Known Issues / Limitations

- **Mobile UI:** The user interface is not fully optimized for all mobile devices; some elements may appear misaligned.  
- **Email Verification:** Signup does not include email verification, so fake accounts could be created.      
- **Search & Filters:** Currently, search functionality is limited to dashboard only; there are no advanced filters by category, location, or date.  
- **Notifications:** Notifications are limited to in-app messages; no email or push notifications yet.  
- **Security:** While JWT authentication is implemented, additional security features like rate limiting or account lockout are not yet in place.

## 9. Future Improvements

- **Mobile UI Enhancements:** Fully optimize the platform for mobile devices with responsive layouts and better touch interactions.  
- **Email Verification:** Add email verification during signup to prevent fake accounts.  
- **Advanced Search & Filters:** Implement search filters by category, location, date, and keywords.  
- **Notifications:** Add email and push notifications for claims and updates.  
- **Security Enhancements:** Introduce rate limiting, account lockout mechanisms, and improved JWT handling.  
- **Image Uploads:** Allow users to attach images when reporting lost or found items for easier identification.    

## 10. Contributing

1. Fork the repository  
2. Create a new branch for changes  
3. Commit your changes  
4. Push to your branch and create a pull request

---

## 11. License

This project is open-source for educational purposes.



