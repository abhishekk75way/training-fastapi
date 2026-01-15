from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import UserCreate, UserResponse
from services import UserService
from config.db import get_db

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    return await user_service.create_user(user)

@router.post("/login", response_model=UserResponse)
async def login(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    return await user_service.create_user(user)

