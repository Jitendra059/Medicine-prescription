import sqlite3
connection=sqlite3.connect("D:\my_project\mprescribe.db")
crsr=connection.cursor()
crsr.execute("CREATE TABLE IF NOT EXISTS 'DETAILS'(PID INTEGER PRIMARY KEY AUTOINCREMENT,NAME VARCHAR(20) NOT NULL,ADDRESS VARCHAR(20) NOT NULL,EMAIL VARCHAR(20) NOT NULL,PHONE_NO INTEGER)")
connection.commit()
connection.close()