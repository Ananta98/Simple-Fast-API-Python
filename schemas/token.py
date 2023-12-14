from pydantic import BaseModel
from typing import Optional

class TokenSchema(BaseModel):
    access_token : str

class TokenData(BaseModel):
    username : Optional[str] = None

class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
    user_id : str = None