from pydantic import BaseModel
from pydantic import ConfigDict

# Pydantic schemas validate and shape the data coming IN to the API (request body)
class UserCreate(BaseModel):
    name: str
    email: str
    password: str


# This schema shapes the data going OUT of the API (response body)
class UserResponse(BaseModel):
    # Tells Pydantic to read data from SQLAlchemy model attributes, not just dicts
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    password: str