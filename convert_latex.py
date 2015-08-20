
## Author : Daesung Park
## Date : 2015.08.10
## This script sorts the acronym list by the short name.
## acro{<acronym>}[<short name>]{<full name>}


import re
from operator import itemgetter
import sys

## define the file_path
file_path = "./my_acronym_acronym_package.tex"
a = []
with open(file_path, 'r') as fp:
    for line in fp:
        #print line
        #if line.startswith("%"): continue
        #if line.startswith("\begin"): continue
        #if line.startswith("\end"): continue
        match = re.match(r'\\acro\{(.*?)\}\[(.*?)\]\{(.*?)\}', line)
        if not match: continue
        a.append(match.groups())

a_sort = sorted(a, key=itemgetter(1))

template = r'{0}, {1}, {2}'

## define the output file name
f = open('acronym_sorted_.txt', 'w')

sys.stdout = f
#print r"\begin{acronym}"
print r"## short name, acronym, long name"
for (x,y,z) in a_sort:
    print template.format(x,y,z)

#print r"\end{acronym}"

f.close()
