import os
import requests
import base64
import tempfile
import shutil
from dotenv import load_dotenv
from gptpdf import parse_pdf as call_parse_pdf
import aiofiles
import aiohttp
import asyncio

load_dotenv()

API_KEY = os.getenv('AZURE_OPENAI_KEY')
BASE_URL = os.getenv('AZURE_OPENAI_BASE_URL')


async def download_pdf(url: str) -> str:
    # 使用 base64 编码 URL 生成文件夹名
    folder_name = base64.urlsafe_b64encode(url.encode()).decode('utf-8')
    cache_dir = os.path.join(tempfile.gettempdir(), folder_name)
    filename = os.path.basename(url)
    filepath = os.path.join(cache_dir, filename)
    
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    if not os.path.exists(filepath):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    async with aiofiles.open(filepath, 'wb') as f:
                        await f.write(content)
                else:
                    raise Exception(f"Failed to download PDF: {response.status}")

    return filepath


async def parse_pdf(filepath: str) -> str:
    # 使用临时目录存储解析输出
    output_dir = tempfile.mkdtemp()
    filename = f"{os.path.basename(filepath)}.md"
    
    content, image_paths = call_parse_pdf(
        filepath,
        api_key=API_KEY,
        base_url=BASE_URL,
        model='azure_gpt-4o',
        verbose=False,
        gpt_worker=4,
        output_dir=output_dir
    )

    output_md = os.path.join(output_dir, filename)
    async with aiofiles.open(output_md, 'w') as f:
        await f.write(content)

    return output_md, filename


def cleanup_temp_directory(directory: str):
    """删除临时目录"""
    if os.path.exists(directory):
        shutil.rmtree(directory)
