
import csv
import MySQLdb

with open('../initial-data/directors_data_gender.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile.read().decode('utf-8-sig').encode('utf-8').splitlines())
    directors_data = list(reader)

password = raw_input("Enter your mySQL password:")
db = MySQLdb.connect("127.0.0.1","root",password,"sf2") #ADD BACK POR!?
cur = db.cursor()

for item in directors_data:
    name = str(item[0])
    if item[2]== "True":
        gender = 'W'
    else:
        gender = ''

    query = ('INSERT INTO directors (name,gender) VALUES (%s,%s)')
    cur.execute(query, (name,gender))


db.commit()

cur.close()
db.close()
