from urllib import urlopen
import csv

with open('movie_data.csv') as csvfile:
    movie_data = list(csv.reader(csvfile))

def get_page(url):
    return urlopen(url).read()

def get_section(whole, start_at, end_at):
    start = whole.find(start_at)
    section = whole[start:]
    end = section.find(end_at)
    section = section[:end]
    #whole = whole[end:]
    return section, whole, end_at

def get_individual_characters(characters_cast_section):
    start = 0
    characters_to_process = characters_cast_section
    #one_character = ''
    while True:
        one_character, characters_to_process, end_at = get_section(characters_to_process, '<tr ', '</tr>')

        print 'char'
        if end_at == -1:
            break

#this will be a loop later:
movie = movie_data[0]
imdb_id = movie[6]
url = 'http://www.imdb.com/title/' + imdb_id + '/fullcredits?ref_=tt_cl_sm#cast'
print 'url = ', url


page = get_page(url)
characters_cast_section = get_section(page, '<table class="cast_list">', '  </table>')
get_individual_characters(characters_cast_section)
#print characters_cast_section
#find_characters(page)
#print page

print 'get_section len ', len(get_section(page, '<table class="cast_list">', '  </table>'))
