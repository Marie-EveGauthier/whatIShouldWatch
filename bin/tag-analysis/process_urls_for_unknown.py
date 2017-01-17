"""
get peopleurls as a director
get file list to compare
for each line in file
look for name in dict
when names match, add url
"""

import csv

#filename = raw_input("Enter the name of the file you want to process categories from:\n")

with open('noentry_directors.txt', 'rb') as csvfile:
    list_of_people = list(csvfile)

with open('crewurlsKeyValSample.json') as csvfile:
    url_dict_list = list(csvfile)

def get_section(whole, start_at, end_at):
    start = whole.find(start_at)
    section = whole[start+1:]
    end = section.find(end_at)
    section = section[:end]
    #whole = whole[end:]
    #print section[:2000]
    return section, end

def get_url_list(list_of_dicts):
    result = []
    for dictionary in list_of_dicts:
        name, end = get_section(dictionary, '"', '"')
        name = name[1:-2].decode('utf-8')
        second_part = dictionary[end+3:]
        url, end = get_section(second_part, '"', '"')
        result.append((name, url))
    return result

url_list = get_url_list(url_dict_list)

print list_of_people

people_with_urls = []

for person in list_of_people:
    name = person
    #for entry in url_list:
    entry = url_list[1]
    print entry
    print 'entry name = ', entry[0].decode('utf-8')
    print 'name = ', name
    if name == entry[0].decode('utf-8'):
        print 'found'
    print '\n'

        #url = url_dict[name]
        #people_with_urls.append()
    #else:
        #print 'not found'
print people_with_urls
