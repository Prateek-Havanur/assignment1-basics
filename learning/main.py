from fastapi import FastAPI
import asyncio

app = FastAPI()


async def dummy_hello_from_llm(name):
    await asyncio.sleep(10)
    return f"hello--{name}"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def get_hello_with_name(name: str):
    result = await dummy_hello_from_llm(name)
    return {"message": result, "param_name": name}
