
import requests, json

# list of categories to be queried, we will add to this list
categories_to_search = ['Women_film_directors']

#save data we get back here, in format:
#[name, [identities - from the categories]]
data_we_get_back = []


#This function takes a name and category and adds it to the list data we get back
def add_to_members(new_member, category):
    present = False
    #check if name already in list 'data we get back'
    for name in data_we_get_back:
        if data_we_get_back[0] == new_member:
            data_we_get_back[1].append(category)
            present = True
    if present == False:
        data_we_get_back.append([new_member, [category]])



def get_category_members(category_to_search):
    #Get data
    #cmlimit=20 limits results to 20, increase later
    address = 'http://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmlimit=20&cmtitle=Category:{category_name}'.format(category_name=category_to_search)
    response = requests.get(address)

    #status code should be 200 if the api request works, use this if something isnt working:
    #print 'response.status_code = ', response.status_code

    data = response.json()
    #data = json.dumps(data)
    for result in data["query"]["categorymembers"]:
        title = result['title']
        print title
        #if the result is a category, send it to the list that will be queried
        #(there is probably a better way to check if it is a category using the data)
        if 'List of' in title or 'Category' in title or 'filmmakers' in title:
            categories_to_search.append(title)
        #if the result is a member, send to the function to add to the final data list
        else:
            add_to_members(title, category_to_search)

    #remove category from categories_to_search


#in the future this could be a while loop (while the len of categories_to_search > 0)
for each in categories_to_search :
    get_category_members(each)

print 'categories_to_search', categories_to_search
print 'data_we_get_back', data_we_get_back
