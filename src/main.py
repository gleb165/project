from fastapi import FastAPI
from pydantic import EmailStr

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: EmailStr):
    return {"message": f"Hello {EmailStr}"}