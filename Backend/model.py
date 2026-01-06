from pydantic import BaseModel
class product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int 
    
class user(BaseModel):
    username: str
    email: str | None = None 
    full_name: str | None = None