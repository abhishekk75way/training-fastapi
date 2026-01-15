from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str
    priority: int
    completed: bool

class TodoUpdate(BaseModel):
    title: str
    description: str
    priority: int
    completed: bool
    
class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    completed: bool
    created_at: datetime
    
    class Config:
        orm_mode = True
