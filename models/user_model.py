from pydantic import BaseModel


class user_model(BaseModel):
    username: str
    password: str


class user_in_db(BaseModel):
    id: int
    username: str
    password: str
