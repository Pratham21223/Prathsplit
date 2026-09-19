from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserResponse

# Service layer: contains the actual database logic, keeping routes clean

def create_user(db: Session, user: UserCreate):
    # Build a new SQLAlchemy model instance from the incoming Pydantic schema
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)      # stage the new row
    db.commit()          # write it to the database
    db.refresh(db_user)  # reload from DB so we get the generated id
    return db_user

def get_users(db: Session):
    # Fetch every row from the users table
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    # Fetch the first user that matches the given id
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user: UserCreate):
    # Find the existing row, then overwrite its fields
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    # Find the row and remove it permanently
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
