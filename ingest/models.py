from pydantic import BaseModel, Field
from typing import List
from datetime import date

class Item(BaseModel):
    product: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

class Invoice(BaseModel):
    order_id: str
    date: date
    customer_id: str
    items: List[Item]
