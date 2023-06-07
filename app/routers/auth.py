from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import token, user_login
from app.models import Users
from app.utils import verify_Pass
from app.oauth2 import create_access_token



router = APIRouter(
    # prefix="/post"
    tags=["authentication"]
)

@router.post("/login", response_model=token)
def login(user_credentials:OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials !!")
    
    if not verify_Pass(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials !!")

    token = create_access_token({"user_id" : user.id})
    return {"access_token": token, "token_type":"bearer"}