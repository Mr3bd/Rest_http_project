from fastapi import FastAPI, HTTPException, Query
import uvicorn
import os.path

app = FastAPI()


@app.get("/read-file/{filename}")
async def read_file(filename: str):

    file_path = filename

    if not os.path.exists(file_path):
        raise HTTPException(status_code = 404, detail="Error, File Not Found!")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            return {"content": content}
    except Exception as e:
        raise HTTPException(status_code = 404, detail=f"Error reading file: {str(e)}")


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)