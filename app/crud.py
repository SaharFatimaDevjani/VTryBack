from .database import db
from .models import ProductModel
from .schemas import ProductCreate
from bson import ObjectId

collection = db.products

async def create_product(product: ProductCreate):
    result = await collection.insert_one(product.dict())
    return await collection.find_one({"_id": result.inserted_id})

async def get_all_products():
    return [ProductModel(**doc) async for doc in collection.find()]

async def get_product(id: str):
    return await collection.find_one({"_id": ObjectId(id)})

async def update_product(id: str, product: ProductCreate):
    await collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": product.dict()}
    )
    return await collection.find_one({"_id": ObjectId(id)})

async def delete_product(id: str):
    result = await collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
