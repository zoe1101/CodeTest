# coding:utf-8
import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


if __name__ == '__main__':
    uvicorn.run(app='请求文件:app', host="127.0.0.1", port=8000, reload=True)