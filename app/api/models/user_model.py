from pydantic import BaseModel, EmailStr

# Incoming data for user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Response model for user details
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
