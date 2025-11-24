from fastapi import FastAPI
from model import product
from database import sessionLocal 
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

products = [
    product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6)
]

@app.get("/products")
def get_all_products ():
    db = sessionLocal()
    db.query()
    return products

@app.get("/product/{idf}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product: product):
    products.append(product)
    return product
     

@app.put("/product")
def update_product(id: int, product: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated"
    return "no product found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted succesfully"
    return "product not found"
        