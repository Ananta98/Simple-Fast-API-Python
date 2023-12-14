import pymysql
from schemas.notes import Note
from .database import connection

def insert_new_note(user_id : any, note : Note):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "INSERT INTO notes VALUES(default, %s, %s, %s)"
        cursor.execute(sql,(user_id, note.title, note.content))
        connection.commit()

def get_all_notes(user_id):
    result = []
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM notes where user_id = %s"
        cursor.execute(sql, (user_id))
        result = cursor.fetchall()
    return result

def delete_note(note_id):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "DELETE FROM notes where id = %s"
        cursor.execute(sql,(note_id))
        connection.commit()

def get_single_note(note_id):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM notes where id = %s"
        cursor.execute(sql, (note_id))
        result = cursor.fetchone()
    return result

def update_note(note_id, title, content):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "UPDATE notes SET title = %s, content = %s WHERE id = %s"
        cursor.execute(sql, (title, content, note_id))
        connection.commit()