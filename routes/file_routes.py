import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

file_router = APIRouter(tags=["File"])

UPLOAD_DIR = "static/files"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@file_router.post("/upload")
async def upload_file(file: UploadFile=File(...)):
    file_path=f"{UPLOAD_DIR}/{file.filename}"
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    return{"msg" : "업로드 성공", "filename" : file.filename}

@file_router.get("/")
async def get_files():
    files = os.listdir(UPLOAD_DIR)
    if not files:
        raise HTTPException(status_code=404, detail="파일이 없습니다")
    return {"files": files}

@file_router.get("/download")
async def download_file(filename: str):
    file_path=f"{UPLOAD_DIR}/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=filename)
    raise HTTPException(status_code=404, detail="파일이 없습니다")

