from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import users_database
from .utils import SECRET_KEY, ALGORITHM
from schemas.token import TokenPayload
from jose import jwt, JWTError

reusable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)

async def get_current_user(token : str = Depends(reusable_oauth)):
    crendentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate" : "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        subject : str = payload.get("sub")
        if subject is None:
            raise crendentials_exception
    except JWTError as e:
        raise crendentials_exception
    user = users_database.get_single_user(subject)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    return user