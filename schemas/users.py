from pydantic import BaseModel, Field

class User(BaseModel):
    name : str
    email : str
    username : str
    password : str
    is_active : bool = Field(
        default=True, title="Check user is active or not"
    )

class UserLogin(BaseModel):
    username : str
    password : str