from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "hello dalle"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/item/{item_id}")
def route(item_id: int):
    return {"item_id" : item_id}

from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def route(category : str , limit: int=10):
    return {"category" : category , "limit" : limit}



# problems
# Q1 (Easy): Ek endpoint banao /users/{user_id} jo path parameter le aur return kare {"user_id": <value>, "status": "active"}.

from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
def route(user_id : int , status: str="active"):
    return {"user_id": user_id, "status" : status}

# Q2 (Easy-Medium): Ek endpoint banao /products jo do query parameters le — category (required, string) aur min_price (optional, float, default 0). Return karo dono values ek dictionary me.

from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def route(category : str,min_price: float=0):
    return {"category" : category,"min_price" : min_price}

# Q3 (Medium): Ek endpoint banao /greet/{name} jo path parameter name (string) aur query parameter age (optional int, default None) dono le. Agar age diya ho to return karo "Hello {name}, you are {age} years old", warna sirf "Hello {name}".

from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
def route(name: str, age: int = None):
    if age is not None:
        return {"message":f"Hello {name}, you are {age} years old"}
    else:
        return {"message": f"Hello {name}"}

