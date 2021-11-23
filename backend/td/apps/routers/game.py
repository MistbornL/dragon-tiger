from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends, status

from fastapi.security import OAuth2PasswordRequestForm

from td.apps.documents.document import Game, User
from td.apps.auth.auth import authenticate_user, create_access_token, get_password_hash, get_current_user
from td.config import settings
from td.apps.models.models import Token


router = APIRouter(prefix="")


@router.post("/signup")
async def signup(user_data: User):
    user_data.password = get_password_hash(user_data.password)
    await user_data.save()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/api/create/post", status_code=201, response_model=Game)
async def create_post(item: Game, current_user: User = Depends(get_current_user)):
    return await item.save()


@router.get("/api/get/all/post")
async def get_all():
    return await Game.find_all().to_list()