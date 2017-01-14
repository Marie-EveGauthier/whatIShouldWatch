import pandas as pd


filename1 = raw_input("Enter the name of the file you want to process categories from:")

#Import the data in file as a pandas object
data = pd.read_csv(filename1, names = ['name', 'categories'])

#get a list of names who don't have entries in wikipedia
no_categories = data[data.categories.isnull()]['name'].tolist()

#and saves it to a file
filename2 = raw_input("Enter a filename to save the list of names with no entries on wikipedia")
with open(filename2, 'wb') as h:
    for name in no_categories:
        h.write(name +'\n')

have_cats = data[data.categories.notnull()]
women = have_cats[have_cats['categories'].str.contains("women")]['name'].tolist()

filename3 = raw_input("Enter a filename to save the list of names of people who are women")

with open(filename3, 'wb') as h:
    for name in women:
        h.write(name +'\n')
