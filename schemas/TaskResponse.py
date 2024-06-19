from pydantic import BaseModel
from models.task_model import Task


class task_response(BaseModel):
    id: int
    title: str
