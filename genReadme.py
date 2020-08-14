import sys
import io
import os

if len(sys.argv) == 2:
    os.chdir(sys.argv[1])

dirName = os.path.basename(os.getcwd())
rdme = open('README.md', 'w+')
rdme.write('#  ' + dirName + '  \n')
rdme.write('##  Description  \n')
rdme.write('##  Usage  \n')
rdme.close()
