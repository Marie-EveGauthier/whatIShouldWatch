
import csv, requests, json, nltk

with open('writers_data.csv') as csvfile:
    movie_data = list(csv.reader(csvfile))

people = [x[0] for x in movie_data]
pronouns = ['she', 'her', 'he', 'his']
genders = ['woman', 'woman', 'man', 'man', 'nonbinary', 'nonbinary']



def get_wiki_article(name):
    #Get data in article on person
    name = people[i].replace(' ','%20')
    print name
    address = 'http://en.wikipedia.org/w/api.php?format=json&action=query&titles={search_query}&prop=revisions&exintro&rvprop=content'.format(search_query=name)
    response = requests.get(address)
    #print 'response.status_code = ', response.status_code
    data = response.json()
    return json.dumps(data) #turns it into a string


def get_position_useful_text(string):
    position = 0
    if ' is ' in string:
        position = string.find(' is ')
    elif ' was ' in string:
        position = string.find(' was ')
    else:
        print 'text not found'
    start = position
    end = position+1500
    return start, end

def tokenize_and_search_for_pronouns(string):
    #tokenize the string, then search for pronouns
    words = nltk.word_tokenize(string)
    #print words
    gender = ''
    for word in words:
        for number in range(len(pronouns)):
            if word.lower() == pronouns[number]:
                gender = genders[number]
                return gender
    return 'unknown'

i = 0
while i <50:
    print people[i]
    string = get_wiki_article(people[i])
    start, end = get_position_useful_text(string)
    string = string[start:end]
    #print string
    gender = tokenize_and_search_for_pronouns(string)
    print gender

    #move through while loop
    i = i + 1
