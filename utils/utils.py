from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
ALGORITHM = "HS256"
SECRET_KEY = "rahasiasekali"

password_context = CryptContext(schemes=["bcrypt"])

def get_hashed_password(password : str):
    return password_context.hash(password)

def verify_password(password : str, hashed_pass : str):
    return password_context.verify(password, hashed_pass)

def create_accesss_token(subject : Union[str, Any], expires_delta : int = None):
    if expires_delta is None:
        expires_delta = datetime.utcnow() + timedelta(minutes=15)
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp" : expires_delta, "sub" : str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt