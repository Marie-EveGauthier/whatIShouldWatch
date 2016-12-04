""" This file gets data on the words spoken by main characters in
movies (in the file character_list5), the data is from the polygraph website.
  It stores this data in dialogue_data, and then calculates the percentages of male
and female dialogue for each movie in the original file.  It stores this in
film_info, and then writes it to dbfile """

import csv
with open('character_list5.csv') as csvfile:
    dialogue_data = list(csv.DictReader(csvfile))

films = set(d['script_id'] for d in dialogue_data)

films_info = []

for f in films:
    f_words = 0
    m_words = 0

    for d in dialogue_data:
        if d['script_id'] == f:
            if d['gender'] == 'f':
                f_words = f_words + int(d['words'])
            elif d['gender'] == 'm':
                m_words = m_words + int(d['words'])
            film_id = d['script_id']

    total = f_words + m_words

    f_percent = f_words * 100 / total
    m_percent = m_words * 100 / total

    #film_id, name,year, %female, %male, bechdel, imdb_id
    films_info.append([film_id, '', '', f_percent, m_percent,'', ''])

print films_info

with open('dbfile.csv', 'wb') as db:
    writer = csv.writer(db)
    writer.writerows(films_info)

""" This file adds to the data saved in dbfile in one.py.
meta_data7 is from the same project as the file with dialogue
data (from polygraph).  This file cross references them to get the
name, year, and imdb_id of the films we have data for from one.py  """

import csv
with open('meta_data7.csv') as csvfile:
    data_from_meta = list(csv.DictReader(csvfile))

films_name_info = []     #script_id, title, imdb_id, year

for d in data_from_meta:
    new_entry = [d['script_id'], d['title'], d['imdb_id'], d['year']]
    films_name_info .append(new_entry)

with open('dbfile.csv') as csvfile:
    complete_film_data = list(csv.reader(csvfile)) #film_id, name,year, %female, %male, bechdel, imdb_id

#compare two lists - how?
#if first entry of both is the same, add info from readfile to infotwo



for w in complete_film_data: #iterate through list with/ for whole data

    for n in films_name_info : #iterate through list with names and imdb id
        if w[0] == n[0]: #if script_id matches
            name = n[1]
            imdb_id = n[2]
            year = n[3]

    w[1] = name
    w[2] = year
    w[6] = imdb_id

    print w

with open('dbfile.csv', 'wb') as db:
    writer = csv.writer(db)
    writer.writerows(complete_film_data)
