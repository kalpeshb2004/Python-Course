# pydantic model and basemodel 

# GET me path/query params se data aata. POST/PUT me bada data bhejna ho (jaise naya product) to request body use hota — JSON object bhej ke.

# 2. Pydantic BaseModel
from pydantic import Basemodel 

class Product(Basemodel):
    name : str
    price : int
    description : str = None

# 3. POST endpoint with body
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class product(BaseModel):
    name: str
    price: int
    description : str=None

@app.post("/products")
def route(product: product):
    return product

# field validation
from pydantic import BaseModel,Field

class Products(BaseModel):
    name: str
    price: float = Field(gt=0)
    description: str=None

# Q1 (Easy): User Pydantic model banao — fields: username: str, email: str, age: int. POST endpoint /users banao jo User accept kare aur wahi wapas return kare.

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class user(BaseModel):
    username: str
    email: str
    age: int

@app.post("/users")
def route(user: user):
    return user

# Q2 (Easy-Medium): Book model banao — title: str, author: str, price: float, in_stock: bool = True (default). POST /books endpoint banao. Price validation add karo — Field(gt=0) use kar ke price hamesha 0 se zyada ho.

from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    price: float = Field(gt=0)
    in_stock: bool = True

@app.post("/book")
def route(book:Book):
    return book

# Q3 (Medium): Order model banao — item_name: str, quantity: int = Field(gt=0), customer_email: str. POST /orders endpoint banao jo Order le, aur return kare {"message": f"Order placed for {quantity} x {item_name}", "email": customer_email}.

from pydantic import BaseModel , Field
from fastapi import FastAPI

app = FastAPI()

class Order(BaseModel):
    item_name: str 
    quantity: int = Field(gt=0)
    customer_email: str

@app.post("/order")
def route(order: Order):
    return {"message": f"Order placed for {order.quantity} x {order.item_name}", "email": order.customer_email}

