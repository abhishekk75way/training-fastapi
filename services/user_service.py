from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from schemas import UserCreate, UserResponse
from typing import Optional

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: UserCreate) -> UserResponse:
        db_user = User(**user.dict())
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return UserResponse.from_orm(db_user)

    async def get_user(self, user_id: int) -> Optional[UserResponse]:
        db_user = await self.db.get(User, user_id)
        if not db_user:
            return None
        return UserResponse.from_orm(db_user)

    async def get_user_by_username(self, username: str) -> Optional[UserResponse]:
        db_user = await self.db.execute(select(User).where(User.username == username))
        db_user = db_user.scalar_one_or_none()
        if not db_user:
            return None
        return UserResponse.from_orm(db_user)

    async def get_users(self) -> List[UserResponse]:
        db_users = await self.db.execute(select(User))
        db_users = db_users.scalars().all()
        return [UserResponse.from_orm(db_user) for db_user in db_users]