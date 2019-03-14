import os
from itertools import chain
from glob import glob

filename = "capitals.txt"

f = open(filename, 'r')
text = f.read()
#print(text)

lines = [text.lower() for line in filename]
with open("unCapitals.txt", 'w') as out:
    out.writelines(lines)
    print(lines)