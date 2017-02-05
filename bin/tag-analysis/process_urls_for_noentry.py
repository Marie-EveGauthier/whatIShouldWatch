"""
get peopleurls as a director
get file list to compare
for each line in file
look for name in dict
when names match, add url
"""

import json
import csv

with open('crewurls.json') as jsonfile:
    url_dict_list = json.load(jsonfile)

dictionary = {}

for line in url_dict_list:
    entry = dict(line)
    dictionary.update(entry)


#filename = raw_input("Enter the name of the file you want to process categories from:\n")

list_of_directors = open("noentry_directors.txt", "r")
list_of_writers = open("noentry_writers.txt", "r")


def produce_list_with_urls(list_of_people, filename):
    list_with_urls = []

    for name in list_of_people:
        name = name.strip()
        if name in dictionary.keys():
            url = 'http://www.imdb.com' + dictionary[name]
            list_with_urls.append([name, url])

    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list_with_urls)



produce_list_with_urls(list_of_directors, 'director_noentry_imdburls.csv')
produce_list_with_urls(list_of_writers, 'writer_noentry_imdburls.csv')
