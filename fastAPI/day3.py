# Day 3: Status Codes, Error Handling, Response Models

# 1. HTTPException
# Jab kuch galat ho (item na mile, invalid input), proper error response bhejna:

# from fastapi import FastAPI,HTTPException

# app = FastAPI()

# items = {1:"pen",2:"book",3:"namak"}

# @app.get("/item/{item_id}")
# def route(item_id : int):
#     if item_id not in items:
#         raise HTTPException(status_code=404,detail="Item not found")
#     return {"item_id" : item_id, "name" : items[item_id]}


# # Custom status set karna:
# @app.get("/items",status_code=201)
# def create_items(item:dict):
#     return item

# 3. response_model

# Kabhi input model alag hota, output alag chahiye hota (jaise password hide karna). response_model control karta output shape:

# from pydantic import BaseModel
# from fastapi import FastAPI

# app = FastAPI()

# class userIn(BaseModel):
#     username: str
#     password: str

# class userout(BaseModel):
#     password: str

# @app.post("/register",response_model=userout)
# def register(user: userIn):
#     return user

# FastAPI response ko UserOut shape me convert karega — extra fields (password) drop ho jayenge automatically.

# Practice Questions (Day 3)

# Q1 (Easy): Ek fake DB dict banao students = {1: "Aman", 2: "Riya"}. GET endpoint /students/{student_id} banao — student mile to naam return karo, na mile to 404 with detail "Student not found".

# from fastapi import FastAPI,HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# students = {1: "Aman", 2: "Riya"}

# @app.get("/students/{student_id}")
# def route(student_id: int):
#     if student_id in students:
#         return {"student_name" : students[student_id]}
#     raise HTTPException(status_code=404,detail = "student not found")


# Q2 (Easy-Medium): POST endpoint /register banao. Input model UserIn (username: str, password: str, email: str). Output model UserOut (username: str, email: str — password nahi). response_model=UserOut use karo. Status code 201 set karo.

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class userIn(BaseModel):
#     username: str
#     password: str
#     email: str

# class userOut(BaseModel):
#     username: str
#     email: str

# @app.post("/register",response_model=userOut)
# def route(user: userIn):
#     return user


# Q3 (Medium): Bank balance system banao — fake dict accounts = {"A1": 500, "A2": 1000}. POST endpoint /withdraw/{account_id} banao jo query param amount: float le. Agar account exist nahi → 404. Agar amount > balance → 400 with detail "Insufficient balance". Success pe naya balance return karo.

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

accounts = {"A1": 500, "A2": 1000}

@app.post("/withdraw/{account_id}")
def route(account_id: str,ammount : float):
    if account_id not in accounts:
        raise HTTPException(status_code=404,detail="account not exist")

    if ammount > accounts[account_id]:
        raise HTTPException(status_code=400,detail="insufficient balance")

    accounts[account_id] -= ammount
    return {"account_id" : account_id , "new_balanace": accounts[account_id]}
    


