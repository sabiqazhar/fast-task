from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBaseSchema(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class LoginBaseSchema(BaseModel):
    email: str
    password: str
