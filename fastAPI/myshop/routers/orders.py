# Q2 (Easy-Medium): Same project me routers/orders.py add kar — GET / (sab orders) aur POST / (naya order add, Pydantic model use kar). prefix="/orders" rakh. main.py me dono routers include_router se jod.

from fastapi import APIRouter
from pydantic import BaseModel

router  = APIRouter(prefix="/orders", tags=["orders"])

class order(BaseModel):
    order_id: int
    quantity: int

orders = []

@router.get("/")
def get_order():
    return orders

@router.post("/")
def create_order(order: order):
    order.append(order)
    return order