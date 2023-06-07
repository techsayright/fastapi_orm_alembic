from fastapi import FastAPI, Depends, status, HTTPException
from app.routers.post import post
from sqlalchemy.orm import Session
import sqlalchemy.sql.expression
from app.oauth2 import get_current_user
from .database import engine, get_db
from . import models
from .routers import post, user, auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from app.models import Users
from app.utils import verify_Pass

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.openapi_url = ""

@app.get("/custom_docs", response_class=HTMLResponse)
async def get_custom_docs(db: Session = Depends(get_db), username: str = "xyz@mail.com", password: str = "password"):
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Custom Docs",
            version="1.0.0",
            description="Custom Swagger UI documentation",
            routes=app.routes,
        )
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    user = db.query(Users).filter(Users.email == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials !!")
    
    if not verify_Pass(password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials !!")
    
    app.openapi = custom_openapi

    return get_swagger_ui_html(openapi_url="/openapi.json", title="Custom Docs")

origins = [
   "https:www.google.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router) 
