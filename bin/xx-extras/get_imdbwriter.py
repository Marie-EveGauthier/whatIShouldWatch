from urllib import urlopen
import requests
import csv
import re

with open('writers_data.csv') as csvfile:
    writers_data = list(csv.reader(csvfile))

def get_page(url):
    response = urlopen(url).read()
    #response = requests.get(url)
    if response:
        print 'page got'
    else:
        print 'page not got'
    return response #.content

#gets the part of the page that has the useful stuff in it5
def get_section(whole, start_at, end_at):
    start = whole.find(start_at)
    section = whole[start:]
    end = section.find(end_at)
    section = section[:end]
    #whole = whole[end:]
    #print section[:2000]
    return section #, whole, end_at

#, unit_pattern, unit_part, unit_part
def get_parts_from_section(to_search, part_pattern):
    parts = re.findall(part_pattern, to_search)

    if len(parts) > 0:
        print 'parts found'
        for part in parts:
            print part, '\n'
    else:
        print 'parts not found'

    return parts





imdb_id = writers_data[0][1][2:10]
print imdb_id
url = 'http://www.imdb.com/title/' + imdb_id + '/fullcredits#cast'
url1 = 'http://www.imdb.com/title/tt0070355/fullcredits?ref_=tt_ov_st_sm'

print url
page = get_page(url)
print page


section = get_section(page, 'Writing Credits', 'Cast')

parts = get_parts_from_section(section, '<a href="/name/[\s\S]+?</a>')

writer_code = ''

for part in parts:
    if writers_data[0][0] in part:
        writer_code = get_parts_from_section(part, '"[\s\S]+?"')[0]
        print 'writer code = ', writer_code

writer_url = 'http://www.imdb.com' + writer_code[1:-1]

print writer_url

#writer_page = get_page(writer_url)

#print get_parts_from_section(section, '<title>[\s\S]+?</title>')
