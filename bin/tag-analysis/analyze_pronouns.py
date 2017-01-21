
import csv, requests, json, nltk, re

"""
SOme are incorrect - run to print a list to check.
eg captain - because need to remove the links -  check if that is working or not
"""

pronouns = ['she', 'her', 'he', 'his']
genders = ['woman', 'woman', 'man', 'man', 'nonbinary', 'nonbinary']


def tokenize_and_search_for_pronouns(string):
    if string:
        string = re.sub('<.+?', ' ', string)
        #tokenize the string, then search for pronouns
        words = nltk.word_tokenize(string)
        # this assumes a short bio, where the first pronoun used reflects gender
        gender = ''
        pronouns_used = [] # to look at most frequent pronoun used?
        for word in words:
            for number in range(len(pronouns)):
                if word.lower() == pronouns[number]:
                    gender = genders[number]
                    return gender
    return 'unknown'

def process_list_of_bios(filename, label):
    with open(filename) as jsonfile:
        biodata = json.load(jsonfile)

    men = 0
    names_men = []
    women = 0
    names_women = []
    unknown = 0
    names_unknown = []

    for line in biodata:
        #print line
        dictionary = dict(line)
        #if dictionary['bio']:
        gender = tokenize_and_search_for_pronouns(dictionary['bio'])
        if gender == 'man':
            men = men + 1
            names_men.append(dictionary['name'])
        elif gender == 'woman':
            women = women + 1
            names_women.append(dictionary['name'])
        else:
            unknown = unknown + 1
            names_unknown.append(dictionary['name'])

    print 'for ', filename, ' there are: '
    print 'women: ', women
    print names_women, '\n'
    print 'men: ', men
    print names_men, '\n'
    print 'unknown: ', unknown
    print names_unknown, '\n'

    ### write lists to file
    lists = [names_women, names_men, names_unknown]
    labels = [label+'women.txt', label+'men.txt', label+'unknown.txt']
    for i in range(len(lists)):
        with open(labels[i], 'wb') as h:
            for name in lists[i]:
                h.write(name +'\n')



process_list_of_bios('writer_bios.json', 'writers')
process_list_of_bios('director_bios.json', 'directors')
