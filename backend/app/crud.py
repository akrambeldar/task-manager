from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models
from .auth import hash_password


def create_user(db: Session, email: str, password: str):
    hashed_password = hash_password(password)

    user = models.User(email=email, password=hashed_password)
    db.add(user)

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        return None


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_task(db: Session, title: str, description: str | None, status: str, user_id: int):
    task = models.Task(
        title=title,
        description=description,
        status=status,
        user_id=user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(models.Task).all()


def get_tasks_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task(db: Session, task: models.Task, title: str, description: str | None, status: str):
    task.title = title
    task.description = description
    task.status = status
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: models.Task):
    db.delete(task)
    db.commit()