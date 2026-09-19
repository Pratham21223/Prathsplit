from fastapi import FastAPI

from database import Base, engine, get_db
from sqlalchemy.orm import Session
from fastapi import Depends

# Import models so SQLAlchemy registers them
from models.user import User
from schemas.user import UserCreate
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

@app.post("/users")
def create_user(
    user : UserCreate,
    db : Session = Depends(get_db)
):
    new_user = User(
        name = user.name,
        email = user.email,
        password = user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user