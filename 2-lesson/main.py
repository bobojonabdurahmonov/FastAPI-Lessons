from fastapi import FastAPI

app = FastAPI()

@app.get("/api/register/{username}/{email}/{password}")
async def root(username,email,password):
    user = f"Username : {username}. Email: {email}. Password: {password}"
    return {"status":user}