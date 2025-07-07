from fastapi import FastAPI, HTTPException
import uvicorn
import os

app = FastAPI()

@app.get("/get-env/{var_name}")
async def get_env_variable(var_name: str):
    value = os.environ.get(var_name)
    if value is None:
        raise HTTPException(status_code=404, detail=f"Environment variable '{var_name}' not found.")
    return {var_name: value}


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)