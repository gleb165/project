from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import EmailStr, BaseModel
from redis_om import get_redis_connection, HashModel
from fastapi.responses import JSONResponse


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:3000'],
                   allow_methods=['*'], allow_headers=['*'])
redis = get_redis_connection(host='redis-14457.c55.eu-central-1-1.ec2.cloud.redislabs.com', port=14457, password='qyg5Z40sC0W77p0eCCk4iGvaCghTIosn', decode_responses=True)


class Product(HashModel):
    name: str
    price: int
    quantity: int

    class Meta:
        database = redis


class CreateProduct(BaseModel):
    name: str
    price: int
    quantity: int


@app.get("/products")
def root():
    return Product.all_pks()


@app.post("/products")
def create(product: CreateProduct):
    product_data = product.dict()
    return Product(**product_data).save()



