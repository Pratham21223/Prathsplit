from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()
class User(BaseModel,EmailStr) : # User class is child of BaseModel class for type safety 
    name :str
    email : EmailStr
    password : str

# @ is decorator which mean the inner function gets outer functions super power
@app.get("/")
def home():
    return {"message" : "MY first fastapi app"}

@app.post("/users")
def create_user(user:User) : 
    return user


@app.get("/health")
def getHealth():
    return {"message" : "Working..."}



# Path Paramenter
@app.get("/hello/{name}")
def getName(name:str) :
    return {"msg" : f"Hi,{name}"}


#query parameter
@app.get("/sum")
def sum_numbers(a: float, b: float):
    return {"result": a + b}