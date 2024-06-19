from fastapi import APIRouter
from schemas.UserResponse import user_response
from utils.utils import get_db_connection
from models.user_model import user_model
import sqlite3
router = APIRouter()


@router.post("/api/user/register")
def add_user(user_model: user_model) -> user_response:
    conn = get_db_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username,password) VALUES (?,?)",
                  (user_model.username, user_model.password))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return {"message": "User already exists"}
    finally:
        conn.close()
        return {"message": "User created"}
