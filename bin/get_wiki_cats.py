"""
This gets and prints (all) the wiki categories of the writers.  Right now the
loop at the bottom is set to just the first 50.
"""


import csv, requests, json

with open('writers_data.csv') as csvfile:
    writers_data = list(csv.reader(csvfile))

people = [x[0] for x in writers_data]

def get_wiki_cats(name):
    #Get data in article on person
    name = name.replace(' ','%20')
    print name
    address = 'http://en.wikipedia.org/w/api.php?format=json&action=query&titles={search_query}&prop=categories&info&rvprop=content&redirects'.format(search_query=name)
    response = requests.get(address)
    #print 'response.status_code = ', response.status_code
    data = response.json()

    page_number = data['query']['pages'].keys()[0]
    if 'categories' in data['query']['pages'][page_number]:
        categories = data['query']['pages'][page_number]['categories']
        for category in categories:
            print category['title']

i = 0
while i <50:
    print '\n\n'
    print people[i]
    get_wiki_cats(people[i])
    i = i + 1
