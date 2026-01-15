from sqlalchemy.ext.asyncio import AsyncSession
from models import Todo
from schemas import TodoCreate, TodoResponse
from typing import Optional

class TodoService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_todo(self, todo: TodoCreate) -> TodoResponse:
        db_todo = Todo(**todo.dict())
        self.db.add(db_todo)
        await self.db.commit()
        await self.db.refresh(db_todo)
        return TodoResponse.from_orm(db_todo)

    async def get_todo(self, todo_id: int) -> Optional[TodoResponse]:
        db_todo = await self.db.get(Todo, todo_id)
        if not db_todo:
            return None
        return TodoResponse.from_orm(db_todo)

    async def get_todos(self) -> List[TodoResponse]:
        db_todos = await self.db.execute(select(Todo))
        db_todos = db_todos.scalars().all()
        return [TodoResponse.from_orm(db_todo) for db_todo in db_todos]

    async def update_todo(self, todo_id: int, todo: TodoUpdate) -> Optional[TodoResponse]:
        db_todo = await self.db.get(Todo, todo_id)
        if not db_todo:
            return None
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        await self.db.commit()
        await self.db.refresh(db_todo)
        return TodoResponse.from_orm(db_todo)