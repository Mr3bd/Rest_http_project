from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import uvicorn
import os.path

app = FastAPI()


@app.get("/get-env-file", response_class=PlainTextResponse)
async def get_env_file():
    env_path = ".env"

    if not os.path.exists(env_path):
        raise HTTPException(status_code=404, detail=".env file not found.")

    with open(env_path, "r") as file:
        content = file.read()

    return content


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)