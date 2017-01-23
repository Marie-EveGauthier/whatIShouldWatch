import csv


women_directors = []

with open('women_directors.txt','rb') as h:
    for line in h:
        line = line.lstrip().rstrip() #strip whitespace from beginning and newline from end
        if line == "Robert Pulcini": continue
        women_directors.append(line)

women_writers = []
with open('women_writers.txt', 'rb') as h:
    for line in h:
        line = line.lstrip().rstrip()
        women_writers.append(line)

with open('writerswomen.txt') as h:
    for line in h:
        line = line.lstrip().rstrip()
        women_writers.append(line)

allrows = []
with open('directors_data.csv', 'rb') as csvfile:
    with open('directors_data_gender.csv', 'wb') as output:
        reader = csv.reader(csvfile)
        writer = csv.writer(output)
        for line in reader:
            if line[0] in women_directors:
                line[2]=True
                #line.append("1")
            else:
                #line.append("0")
                line[2]=False
            allrows.append(line)
        writer.writerows(allrows)

allrows = []
with open('writers_data.csv', 'rb') as csvfile:
    with open('writers_data_gender.csv', 'wb') as output:
        reader = csv.reader(csvfile)
        writer = csv.writer(output)
        for line in reader:
            if line[0] in women_writers:
                line[2]=True
                #line.append(True)
            else:
                #line.append(False)
                line[2]=False
            allrows.append(line)
        writer.writerows(allrows)
