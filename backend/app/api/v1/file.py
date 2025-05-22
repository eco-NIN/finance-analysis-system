# @Author  : eco
# @Date    :2025/5/21 21:26
# @Function:
# app/api/v1/file.py

# app/api/v1/file.py

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

router = APIRouter()

# 定义上传目录
UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.get("/test")
def test_file_api():
    return {"message": "File API is working!"}


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "status": "uploaded"}


@router.get("/download/{filename}")
def download_file(filename: str):
    file_path = UPLOAD_DIR / filename
    if file_path.exists():
        return FileResponse(file_path, filename=filename)
    return {"error": "File not found"}


@router.get("/list")
def list_files():
    return {"files": [f.name for f in UPLOAD_DIR.iterdir() if f.is_file()]}