
import csv, json, urllib

def process_data(input_list, output_table, current_movie_id):
    for person in input_list:
        #Brackets contain the specific role eg novel, screenplay.  This is being
        #removed and discarded here, but might be useful ultimately
        if '(' in person:
            position = person.find('(')
            person = person[:position].strip()
        found = False
        #Check if this director is already in writers table
        for row in output_table:
            if person == row[0]:
                found = True
                #Add movie to already exsiting director entries
                row[1].append(current_movie_id)
                break
        if found == False:
            #Add director to directors_table
            output_table.append([person, [current_movie_id], []])

#Get data we already have for movies:
with open('movie_data_complete.csv') as csvfile:
    movie_data = list(csv.reader(csvfile))

#Lists to store the data ([writer, [movie imdb ids], [tags]])
writers_table = []
directors_table = []

#Use while loop (instead of for) to make testing/ debugging easier
i = 0
while i <200:
    #Get writer and director info for each movie, from the omdb, using the imdb id
    this_movie = movie_data[i]
    imdb_id = this_movie[6]
    address = 'http://www.omdbapi.com/?i={imdbid}&plot=short&r=json'.format(imdbid=imdb_id)
    data_raw = urllib.urlopen(address).read()
    data = json.loads(data_raw)
    #print data

    #Check the request worked by checking the keys are present
    if 'Writer'  in data:
        writers = data['Writer'].encode('utf-8').split(',')
        #Process people in lists of writers
        process_data(writers, writers_table, imdb_id)
    if 'Director' in data:
        directors = data['Director'].encode('utf-8').split(',')
        #Process people in lists of directors
        process_data(directors, directors_table, imdb_id)

    i = i + 1


#Function to store the data in a csv file (for now)
def write_csv(file_name, list_name):
    with open(file_name, 'wb') as data:
        writer = csv.writer(data)
        for row in list_name:
            writer.writerow((row))

write_csv('directors_data.csv', directors_table)
write_csv('writers_data.csv', writers_table)
