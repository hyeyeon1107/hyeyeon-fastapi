
from pydantic import BaseModel, EmailStr

#user_update_schemas.py

class UserUpdate(BaseModel):
    email : EmailStr | None = None
    name : str | None = None