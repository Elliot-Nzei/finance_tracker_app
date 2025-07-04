from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    profile_img: str