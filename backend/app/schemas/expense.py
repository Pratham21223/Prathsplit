from pydantic import BaseModel,EmailStr

class Expense(BaseModel,EmailStr):
    title : str
    amount : int
    description : str