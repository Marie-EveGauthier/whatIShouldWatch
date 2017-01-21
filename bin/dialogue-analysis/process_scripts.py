
from urllib import urlopen

def get_script(url):
    return urlopen(url).read()

def process_for_indents(raw):
    #split up lines
    lines = raw.split("\n")

    start = 0
    end = len(lines)
    #get the part that is actual script
    for line in lines:
        if 'FADE IN' in line:
            start = lines.index(line)
        if 'FADE OUT' in line:
            end = lines.index(line)
    lines = lines[start:end]

#if line minus brakcets is the name or the first half of the name
#line before is blank
#lines after - word count goes to that Peterson
#until empty line
    for line in lines:
        for character in character:
            if line.strip() == character or line.split()[0] == character[0]:
                print 'match'








scripts = ["http://www.imsdb.com/scripts/Carrie.html"]
characters = ["Margaret White", "Carrie White", "Sue Snell", "Chris Hargensen", "Tina", "Heather", "Nicki", "Lizzy", "Tommy Ross", "George Dawson", "Ms. Desjardin", "Principal Morton", "Miss Helen Finch", "Greg Delois", "Harry Trenant          (as Eddie Huband)", "Billy Nolan", "Neighborhood Kid", "Freddy 'Beak' Holt", "Mr. Ulmann", "Eleanor Snell", "Ernie Peterson", "Kenny", "Jackie", "Erika", "Head Commissioner", "Dr. Dean L. McDuffy", "Mr. Hargensen          (uncredited)", "Student Dancer #6          (uncredited)", "Student Dancer #7          (uncredited)", "Gym Class Mean Girl 3          (uncredited)", "Gym Class Mean Girl 1          (uncredited)", "Dress Shop Passerby          (uncredited)", "Man on Street          (uncredited)", "Grieving Prom Girl          (uncredited)", "Prom Survivor          (uncredited)", "Student          (uncredited)", "Gym Class Mean Girl 5          (uncredited)", "Sheriff Otis Doyle          (uncredited)", "Student Dancer #3          (uncredited)", "Cheerleader #1          (uncredited)", "Estelle Parsons          (uncredited)", "Estelle's Mother          (uncredited)", "Brad          (uncredited)", "Student Dancer #2          (uncredited)", "Ms. Arlene Walsh          (uncredited)", "Mean Girl          (uncredited)", "Young Estelle Horan          (uncredited)", "Flower Girl          (uncredited)", "Student Dancer #8          (uncredited)", "Young Carrie          (uncredited)", "High School Student          (uncredited)", "Student Dancer #1          (uncredited)"]
counts = []

for character in characters:
    character = character.replace('(uncredited)', ' ')
    character = character.strip()
    counts.append(0)

for script in scripts:
    #print script
    raw = get_script(script)

    process_for_indents(raw)
    print '\n\n'
