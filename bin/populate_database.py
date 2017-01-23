
#Get data about movies from movieinfo csv file
#movie_data structure: id, title, year, female dialogue, make dialogue, imdb
import csv
with open('movieinfo.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    movie_data = list(reader)


#Open database
#Database structure: title(str), year(int), imdb(str), bechdel(boolean)
#Example: 0001,A Clockwork Orange,1971,6,94,False,tt0066921
#Maeve: I took out imdb id for now.
import MySQLdb

password = raw_input("Enter your mySQL password:")
<<<<<<< HEAD:bin/populate_database.py
=======
db = MySQLdb.connect("localhost","root",password,"symfony")
>>>>>>> parent of d0aefaf... modification for the script python:bin/database_populate.py

db = MySQLdb.connect("127.0.0.1","root",password,"sf2", port=8889)
cur = db.cursor()


#Iterate through the rows in the movie data to write them to the database
for item in movie_data:
    #title, year, imdb, bechdel
    title = str(item[1])
    year = int(item[2])
#    imdb = str(item[6])
    bechdel = bool(item[5])
#I took out imdb id
#I got it to work with the php format strings
    cur.execute('INSERT INTO Films (title,year,bechdel) VALUES ("%s","%d","%d")' % \
    (title,year,bechdel))

#Commit changes
db.commit()

#Close the database
cur.close()
db.close()
