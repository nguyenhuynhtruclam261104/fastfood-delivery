from fastapi import FastAPI

app = FastAPI()

products = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/product")
def create_product(name: str, price: float):
    product = {"name": name, "price": price}
    products.append(product)
    return {"message": "Product added", "product": product}

@app.get("/products")
def list_products():
    return {"products": products}
