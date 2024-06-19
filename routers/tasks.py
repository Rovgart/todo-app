import datetime
from fastapi import APIRouter
from schemas.TaskResponse import task_response
from utils.utils import get_db_connection
router = APIRouter()


@router.post("/api/task/add_task")
def add_task(user_id, task: task_response) -> task_response:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO todos (user_id, title,created_at) VALUES (?,?,?)",
              (user_id, task.title, datetime.now()))
    conn.commit()
    conn.close()


@router.delete("/api/task/delete_task/{task_id}")
def delete_task(task_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE id=?", (task_id,))
    conn.commit()
    conn.close()


@router.post("/api/tasks/{user_id}")
def get_user_todos(user_id) -> list[task_response]:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM todos WHERE user_id=?", (user_id,))
    todos = c.fetchall()
    conn.close()
    return todos
