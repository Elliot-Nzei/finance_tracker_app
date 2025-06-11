from fastapi import APIRouter, Form, UploadFile, File
from backend.app.models.user import User
import uuid
import shutil

router = APIRouter()

@router.post("/login")
def login(name: str = Form(...), email: str = Form(...), phone: str = Form(...), profile_img: UploadFile = File(...)):
    user_id = str(uuid.uuid4())
    filepath = f"backend/app/static/uploads/{user_id}_{profile_img.filename}"
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(profile_img.file, buffer)
    return {"id": user_id, "name": name, "email": email, "phone": phone, "profile_img": filepath}
