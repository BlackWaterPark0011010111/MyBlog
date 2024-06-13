import sqlite3 as sq

with sq.connect('my_diary') as con:
    cur = con.cursor()
    cur.execute("""""")