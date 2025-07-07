from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import configparser
import uvicorn
import os

class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

load_dotenv()
config = configparser.ConfigParser()
config.read("config.ini")

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = config["database"]["name"]
COLLECTION_NAME = config["database"]["collection"]


client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
products_collection = db[COLLECTION_NAME]

app = FastAPI(
    title=config["app"]["name"],
    version=config["app"]["version"]
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