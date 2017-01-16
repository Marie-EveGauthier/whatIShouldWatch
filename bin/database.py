import csv
import MySQLdb

mysqlpswd = raw_input("Enter your mySQL password:")

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd=mysqlpswd,  # your password
                     db="sf2")

cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS moviestwo")

cur.execute("""CREATE TABLE moviestwo(
    title TEXT,
    year INTEGER,
    bechdel TINYINT)
    """)

db.commit()
db.close()
