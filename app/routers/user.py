from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from app.schemas import UserCreate, UserCreate_resp
from app.models import Users
from app.database import get_db
from .. import utils

router = APIRouter(
    # prefix="/user"
    tags=["user"]
)

@router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=UserCreate_resp)
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    try:
        hashed_password = utils.Hash(new_user.password)
        new_user.password = hashed_password

        new_user = Users(**new_user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    
@router.get("/user/{id}", response_model=UserCreate_resp)
def get_user(id : int, db: Session = Depends(get_db)):
    
    data = db.query(Users).filter(Users.id == id).first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"requested id {id} was not found!")
    return data