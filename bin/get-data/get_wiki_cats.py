"""
This gets all the wikipedia categories for either the writers or directors on our list
and saves them to a file.
"""


import csv, requests, json

ifilename = raw_input("Enter the file you want to read from:\n")
with open(ifilename) as csvfile:
    names_data = list(csv.reader(csvfile))

people = [x[0] for x in names_data]

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

people_categories={}

#Makes a dictionary with only first 10 people
#i = 0
#while i <10:

#    writer_categories[people[i]] = get_wiki_cats(people[i])
#    i = i + 1

#print writer_categories

#Makes dictionary of all writers in file
for person in people:
    people_categories[person] = get_wiki_cats(person)

#Function to save the dictionary in a csv file (for now)
def write_csv(file_name, dict_name):
    with open(file_name, 'wb') as data:
        writer = csv.writer(data)
        writer.writerows(dict_name.items())

ofilename = raw_input("Enter the name of the file where you want to save the categories:\n")
write_csv(ofilename, people_categories)
