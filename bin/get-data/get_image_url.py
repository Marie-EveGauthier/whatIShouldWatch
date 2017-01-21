import csv, json, urllib


#Get data we already have for movies:
with open('movieinfo.csv') as csvfile:
    movie_data = list(csv.reader(csvfile))

#Lists to store the data
movie_data_with_url = []


#Use while loop (instead of for) to make testing/ debugging easier
i = 0
while i <2000:
    #Get writer and director info for each movie, from the omdb, using the imdb id
    this_movie = movie_data[i]
    imdb_id = this_movie[6]
    address = 'http://www.omdbapi.com/?i={imdbid}&plot=short&r=json'.format(imdbid=imdb_id)
    data_raw = urllib.urlopen(address).read()
    data = json.loads(data_raw)
    #print data

    #Check the request worked by checking the keys are present
    if 'Poster'  in data:
        image_url = data['Poster'] #.encode('utf-8').split(',')

    else:
        print 'no image url'
        image_url = ''

    movie_data_with_url.append([this_movie[0], this_movie[1], this_movie[2], this_movie[3], this_movie[4], this_movie[5], this_movie[6], image_url])

    i = i + 1


#Function to store the data in a csv file (for now)
def write_csv(file_name, list_name):
    with open(file_name, 'wb') as data:
        writer = csv.writer(data)
        for row in list_name:
            writer.writerow((row))

write_csv('movie_data_with_url.csv', movie_data_with_url)
