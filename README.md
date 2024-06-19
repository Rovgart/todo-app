# ToDoList Backend

This is the backend service for the ToDoList application, built using FastAPI. The backend provides functionalities for user authentication (login and signup) and managing todos (adding, deleting, and fetching todos for users).

## Features

- **User Registration**: Create a new user account.
- **User Login**: Authenticate an existing user.
- **Add Todo**: Add a new todo item for the authenticated user.
- **Delete Todo**: Delete an existing todo item for the authenticated user.
- **Fetch Todos**: Retrieve all todo items for the authenticated user.

## Requirements

- Python 3.7+
- SQLite3

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/todolist-backend.git
    cd todolist-backend
    ```

2. **Create a virtual environment and activate it**:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the SQLite database**:

    ```sh
    python setup_db.py
    ```

    *Note: `setup_db.py` is a script you should create to initialize your database with the necessary tables. See below for a sample script.*

## Running the Application

1. **Start the FastAPI server**:

    ```sh
    uvicorn main:app --reload
    ```

2. The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### User Endpoints

- **Register a new user**

    ```
    POST /api/user/register
    ```

    **Request Body**:

    ```json
    {
        "username": "exampleuser",
        "password": "examplepassword"
    }
    ```

    **Response**:

    ```json
    {
        "message": "User created"
    }
    ```

- **Login an existing user**

    ```
    POST /api/login
    ```

    **Request Body**:

    ```json
    {
        "username": "exampleuser",
        "password": "examplepassword"
    }
    ```

    **Response**:

    ```json
    {
        "id": 1,
        "username": "exampleuser"
    }
    ```

### Todo Endpoints

- **Add a new todo**

    ```
    POST /api/todos
    ```

    **Request Body**:

    ```json
    {
        "user_id": 1,
        "task": "New Todo Item"
    }
    ```

    **Response**:

    ```json
    {
        "id": 1,
        "task": "New Todo Item",
        "user_id": 1
    }
    ```

- **Delete an existing todo**

    ```
    DELETE /api/todos/{todo_id}
    ```

    **Response**:

    ```json
    {
        "message": "Todo deleted"
    }
    ```

- **Fetch all todos for a user**

    ```
    GET /api/todos/{user_id}
    ```

    **Response**:

    ```json
    [
        {
            "id": 1,
            "task": "New Todo Item",
            "user_id": 1
        }
    ]
    ```

## Database Setup Script (`setup_db.py`)

Here is a sample script to set up your SQLite database:

```python
import sqlite3

def create_tables():
    conn = sqlite3.connect("db/todo.db")
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
