from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import TodoCreate, TodoResponse, TodoUpdate
from services import TodoService
from config.db import get_db

router = APIRouter()

@router.post("/todos", response_model=TodoResponse)
async def create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    todo_service = TodoService(db)
    return await todo_service.create_todo(todo)

@router.get("/todos", response_model=List[TodoResponse])
async def get_todos(db: AsyncSession = Depends(get_db)):
    todo_service = TodoService(db)
    return await todo_service.get_todos()

@router.get("/todos/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    todo_service = TodoService(db)
    return await todo_service.get_todo(todo_id)

@router.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo: TodoUpdate, db: AsyncSession = Depends(get_db)):
    todo_service = TodoService(db)
    return await todo_service.update_todo(todo_id, todo)