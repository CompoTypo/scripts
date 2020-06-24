import sys
import os

def createSchema(dir):
    out = open('./schema2.sql', 'w+')
    out.write('DROP SCHEMA IF EXISTS foodsources;\n')
    out.write('CREATE SCHEMA foodsources;\n\n')
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file[-4:] == '.csv':
                out.write('DROP TABLE IF EXISTS ' + file[:-4] + ';\n')
                out.write('CREATE TABLE ' + file[:-4] + ' (\n')
                csv = open(dir + file, 'r')
                headers = csv.readline()
                for header in headers.split(','):
                    header = header.replace(' ', '_').strip('\"\n')
                    t = ''
                    if header.find('id') >= 0 or header.find('num') >= 0:
                        t = ' BIGINT UNSIGNED'
                        t += ',' if header != 'id' else ' NOT NULL AUTO_INCREMENT,'
                    elif header.find('date') >= 0: 
                        t = ' TIMESTAMP NOT NULL,'
                    else:
                        t = ' VARCHAR(255),'
                    out.write('\t' + header.replace(' ', '_') + t + '\n')
                out.write(');\n\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('ERR format: python3 csvToSql.py <path/to/csv>')
    else:
        createSchema(sys.argv[1])
