from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Literal

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username of the user")
    email: EmailStr = Field(..., description="Email address of the user")
    role: str = Field("user", description="Role of the user: user or admin")
    model_config = ConfigDict(from_attributes=True)
Role = Literal["admin", "user"]

class UserPublic(UserBase):
    id: int
    role: Role

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username of the user")
    email: EmailStr = Field(..., description="Email address of the user")
    password: str = Field(..., min_length=6,  max_length=50,description="Password for the user")

class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="Email address of the user")
    password: str = Field(..., min_length=6, max_length=50, description="Password for the user")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserPublic
