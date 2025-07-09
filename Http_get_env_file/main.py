from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import uvicorn
import os.path
from dotenv import load_dotenv
app = FastAPI()
load_dotenv()  

@app.get("/get-env-file", response_class=PlainTextResponse)
async def get_env_file():
    secret = os.getenv("SECRET_KEY")

    return secret


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)