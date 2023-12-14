import pymysql
from schemas.users import User
from .database import connection

def insert_new_user(user : User):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "INSERT INTO users VALUES(default, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(user.name, user.username, user.email, user.password, 1))
        connection.commit()

def get_single_user(username : str):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM users WHERE username = %s and is_active = 1"
        cursor.execute(sql, (username))
        result = cursor.fetchone()
    return result

def get_single_user_by_email(email : str):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM users WHERE email = %s and is_active = 1"
        cursor.execute(sql, (email))
        result = cursor.fetchone()
    return result

def get_user_by_id(id):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM users WHERE id = %s and is_active = 1"
        cursor.execute(sql, (id))
        result = cursor.fetchone()
    return result

def get_user_id(username):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT id FROM users WHERE username = %s"
        cursor.execute(sql,(username))
        result = cursor.fetchone()
    return result

def get_all_users():
    result = []
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def disable_user(user_id):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "UPDATE users SET is_active = 0 WHERE user_id = %s"
        cursor.execute(sql, (user_id))
        connection.commit()