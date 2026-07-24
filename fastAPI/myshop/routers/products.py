from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

products = {1: "pen", 2: "narayan", 3: "ganja"}

@router.get("/")
def route():
    return products

@router.get("/{product_id}")
def route1(product_id: int):
    return products.get(product_id, "Not found")


