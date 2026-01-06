from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/api/v1/healt")
async def root():
    return {
        "status": "Everything is OK",
        "database": os.environ.get("DB_NAME")
    }
