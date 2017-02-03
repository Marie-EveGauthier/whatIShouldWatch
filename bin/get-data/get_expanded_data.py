import csv, json, urllib, unicodecsv

def process_data(input_list, output_table, current_movie_id):
    for person in input_list:
        #Brackets contain the specific role eg novel, screenplay.  This is being
        #removed and discarded here, but might be useful ultimately
        if '(' in person:
            position = person.find('(')
            person = person[:position].strip()
        found = False
        #encode to unicode to avoid problems later
        person = person.encode('utf8')
        #Check if this director is already in writers table
        for row in output_table:
            if person == row[0]:
                found = True
                #Add movie to already exsiting director entries
                row[1].append(current_movie_id)
                break
        if found == False:
            #Add director to directors_table
            output_table.append([person, [current_movie_id]])

#open list of movies and directors/writers from the new lists
with open('../../initial-data/expandedfilms.csv') as csvfile:
    movie_names = list(csv.reader(csvfile))
with open('../../initial-data/expandedpeople.csv') as csvfile:
    people = list(csv.reader(csvfile))

#Lists to store the data
movie_data = []
writers_data = []
directors_data = []

#iterate through the movies
i = 0
for movie in movie_names:
    i = i + 1
    movie_name = str(movie[0])
    name_for_call = str(movie).replace(' ', '+')
#get info about each movie from omdb api
    address = 'http://www.omdbapi.com/?t={name}&y=&plot=short&r=json'.format(name=name_for_call)
    data_raw = urllib.urlopen(address).read()
    data = json.loads(data_raw)
    #print data

    #Check the request worked by checking the keys are present
    #otherwise there will be an error
    #could this use try and except?
    if 'Year'  in data:
        year = data['Year']
    else:
        year = ''
    if 'imdbID'  in data:
        imdbid = data['imdbID']
    else:
        imdbid = 0
    if 'Poster'  in data:
        image_url = data['Poster']
    else:
        image_url = ''
    if 'Director'  in data:
        directors = data['Director'].split(',')
    else:
        directors = []
    if 'Writer'  in data:
        writers = data['Writer'].split(',')
    else:
        writers = []

    #add a line to only continue if no data missing?!

    #line to add to movieinfo2 csv file, process writer and director data
    movie_data.append([i, movie_name, year, 0, 0, '', imdbid, image_url])
    process_data(directors, directors_data, imdbid)
    process_data(writers, writers_data, imdbid)

#oterate through writers and directors and add tags
for writer in writers_data:
    for person in people:
        if writer[0] == person[0] and len(writer) < 4:
            writer.append(person[1])
            if 'poc' in person[2]:
                writer.append('T')
            else:
                writer.append('')
            if 'LGBTQ' in person[3]:
                writer.append('T')
            else:
                writer.append('')

for director in directors_data:
    for person in people:
        if director[0] == person[0] and len(director) < 4:
            director.append(person[1])
            if 'poc' in person[2]:
                director.append('T')
            else:
                director.append('')
            if 'LGBTQ' in person[3]:
                director.append('T')
            else:
                director.append('')



print 'movie data', movie_data, '\n'
print 'directors data', directors_data, '\n'
print 'writers data', writers_data, '\n'

#Function to store the data in a csv file (for now)
def write_csv(file_name, list_name):
    with open(file_name, 'wb') as newfile:
        writer = unicodecsv.writer(newfile)
        writer.writerows(list_name)


write_csv('../../initial-data/movieinfo2.csv', movie_data)
write_csv('../../initial-data/writersdata2.csv', writers_data)
write_csv('../../initial-data/directorsdata2.csv', directors_data)
