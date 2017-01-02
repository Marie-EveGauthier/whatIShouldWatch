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
    #print name
    address = 'http://en.wikipedia.org/w/api.php?format=json&action=query&titles={search_query}&prop=categories&info&rvprop=content&redirects'.format(search_query=name)
    response = requests.get(address)
    #print 'response.status_code = ', response.status_code
    data = response.json()

    page_number = data['query']['pages'].keys()[0]
    if 'categories' in data['query']['pages'][page_number]:
        categories = data['query']['pages'][page_number]['categories']
        category_list=[]
        for category in categories:
            category_list.append(category['title'])
        return category_list

#i = 0
#while i <50:
#    print '\n\n'
#    print people[i]
#    get_wiki_cats(people[i])
#    i = i + 1

#Create a dictionary to save the people as keys and the list of categories as values.

writer_categories={}

#Makes a dictionary with only first 10 people
#i = 0
#while i <10:

#    writer_categories[people[i]] = get_wiki_cats(people[i])
#    i = i + 1

#print writer_categories

#Makes dictionary of all writers in file
for person in people:
    writer_categories[person] = get_wiki_cats(person)

#Function to save the dictionary in a csv file (for now)
def write_csv(file_name, dict_name):
    with open(file_name, 'wb') as data:
        writer = csv.writer(data)
        writer.writerows(dict_name.items())

write_csv('writer_categories.csv', writer_categories)
