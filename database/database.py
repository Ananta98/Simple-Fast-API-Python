import pymysql

SQLALCHEMY_DATABASE_URL = "mysql://root@127.0.0.1:3306/note_taking"

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='note_taking',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
