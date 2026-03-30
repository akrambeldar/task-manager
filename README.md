# 🚀 Full-Stack Task Manager Application

A production-style **full-stack task management application** built with **FastAPI, React, PostgreSQL, Docker, JWT Authentication, and CI/CD**.

This project was designed as a **portfolio-grade software engineering project** to demonstrate backend APIs, authentication, database design, frontend integration, testing, containerization, and modern development workflows.

---

# 📌 Project Overview

This application allows users to:

* Register securely
* Log in using JWT authentication
* Create personal tasks
* View their own tasks
* Edit existing tasks
* Delete tasks
* Persist login sessions using tokens
* Use a polished dashboard UI

Each user can only access **their own tasks**, making the project demonstrate **ownership-based authorization**.

---

# 🏗️ Tech Stack

## Backend

* **FastAPI** – API framework
* **PostgreSQL** – relational database
* **SQLAlchemy** – ORM
* **Pydantic** – schema validation
* **JWT** – secure authentication
* **Passlib + bcrypt** – password hashing
* **Pytest** – backend tests
* **Docker + Docker Compose** – containerization
* **GitHub Actions** – CI pipeline

## Frontend

* **React**
* **Vite**
* **Axios**
* **React Router DOM**
* Custom modern CSS dashboard styling

---

# 🔐 Features Implemented

## ✅ Authentication System

* User registration endpoint
* Secure password hashing
* JWT token generation
* Login endpoint
* Protected routes
* Token-based user session persistence

## ✅ Task Management (Full CRUD)

* Create task
* Read all tasks for logged-in user
* Update task
* Delete task
* Ownership validation

## ✅ Frontend Dashboard

* Login page
* Registration page
* Protected dashboard route
* Create task UI
* Edit task workflow
* Delete task buttons
* Logout support
* Task cards with status badges

## ✅ DevOps / Engineering Workflow

* Dockerized backend + PostgreSQL
* `.env` configuration support
* GitHub Actions CI pipeline
* Automated pytest execution
* Monorepo structure
* Production-ready environment variable setup

---

# 📂 Project Structure

```bash
TASK-MANAGER/
│
├── .github/workflows/
│   └── ci.yml
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── config.py
│   │
│   ├── tests/
│   │   └── test_main.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│
└── docker-compose.yml
```

---

# ⚙️ How It Works

## Backend Flow

1. User registers
2. Password gets hashed using bcrypt
3. User logs in
4. JWT token is generated
5. Frontend stores token in localStorage
6. Protected requests send `Authorization: Bearer <token>`
7. Backend validates token
8. Only user-owned tasks are returned

## Frontend Flow

1. User logs in
2. Token stored in browser
3. Dashboard fetches `/my-tasks`
4. Users can add/edit/delete tasks
5. UI refreshes live after every operation

---

# 🧪 Testing

The backend includes **pytest integration tests** covering:

* User registration
* Login
* JWT authentication
* Protected routes
* Task CRUD operations

Run tests locally:

```bash
cd backend
pytest
```

---

# 🐳 Docker Support

The backend and PostgreSQL database are fully containerized.

Run locally:

```bash
docker-compose up --build
```

This starts:

* FastAPI backend
* PostgreSQL database

---

# 🎯 Key Software Engineering Concepts Demonstrated

* REST API design
* JWT authentication
* secure password storage
* SQL ORM modelling
* CRUD architecture
* route protection
* React state management
* frontend/backend integration
* environment variable management
* CI/CD workflows
* containerization
* production-style project structure

---


# ⭐ Future Enhancements

* Task due dates
* Task priority levels
* Search and filtering
* Team collaboration
* Notifications
* Activity logs
* Production cloud deployment
