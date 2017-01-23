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
