#!/usr/bin/python

#Get data about movies from movieinfo csv file
#movie_data structure: id, title, year, female dialogue, make dialogue, imdb
import csv
with open('../initial-data/movieinfo.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    movie_data = list(reader)


#Open database
#Database structure: title(str), year(int), imdb(str), bechdel(boolean)
#Example: 0001,A Clockwork Orange,1971,6,94,False,tt0066921
#Maeve: I took out imdb id for now.
import MySQLdb

password = raw_input("Enter your mySQL password:")
port_number = raw_input("Enter your mySQL port number if required:")
if len(port_number) > 0:
    db = MySQLdb.connect("127.0.0.1","root",password,"sf2",port=int(port_number))
else:
    db = MySQLdb.connect("127.0.0.1","root",password,"sf2")
cur = db.cursor()


#Iterate through the rows in the movie data to write them to the database
for item in movie_data:
    #title, year, imdb, bechdel
    imdb_id = str(item[6])
    title = str(item[1])
    year = int(item[2])
    dialogue_men = float(item[3])
    dialogue_women = float(item[4])
#    imdb = str(item[6])
    if item[5]=="True" :
        bechdel=True
    else :
        bechdel=False

#I took out imdb id
#I got it to work with the php format strings




    if item[5]=="" :
             cur.execute('INSERT INTO Films (title,year,dialogue_men,dialogue_women,imdb_id) VALUES ("%s","%d","%d","%d","%s")' % \
             (title,year,dialogue_men,dialogue_women,imdb_id))
    else:
             cur.execute('INSERT INTO Films (title,year,bechdel,dialogue_men,dialogue_women,imdb_id) VALUES ("%s","%d","%d","%d","%d","%s")' % \
             (title,year,bechdel,dialogue_men,dialogue_women,imdb_id))
#Commit changes
db.commit()



#Close the database
cur.close()
db.close()
