""" This file uses movie dialogue data from:
 https://github.com/matthewfdaniels/scripts/

It uses data on the words spoken by main characters in movies (in the file
character_list5) to calculates the percentages of male and female dialogue for
each movie.  It stores this in film_info.

Then the data in film_info is cross referenced with the data in meta_data7 to
get the name, year, and imdb_id of each movie.

This file accesses character_list5.csv, and meta_data7.csv.  It creates
movie_data.csv"""

#Get the data in the csv file.  Each row represents one character.  Each movie
#has several rows, linked by the script_id
import csv
with open('character_list5.csv') as csvfile:
    dialogue_data = list(csv.DictReader(csvfile)) #stores characters, words spoken

#Get a set of the unique movie ids
films = list(set(d['script_id'] for d in dialogue_data))

movie_percentages_info = []

for film in films: #for film in films: #Iterate through the unique movie ids
    print film
    #Variables to collect the words spoken by male and female characters
    f_words = 0
    m_words = 0
    #Iterate through the data, looking for the entries matching this film (via id)
    for d in dialogue_data:
        if d['script_id'] == film:
            #print d['imdb_character_name'], d['gender'], d['words']
            if d['gender'] == 'f':
                f_words = f_words + float(d['words'])
            elif d['gender'] == 'm':
                m_words = m_words + float(d['words'])
            film_id = d['script_id']

    #Calculate percentages:
    total = f_words + m_words
    print 'total ', total
    f_percent = round((f_words * 100 / total), 2)
    print 'f_percent ', f_percent
    m_percent = round((m_words * 100 / total), 2)
    print 'm_percent ', m_percent
    unit = [film_id, f_percent, m_percent]
    print unit
    movie_percentages_info.append(unit)

print '\n', movie_percentages_info, '\n'

#Get data on movie names (and years and imdb ids) from meta7 csv file
import csv
with open('meta_data7.csv', 'rb') as csvfile:
    data_from_meta7 = list(csv.DictReader(csvfile))

#List to store data on: script_id, title, imdb_id, year.  Add data to it from
#meta7
movie_name_info = []
for d in data_from_meta7:
    new_entry = [d['script_id'], d['title'], d['imdb_id'], d['year']]
    movie_name_info.append(new_entry)

#Lst to store complete data:
complete_movie_data = []

#Iterate through list which has dialogue percentages
i = 0
for movie in movie_percentages_info:
#Iterate through list with movie names in, check if script ids match
    for film in movie_name_info:
        if movie[0] == film[0]:
            name = film[1]
            imdb_id = film[2]
            year = film[3]
    print name, imdb_id, year
    f_percent = movie[1]
    m_percent = movie[2]
    print m_percent, f_percent
#Add complete movie entry to complete_movie_data
#film_id, name,year, %female, %male, bechdel, imdb_id
    unit = [i, name, year, f_percent, m_percent, '', imdb_id]
    complete_movie_data.append(unit)
    i = i + 1

with open('movie_data.csv', 'wb') as db:
    writer = csv.writer(db)
    writer.writerows(complete_movie_data)
