from fastapi import FastAPI,Depends
from model import product
from database import sessionLocal,engine
from sqlalchemy.orm import Session
import database_model


app = FastAPI()

database_model.Base.metadata.create_all(bind=engine) 

@app.get("/")
async def root():
    return {"message": "Hello World"}

products = [
    product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6)
]
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = sessionLocal()

    count = db.query(database_model.product).count

    if count == 0 :
        for product in products:
            db.add(database_model.product(**product.model_dump()))
        db.commit()

init_db()

@app.get("/products")
def get_all_products (db: Session = Depends(get_db)):
    db_products = db.query(database_model.product).all()
    return db_products

@app.get("/product/{idf}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.product).filter(database_model.product.id == id).first()
    if db_product:
        return db_product
    else:
        return "product not found"

@app.post("/product")
def add_product(product: product,db: Session = Depends(get_db)):
    db.add(database_model.product(**product.model_dump()))
    db.commit()
    return product
     

@app.put("/product/{id}")
def update_product(id: int, product: product,db: Session = Depends(get_db)):
    db_product = db.query(database_model.product).filter(database_model.product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
    else:
        return " product NOT found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted succesfully"
    return "product not found"
        