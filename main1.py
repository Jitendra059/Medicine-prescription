import sqlite3
connection=sqlite3.connect("D:\my_project\mprescribe.db")
crsr=connection.cursor()
crsr.execute("CREATE TABLE IF NOT EXISTS 'USER'(UID INTEGER PRIMARY KEY AUTOINCREMENT,UNAME VARCHAR(20) NOT NULL,PASSWORD VARCHAR(20) NOT NULL)")
connection.commit()
connection.close()