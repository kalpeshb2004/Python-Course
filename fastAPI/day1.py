# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message" : "hello dalle"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/item/{item_id}")
def get_item(item_id: int):
    return {"item_id" : item_id}
