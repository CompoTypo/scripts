import sys
import io
import re


def CleanlyWrite(in_csv_file, out_file_name):
    out_set = open(out_file_name, 'w+')
    for line in in_set:
        words = line.split(',')
        words[-1] = words[-1].strip('\n')
        words[-1] = words[-1].replace('.', '')

        for word in words:
            word = word.replace('\"', '')
            word = word.replace(' ', '')
            if re.match(r'^([+-]?[1-9]\d*|0)$', word):  # if string matches an integer type
                int(word[0])
                out_set.write(word + ',')
            # if string matches an float type
            elif re.match(r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$', word):
                float(word[0])
                out_set.write(word + ',')
            # if there is no data (MAY NEED ADDITIONS)
            elif word == '?' or re.match(r'/(n[\/]?a)/gi', word):
                out_set.write('NA,')
            else:  # otherwise just handle it as a string
                out_set.write('\"' + word + '\",')
        out_set.write('\n')


# Clean dataset
in_set = open(sys.argv[1])
if len(sys.argv) != 3:
    print("ERR Format: python cleaner.py <path/infile> <path/outfile>")
else:
    CleanlyWrite(in_set, sys.argv[2])
