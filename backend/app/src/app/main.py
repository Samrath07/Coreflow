from fastapi import FastAPI  # type: ignore[reportMissingImports]

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}