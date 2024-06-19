from fastapi import APIRouter, HTTPException, status
from utils.utils import get_db_connection
from models.user_model import user_model
from schemas.UserResponse import login_response
router = APIRouter()


@router.post("/api/login")
def login(user_model: user_model):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (user_model.username, user_model.password))
    user = c.fetchone()
    conn.close()

    if user:
        return login_response(id=user['id'], username=user['username'])
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
