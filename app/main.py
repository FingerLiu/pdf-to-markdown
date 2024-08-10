from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from app.utils import download_pdf, parse_pdf, cleanup_temp_directory
import os
from urllib.parse import urlparse

app = FastAPI()

@app.get("/")
async def process_pdf(url: str):
    try:
        print(f"received {url}")
        # 下载 PDF
        filepath = await download_pdf(url)
        print(f"downloaed {filepath}")
        
        # 解析 PDF
        output_md, filename = await parse_pdf(filepath)
        print(f"pasred to {filename}")

        # 返回解析后的 Markdown 文件，并在响应后删除临时文件夹
        response = FileResponse(output_md, media_type='text/markdown', filename=filename)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

