import sqlite3


DB_NAME = r"data\team.db3"
con = sqlite3.connect(DB_NAME)
cur = con.cursor()

SQLOPS={
	"newUser":"""INSERT INTO players
                          (id, username, first_name, last_name, entitlement,dni,position,creation_date,created_by) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);""",
	"authUser":"""INSERT INTO players
                          (id, username, first_name, last_name, entitlement,dni,position,authorization_date,authorized_by) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);""",
    "checkUser":"SELECT * FROM tasks WHERE priority=?",
}