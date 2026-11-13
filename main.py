import uvicorn
from fastapi import FastAPI
from routes.file_routes import file_router

app = FastAPI()

app.include_router( file_router , prefix="/files")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
