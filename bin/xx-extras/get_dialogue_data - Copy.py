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
    dialogue_data = list(csv.DictReader(csvfile))

#Get a set of the unique movie ids
films = set(d['script_id'] for d in dialogue_data)

movie_percentages_info = []

#Iterate through the unique movie ids
for f in films:
#Variables to collect the words spoken by male and female characters
    f_words = 0
    m_words = 0
#Iterate through the data, looking for the entries matching this film (via id)
    for d in dialogue_data:
        if d['script_id'] == f:
            if d['gender'] == 'f':
                f_words = f_words + int(d['words'])
            elif d['gender'] == 'm':
                m_words = m_words + int(d['words'])
            film_id = d['script_id']

#Calculate percentages:
    total = f_words + m_words
    f_percent = f_words * 100 / total
    m_percent = m_words * 100 / total

    movie_percentages_info.append([film_id, f_percent, m_percent])


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
for w in movie_percentages_info:
#Iterate through list with movie names in, check if script ids match
    w[1] = f_percent
    w[2] = m_percent
    for n in movie_name_info:
        if w[0] == n[0]:
            name = n[1]
            imdb_id = n[2]
            year = n[3]
#Add complete movie entry to complete_movie_data
#film_id, name,year, %female, %male, bechdel, imdb_id
    complete_movie_data.append((i, name, year, f_percent, m_percent, '', imdb_id))
    i = i + 1

with open('movie_data.csv', 'wb') as db:
    writer = csv.writer(db)
    writer.writerows(complete_movie_data)
