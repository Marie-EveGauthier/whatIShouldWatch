#!/usr/bin/python

import csv
import MySQLdb
import ast

with open('../initial-data/directors_data_gender.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile.read().decode('utf-8-sig').encode('utf-8').splitlines())
    directors_data = list(reader)

password = raw_input("Enter your mySQL password:")
port_number = raw_input("Enter your mySQL port number if required:")
if len(port_number) > 0:
    db = MySQLdb.connect("127.0.0.1","root",password,"sf2",port=int(port_number))
else:
    db = MySQLdb.connect("127.0.0.1","root",password,"sf2")
cur = db.cursor()

for item in directors_data:
    name = str(item[0])
    imdb_ids = ast.literal_eval(item[1])
    for current_imdb_id in imdb_ids: #['tt1939659']:  #imdb_ids:tt0066921', '
        print 'current_imdb_id ', current_imdb_id
        cur.execute("SELECT id FROM films WHERE imdb_id = ('%s')" % (current_imdb_id))
        film_key = cur.fetchone()[0]
        print film_key

        cur.execute("""SELECT id FROM directors WHERE name = ("%s")""" % (name))
        director_key = cur.fetchone()[0]
        print director_key

        cur.execute('INSERT INTO directorfilm (director_id,film_id) VALUES ("%d","%d")' % \
        (director_key,film_key))

db.commit()

cur.close()
db.close()
