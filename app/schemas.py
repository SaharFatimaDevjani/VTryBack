from pydantic import BaseModel

class ProductCreate(BaseModel):
    title: str
    description: str
    category: str
    image: str
    price: float
