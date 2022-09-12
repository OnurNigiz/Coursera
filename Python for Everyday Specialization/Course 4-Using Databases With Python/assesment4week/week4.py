import json
import sqlite3

# PART 1: Creating the database
dbname = "roster.sqlite"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS User;
	DROP TABLE IF EXISTS Course;
	DROP TABLE IF EXISTS Member;
	CREATE TABLE User (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE
	);
	CREATE TABLE Course (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title TEXT UNIQUE
	);
	CREATE TABLE Member (
		user_id INTEGER,
		course_id INTEGER,
		role INTEGER,
		PRIMARY KEY(user_id, course_id)
	)
''')

# Read the file
filename = "roster_data.json"
jsondata = open(filename)
data = json.load(jsondata)

for entry in data:
    user = entry[0]
    course = entry[1]
    role = entry[2]

    # User
    cur.execute('''INSERT OR IGNORE INTO User(name) VALUES( ? )''', (user, ))
    cur.execute('''SELECT id FROM User WHERE name =?''', (user, ))
    user_id = cur.fetchone()[0]

    # Coure
    cur.execute('''INSERT OR IGNORE INTO Course(title) VALUES( ? )''', (course, ))
    cur.execute('''SELECT id FROM Course WHERE title =?''', (course, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)''', (user_id, course_id, role))

conn.commit()
conn.close()
