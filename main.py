from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root():
    return {"status":"not found"}