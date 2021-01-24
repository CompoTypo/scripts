from dataclasses import dataclass
import sys

stdToTSDict = {
    '<assert.h>': None, # builtin
    '<complex.h>': None, # builtin
    '<ctype.h>': None, # builtin types
    '<errno.h>': None, # not necessary
    '<fenv.h>': None, # floating point handled already
    '<float.h>': None, # floating point handled already
    '<inttypes.h>': None, # floating point handled already 
    '<iso646.h>': None,
    '<limits.h>': None,
    '<locale.h>': None,
    '<math.h>': None,
    '<setjmp.h>': None,
    '<signal.h>': None,
    '<stdalign.h>': None,
    '<stdarg.h>': None,
    '<stdatomic.h>': None,
    '<stdbool.h>': None,
    '<stddef.h>': None,
    '<stdint.h>': None,
    '<stdio.h>': None,
    '<stdlib.h>': None,
    '<stdnoreturn.h>': None,
    '<string.h>': None,
    '<tgmath.h>': None,
    '<threads.h>': None,
    '<time.h>': None,
    '<uchar.h>': None,
    '<wchar.h>': None,
    '<wctype.h>': None
}


def cCheck(file_name):
    if file_name[-2:] == '.c':  # or file_name[-4:] == '.cpp'
        return True
    return False


def toTypeScript(file_name):
    infile = open(file_name, 'r')
    outfile = open(file_name[-2:0] + '.ts', 'w+')

    def isIncludeLine(incPrefix):
        if incPrefix.strip() == '#include':
            return True
        return False

    def handleIncludeLine():

    rParen = []
    lParen = []

    lines = infile.readlines()
    for line in lines:
        words = line.split(' ')

        # handles std
        if isIncludeLine(words[0]):
            handleIncludeLine(words)

        for word in words:
            print(word)


if cCheck(sys.argv[1]):
    toTypeScript(sys.argv[1])
