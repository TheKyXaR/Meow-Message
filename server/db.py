# db command

import sqlite3

con = sqlite3.connect("db.db")
cur = con.cursor()

def select () :	
	return cur.execute("SELECT user, data FROM message").fetchmany(20)

def insert (data) :
	cur.execute(f"INSERT INTO message (user, data) VALUES ('{data['nickname']}', '{data['data']}')")
	con.commit()
	