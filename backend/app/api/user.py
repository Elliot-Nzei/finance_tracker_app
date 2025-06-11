from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import os
import uuid

from app.models.user import User
from app.services.user_service import save_user, update_user

router = APIRouter()

UPLOAD_DIR = "backend/app/static/uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/login")
async def login(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    profile_img: UploadFile = None
):
    # Save profile image
    filename = None
    if profile_img:
        ext = os.path.splitext(profile_img.filename)[1]
        filename = f"{uuid.uuid4()}{ext}"
        file_path = os.path.join(UPLOAD_DIR, filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(profile_img.file, buffer)

    user = User(name=name, email=email, phone=phone, profile_img=filename)
    save_user(user)

    return JSONResponse(content={"message": "User created", "user": user.dict()})

@router.post("/update")
async def update_profile(
    name: str = Form(None),
    email: str = Form(None),
    phone: str = Form(None),
    profile_img: UploadFile = None
):
    updated_fields = {}
    if name: updated_fields["name"] = name
    if email: updated_fields["email"] = email
    if phone: updated_fields["phone"] = phone

    if profile_img:
        ext = os.path.splitext(profile_img.filename)[1]
        filename = f"{uuid.uuid4()}{ext}"
        file_path = os.path.join(UPLOAD_DIR, filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(profile_img.file, buffer)
        updated_fields["profile_img"] = filename

    updated_user = update_user(updated_fields)
    return JSONResponse(content={"message": "Profile updated", "user": updated_user.dict()})
