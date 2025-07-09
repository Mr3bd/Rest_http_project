from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import configparser
import os
import uvicorn

app = FastAPI()

def get_config_value(section: str, key: str) -> str:
    if not os.path.exists("config.ini"):
        raise FileNotFoundError("Config file not found.")

    config = configparser.ConfigParser()
    config.read("config.ini")

    return config[section][key]
    


@app.get("/get-config-value")
async def get_config_value_api():

    name=get_config_value("app", "name")

    return name


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


## Ex: http://127.0.0.1:8000/get-config-value