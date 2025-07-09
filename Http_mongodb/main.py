from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import uvicorn
import os


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

load_dotenv()

COLLECTION_NAME = "products"

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB = os.getenv("MONGO_DB")

MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]


products_collection = db[COLLECTION_NAME]

app = FastAPI(
)


@app.post("/products")
async def add_product(product: Product):

    product_dict = product.dict()

    result = await products_collection.insert_one(product_dict)

    return {"message": "Product added", "id": str(result.inserted_id)}


@app.get("/products")
async def get_products():

    cursor = products_collection.find({}, {"_id": 0, "name": 1, "price": 1})

    products = await cursor.to_list(length=100)

    return {"products": products}


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)