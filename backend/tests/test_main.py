from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.app.main import app, get_db
from backend.app.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Task Manager API is running"}


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "email": "testuser@example.com",
            "password": "123456"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "testuser@example.com"
    assert "id" in data


def test_login():
    client.post(
        "/users/",
        json={
            "email": "loginuser@example.com",
            "password": "123456"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": "loginuser@example.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_me():
    client.post(
        "/users/",
        json={
            "email": "meuser@example.com",
            "password": "123456"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "email": "meuser@example.com",
            "password": "123456"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/me",
        headers={"authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "meuser@example.com"


def test_create_task_and_get_my_tasks():
    client.post(
        "/users/",
        json={
            "email": "taskuser@example.com",
            "password": "123456"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "email": "taskuser@example.com",
            "password": "123456"
        }
    )

    token = login_response.json()["access_token"]
    headers = {"authorization": f"Bearer {token}"}

    create_task_response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Testing task creation",
            "status": "pending"
        },
        headers=headers
    )

    assert create_task_response.status_code == 200
    task_data = create_task_response.json()
    assert task_data["title"] == "Test Task"

    my_tasks_response = client.get("/my-tasks", headers=headers)

    assert my_tasks_response.status_code == 200
    tasks = my_tasks_response.json()
    assert len(tasks) >= 1
    assert tasks[0]["title"] == "Test Task"