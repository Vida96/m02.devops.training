import sqlite3
import os

DB_NAME = "test_users.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()


def create_user(name, email, age=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    if cursor.rowcount == 0:
        raise ValueError("Failed to create user")
    if cursor.lastrowid is None:
        raise ValueError("Email already exists")
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    if cursor.rowcount == 0:
        raise ValueError(f"User with id {user_id} does not exist")
    user = cursor.fetchone()
    conn.close()
    return user


def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    if cursor.rowcount == 0:
        raise ValueError(f"User with email {email} does not exist")
    user = cursor.fetchone()
    conn.close()
    return user


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def update_user(user_id, name=None, email=None, age=None):
    conn = get_connection()
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
    if email:
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, user_id))
    if age is not None:
        cursor.execute("UPDATE users SET age = ? WHERE id = ?", (age, user_id))
    if cursor.rowcount == 0:
        raise ValueError(f"User with id {user_id} does not exist")
    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    if cursor.rowcount == 0:
        raise ValueError(f"User with id {user_id} does not exist")
    conn.commit()
    conn.close()


def delete_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()


def drop_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
