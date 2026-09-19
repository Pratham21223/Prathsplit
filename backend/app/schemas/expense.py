from pydantic import BaseModel


class Expense(BaseModel):
    title: str
    amount: int
    description: str