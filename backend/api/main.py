from fastapi import FastAPI
from .entry_routes import entry_router
from .user_routes import user_router

app = FastAPI(title="GuestBook Backend", version="1.0")

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(entry_router, prefix="/entries", tags=["entries"])