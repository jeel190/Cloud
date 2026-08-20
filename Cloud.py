import os
import requests
import mimetypes
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BUCKET_NAME = "jeelvasani"

def upload_and_download_file(file_path):
    filename = os.path.basename(file_path)
    
    # Automatically detect file content type (e.g., application/pdf, image/jpeg)
    content_type, _ = mimetypes.guess_type(file_path)
    if not content_type:
        content_type = "application/octet-stream"

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": content_type
    }

    # 1. Upload File
    with open(file_path, "rb") as f:
        res = requests.post(
            f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{filename}",
            headers=headers,
            data=f
        )
    print(f"--- Uploading {filename} ---")
    print("Upload Status:", res.status_code)
    print("Upload Response:", res.text)

    # 2. Download File
    res_download = requests.get(
        f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{filename}",
        headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
    )
    print("Download Status:", res_download.status_code)
    print("Download Response Length (bytes):", len(res_download.content))
    print("-" * 30)


upload_and_download_file("DOC.pdf")