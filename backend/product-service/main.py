from fastapi import FastAPI, HTTPException
from database import load_products, save_products

app = FastAPI(title="Product Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/products")
def create_product(name: str, price: float, category: str):
    products = load_products()
    product_id = len(products) + 1
    product = {"id": product_id, "name": name, "price": price, "category": category}
    products.append(product)
    save_products(products)
    return product

@app.get("/products/{product_id}")
def get_product(product_id: int):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Not found")
