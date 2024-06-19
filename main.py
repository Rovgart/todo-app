import os
import sqlite3
from fastapi import FastAPI
from sqlite3 import connect
from fastapi.middleware.cors import CORSMiddleware
from routers import login, tasks, user
app = FastAPI()

# Assuming the path to your database file
db_path = "todo.db"

# Check if the file exists before connecting
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    print("Connected to SQLite database")
else:
    print(f"Error: Database file '{db_path}' not found.")
conn = connect('todo.db')
c = conn.cursor()

# Task table
c.execute(
    '''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL)''')
# Create todos table
c.execute('''
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    task TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

# Create users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')


conn.commit()
conn.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


app.include_router(login.router)
app.include_router(user.router)
app.include_router(tasks.router)

origins: list[str] = ["*"]  # i love CORS


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
