from pydantic import BaseModel,EmailStr

class User(BaseModel,EmailStr) :
    name : str
    email : EmailStr
    password : str