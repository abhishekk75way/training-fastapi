from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr 
    password: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr 
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    
class UserLogout(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True