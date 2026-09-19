from fastapi import FastAPI

from database import Base, engine

# Import models so SQLAlchemy registers them
from models.user import User

Base.metadata.create_all(bind=engine)

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