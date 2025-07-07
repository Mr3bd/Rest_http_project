from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import configparser
import os
import uvicorn

app = FastAPI()

CONFIG_PATH = "config.ini"

def get_config_value(section: str, key: str) -> str:
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("Config file not found.")

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    if section not in config:
        raise KeyError(f"Section '{section}' not found.")

    if key not in config[section]:
        raise KeyError(f"Key '{key}' not found in section '{section}'.")

    return config[section][key]

@app.get("/get-config-value", response_class=PlainTextResponse)
async def get_config_value_api(section: str, key: str):
    try:
        value = get_config_value(section, key)
        return value
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


## Ex: http://127.0.0.1:8000/get-config-value?section=app&key=name