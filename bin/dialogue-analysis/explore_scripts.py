"""
Looking at indent patterns in scripts.  Thinking about how we can process them.

-->>> We need to know the characters names first

This program prints out the script link and common indent lengths in the lines,
with some examples for each indent length.

Some things we should consider:

Some scripts indent character names and
words spoken differently from each other (and from description/ stage directions).

Some seem to show character who is speaking by having the name in bold, and the
lines directly underneath.  With no indent.

Some of them seem to have directions or comments wrapped in brackets which would
be easy to remove.

The scripts here are from the IMSDb.  There are other sources of scripts online,
some are pdfs.  There is a library that can extract from pdf, but I haven't  used
it.
"""

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


    indents = []
    lines_sorted = []
    for line in lines:
        #don't include lines that are empty or html
        #(maybe should include lines that start but dont end in html)
        stripped_line = line.strip()
        if len(stripped_line) > 1 and stripped_line [0] != "<":
        #count spaces at the start of the lines
        #save this number in spaces, and corresponding line in lines_sorted
            space = 0
            while True:
                if len(line) > space and line[space] == ' ':
                    space = space + 1
                else:
                    indents.append(space)
                    lines_sorted.append(line)
                    space = 0
                    break

    #get indent size, number f lines with that indent, and some examples
    indents_in_script = set(indents)
    for x in indents_in_script:
        occurances = 0
        examples = []
        for y in range(len(indents)):
            if indents[y] == x:
                occurances = occurances + 1
                examples.append(lines_sorted[y])
        #if less than 5 lines with that indent, then it isn't a character name
        # or dialogue
        if occurances > 5:
            print 'indent length:', x
            print 'occurances: ', occurances
            print 'examples: '
            for example in examples[:15]:
                print example








scripts = ["http://www.dailyscript.com/scripts/AirForceOne_TXT.html",
"http://www.imsdb.com/scripts/Revenant,-The.html",
"http://www.imsdb.com/scripts/Star-Wars-The-Force-Awakens.html",
"http://www.imsdb.com/scripts/Interstellar.html",
"http://www.imsdb.com/scripts/Foxcatcher.html",
"http://www.imsdb.com/scripts/How-to-Train-Your-Dragon-2.html"]
for script in scripts:
    print script
    raw = get_script(script)
    process_for_indents(raw)
    print '\n\n'
