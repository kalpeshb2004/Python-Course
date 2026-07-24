# Day 4: Routers + Project Structure
# 1. Kyu chahiye

# Bade app me sab kuch ek file (main.py) me likhna messy ho jata. APIRouter se code alag files me split karte, phir jodte.

# 2. Basic Structure
# myapp/
# ├── main.py
# ├── routers/
# │   ├── __init__.py
# │   ├── items.py
# │   └── users.py

# 3. Router file (routers/items.py)
# from fastapi import APIRouter
# from fastapi import FastAPI

# app = FastAPI()

# router = APIRouter(prefix="/itmes" , tags=["items"])

# items = {1:"pen", 2:"book"}

# @router.get("/")
# def get_item():
#     return items

# @router.get("/{item_id}")
# def get_item(item_id: int):
#     return items.get(item_id, "not Found")

# app.include_router(router) #include_router : har router ko main app me plug karta.

# prefix="/items" — is router ke saare routes automatically /items se start honge. 
# @router.get("/") actually /items/ ban jayega.
# tags=["items"] — /docs me routes group ho ke dikhenge, clean UI.

# 4. Router file (routers/users.py)
from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter(prefix="/item",tags=["users"])

users = {1: "Aman" , 2: "Riya"}

@router.get("/")
def route():
    return users

app.include_router(router)






