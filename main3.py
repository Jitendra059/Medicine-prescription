import sqlite3
connection=sqlite3.connect("D:\my_project\mprescribe.db")
crsr=connection.cursor()
crsr.execute("CREATE TABLE IF NOT EXISTS 'PATIENT'(PID INTEGER PRIMARY KEY AUTOINCREMENT,PNAME VARCHAR(20) NOT NULL,PHONE INTEGER NOT NULL,EMAIL VARCHAR(20) NOT NULL,AGE INTEGER NOT NULL,GENDER CHAR(2) NOT NULL)")
connection.commit()
connection.close()