from fastapi import FastAPI
from routers_day4 import products

app = FastAPI()

app.include_router(products.router)