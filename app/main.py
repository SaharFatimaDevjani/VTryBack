from fastapi import FastAPI, HTTPException
from .schemas import ProductCreate
from .models import ProductModel
from . import crud

app = FastAPI()

@app.post("/products", response_model=ProductModel)
async def create_product(product: ProductCreate):
    return await crud.create_product(product)

@app.get("/products", response_model=list[ProductModel])
async def get_products():
    return await crud.get_all_products()

@app.get("/products/{id}", response_model=ProductModel)
async def get_product(id: str):
    product = await crud.get_product(id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{id}", response_model=ProductModel)
async def update_product(id: str, product: ProductCreate):
    updated = await crud.update_product(id, product)
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{id}")
async def delete_product(id: str):
    deleted = await crud.delete_product(id)
    if deleted:
        return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
