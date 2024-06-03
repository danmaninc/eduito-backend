from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserCreateResponse(UserBase):
    id: int
    is_verified: bool

class User(UserBase):
    id: int
    is_verified: bool