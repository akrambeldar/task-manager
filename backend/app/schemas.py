from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"


class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    status: str


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str
    user_id: int

    class Config:
        from_attributes = True