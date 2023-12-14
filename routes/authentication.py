from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.users import UserLogin, User
from schemas.token import TokenSchema
from database import users_database
from utils import utils
import re

authRouter = APIRouter()

@authRouter.post("/login", response_model=TokenSchema)
async def login(form_data : OAuth2PasswordRequestForm = Depends()):
    user_check = users_database.get_single_user(username=form_data.username)
    if user_check is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User doesn't exist"
        )
    if not utils.verify_password(password=form_data.password, hashed_pass=user_check["password"]) is True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    return {
        "access_token" : utils.create_accesss_token(user_check["username"])
    }

@authRouter.post("/register")
async def register(new_user : User):
    exist_username = users_database.get_single_user(new_user.username)
    if exist_username:
        raise HTTPException(status_code=400,detail="Username Existed")
    exist_email = users_database.get_single_user_by_email(new_user.email)
    if exist_email:
        raise HTTPException(status_code=400,detail="Email Existed")
    email_regex = re.compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    if email_regex.fullmatch(new_user.email):
        raise HTTPException(status_code=400,detail="Invalid Email")
    password_regex = re.compile("(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})")
    if password_regex.fullmatch(new_user.password):
        raise HTTPException(status_code=400,detail="Password Not Match")
    hashed_password = utils.get_hashed_password(new_user.password)
    new_user.password = hashed_password
    users_database.insert_new_user(new_user)
    return {"message" : "successfull register"}