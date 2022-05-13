from typing import List

from pydantic import BaseModel

from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str


class WorkPlaceSchema(BaseModel):
    user_id: int
    address: str


class UserSchema(BaseModel):
    id: int
    username: str
    workplaces: List[WorkPlaceSchema]
