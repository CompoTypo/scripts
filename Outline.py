import sys
import io
import re

codeFile = open(sys.argv[1], 'r')
commentFile = open(sys.argv[2], 'w+')

for line in codeFile.readlines():
    if re.search('//', line) or re.search('#', line):
        commentFile.write('Com: ' + line)
        print('Comment: ', line)
    elif re.search('\b[^()]+\((.*)\)$', line):
        commentFile.write('\n\n## FUNCT: ' + line)


