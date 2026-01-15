from fastapi import FastAPI
from config.config import settings
from config.db import engine, Base
from routers import auth_router, todo_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(auth_router)
app.include_router(todo_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("Database connected")