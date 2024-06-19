from pydantic import BaseModel


class user_response(BaseModel):
    message: str


class login_response(BaseModel):
    id: int
    username: str
