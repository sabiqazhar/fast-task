from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from Model import models
from Schemas import user
from database import get_db

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/")
async def register(payload: user.UserBaseSchema, db: Session = Depends(get_db)):
    hash_pass = pwd_context.hash(payload.password)
    new_user = models.User(id= payload.id, username = payload.username, email = payload.email, password = hash_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "success", 'code': 200, 'message': 'User Registered'}