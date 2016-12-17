
#Get data about movies from movieinfo csv file
#movie_data structure: id, title, year, female dialogue, make dialogue, imdb
import csv
with open('movieinfo.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    movie_data = list(reader)


#Open database
#Database structure: title(str), year(int), imdb(str), bechdel(boolean)
#Example: 0001,A Clockwork Orange,1971,6,94,False,tt0066921
import MySQLdb
db = MySQLdb.connect(host="localhost",
                     user="root",
                     password="",
                     db="watch")
cur = db.cursor()


#Iterate through the rows in the movie data to write them to the database
for item in movie_data:
    #title, year, imdb, bechdel
    title = str(item[1])
    year = int(item[2])
    imdb = str(item[6])
    bechdel = bool(item[5])
    #fix data type %s to %d?
    cur.execute("INSERT INTO moviestwo (title,year,imdb,bechdel) VALUES (%s,%d,%s,%b)", (title,year,imdb,bechdel))

#Commit changes
db.commit()

#Close the database
cur.close()
db.close()
