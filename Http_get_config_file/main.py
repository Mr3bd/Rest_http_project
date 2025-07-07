from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import uvicorn
import os.path

app = FastAPI()


@app.get("/get-config-file", response_class=PlainTextResponse)
async def get_env_file():
    config_path = "config.ini"

    if not os.path.exists(config_path):
        raise HTTPException(status_code=404, detail="config file not found.")

    with open(config_path, "r") as file:
        content = file.read()

    return content


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)