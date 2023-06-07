from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app.schemas import PostCreate, Response_post
from app.models import Posts
from app.database import get_db
from app.oauth2 import get_current_user

router = APIRouter(
    # prefix="/post"
    tags=["post"]
)

@router.get("/post", response_model=List[Response_post])
def post(db: Session = Depends(get_db)):
    post_data = db.query(Posts).all()
    return post_data

@router.get("/post/{id}", response_model=Response_post)
def get_post(id : int, db: Session = Depends(get_db)):
    
    data = db.query(Posts).filter(Posts.id == id).first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"requested id {id} was not found!")
    return data


@router.post("/create_post", status_code=status.HTTP_201_CREATED, response_model=Response_post)
def create_post(new_post: PostCreate, db: Session = Depends(get_db), user_email: str = Depends(get_current_user)):
    print(user_email)
    new_data = Posts(**new_post.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@router.delete("/post/{id}")
def delete_post(id : int, db: Session = Depends(get_db)):
   
    post_for_delete = db.query(Posts).filter(Posts.id == id)

    if not post_for_delete.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"requested id {id} for delete was not found!")
    
    post_for_delete.delete(synchronize_session=False)
    db.commit()
    return {"detail":"removed data"}
    

@router.put("/post/{id}")
def update_post(id : int, updated_post: PostCreate, db: Session = Depends(get_db)):

    post_for_update = db.query(Posts).filter(Posts.id == id)

    if not post_for_update.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"requested id {id} for update was not found!")
    
    post_for_update.update(updated_post.dict(), synchronize_session=False)
    db.commit() 
    return {"detail":f"updated data is {post_for_update.first().__dict__}"}
