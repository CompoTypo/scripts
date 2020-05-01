import sys
import io
import os

if len(sys.argv) != 2:
    print('ERR Format: python mkproj.py <project-name>')
    quit()

os.makedirs(sys.argv[1], exist_ok=True)
os.chdir(sys.argv[1])
rdme = open('README.md', 'w+')
rdme.write('#  ' + sys.argv[1] + '  \n')
rdme.write('##  Description  \n')
rdme.write('##  Usage  \n')
rdme.close()
