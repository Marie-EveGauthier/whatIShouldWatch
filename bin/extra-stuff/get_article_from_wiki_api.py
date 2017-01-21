def get_wiki_article(name):
    #Get data in article on person
    name = people[i].replace(' ','%20')
    print name
    address = 'http://en.wikipedia.org/w/api.php?format=json&action=query&titles={search_query}&prop=revisions&exintro&rvprop=content'.format(search_query=name)
    response = requests.get(address)
    #print 'response.status_code = ', response.status_code
    data = response.json()
    return json.dumps(data) #turns it into a string
