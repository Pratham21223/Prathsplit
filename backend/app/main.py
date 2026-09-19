from fastapi import FastAPI

from database import Base, engine

# Import models so SQLAlchemy registers them before create_all
from models.user import User  # noqa: F401

# Register all routers (groups of related routes)
from routes.user import router as userRouter

# Creates all tables in the database if they don't already exist
Base.metadata.create_all(bind=engine)

# FastAPI() is the main application instance
app = FastAPI(
    title="PrathSplit API",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to PrathSplit API"
    }


@app.get("/health")
def get_health():
    return {
        "status": "healthy"
    }


# Attach the user router — all its routes become part of the main app
app.include_router(userRouter)