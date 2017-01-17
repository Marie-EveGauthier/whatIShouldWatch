""" This file scrapes http://bechdeltest.com/?list=all for movie info.
It stores movies that pass in pass_movies, and movies that fail in fail_movies.
It then adds this information to the csv file which already has movie data.

This file accesses and rewrites movie_data_complete.csv"""

import requests
import csv

pass_movies = []
fail_movies = []


def get_page(url):
    #Gets contents of page
    response = requests.get(url)
    return response.content

def find_movie(page, start):
    #Parses page to get info about one movie
    start_movie = page.find('<div class="movie">', start)
    #get pass or fail:
    verdict_place = page.find('<img src="/static/', start_movie) + 18
    verdict = page[verdict_place:verdict_place+4]
    #get imdb code too:
    imdbid_start = page.find('http://us.imdb.com/title/', start_movie) + 25
    imdbid_end = page.find('/', imdbid_start)
    imdbid = page[imdbid_start:imdbid_end]
    #get name:
    name_place = page.find('<a id="movie', start_movie)
    start_name = page.find('>', name_place) + 1
    end_name = page.find('<', start_name)
    movie_name = page[start_name:end_name]
    #clean name:
    movie_name.replace("&#39;", "'")
    movie_name.replace("&amp;", "&")
    #send to pass_movies OR fail_movies with the code
    if verdict == "pass":
        pass_movies.append(imdbid)
    elif verdict == "nopa":
        verdict = "fail"
        fail_movies.append(imdbid)
    return end_name


def find_all_movies(page):
    #Goes through the page, runnings find_movie until all found
    start = 0
    while True:
        start = find_movie(page, start)
        if start == -1:
            return
"""
#This function writes the two lists of pass and fail movies to files
def save_to_file():
    #Save to csv file, this can be replaced with writing to database
    with open('bechdel_pass.csv', 'wb') as csvfile1:
        writer = csv.writer(csvfile1, quoting=csv.QUOTE_ALL)
        writer.writerow(pass_movies)
    with open('bechdel_fail.csv', 'wb') as csvfile2:
        writer = csv.writer(csvfile2, quoting=csv.QUOTE_ALL)
        writer.writerow(fail_movies)
"""

def add_to_file():
#Get movie data already in the file
    with open('movie_data.csv', 'rb') as csvfile:
        movie_data_update = list(csvfile)

#Turn list of strings into list of lists
    movie_data_updated = []
    for movie in movie_data_update:
        entry = [x.strip() for x in movie.split(',')]
        movie_data_updated.append(entry)

#Add bechdel pass or fail
    for movie in movie_data_updated:
        imdbid = movie[6]
        for entry in pass_movies:
            if entry == imdbid:
                movie[5] = True
        for entry in fail_movies:
            if entry == imdbid:
                movie[5] = False

    with open('movie_data_complete.csv', 'wb') as db:
        writer = csv.writer(db)
        for movie in movie_data_updated:
            writer.writerow((movie))

#Add bechdel pass or fail
"""    for movie in movie_data_updated:
        print movie
        imdbid = movie[6]
        for entry in pass_movies:
            if entry == imdbid:
                movie[5] = True
        for entry in fail_movies:
            if entry == imdbid:
                movie[5] = False
"""

page = get_page("http://bechdeltest.com/?list=all")
find_all_movies(page)
#save_to_file()
add_to_file()
