import sys
import re
import os

def buildTableData(csv, f, attrs, out):
    r = csv.readline()
    while True:
        values = []
        types = []
        if r == '':
            break
        for col in r.split(','):
            val = col.replace(' ', '_').strip('\"\n')
            if re.match('^\d+$', val):
                types.append('INTEGER')
            elif re.match('[+-]?([0-9]*[.])?[0-9]+'):
                types.append('FLOAT')
            values.append(val)
        
        out.write('INSERT INTO ' + f + ' (' + str(attrs).strip('\[\'\'\]').replace("'", "") + ') VALUES (' + str(values).strip('\'\[\]\'').replace("'", "") + ');\n')
        r = csv.readline()

def buildTable(dir, f, out):
    out.write('DROP TABLE IF EXISTS ' + f[:-4] + ';\n')
    out.write('CREATE TABLE ' + f[:-4] + ' (\n')
    csv = open(dir + f, 'r')
    headers = csv.readline().split(',')
    for i in range(len(headers)):
        headers[i] = headers[i].replace(' ', '_').strip('\"\n')
        line_comma = ',' if len(headers)-1 != i else ''
        if headers[i] == "":
            headers[i] = 'id'
        if headers[i].find('id') >= 0 or headers[i].find('num') >= 0:
            t = ' BIGINT UNSIGNED'
            t += ',' if headers[i] != 'id' else ' NOT NULL AUTO_INCREMENT PRIMARY KEY' + line_comma
        elif headers[i].find('date') >= 0: 
            t = ' TIMESTAMP NOT NULL' + line_comma
        else:
            t = ' VARCHAR(255)' + line_comma
        out.write('\t' + headers[i].replace(' ', '_') + t + '\n')
    out.write(');\n\n')
    buildTableData(csv, f[:-4], headers, out)

def getFileName():
    return input('Enter a better filename for the schema file: ')

def createSchema(dir):
    out = ''
    if dir == './':
        file_name = getFileName()
        out = open('./' + file_name + '.sql', 'w+')
        out.write('DROP SCHEMA IF EXISTS ' + file_name + ';\n')
        out.write('CREATE SCHEMA ' + file_name + ';\n\n')
        out.write('USE ' + file_name + ';\n\n')
    else:
        out = open('./' + dir + '.sql', 'w+')
        out.write('DROP SCHEMA IF EXISTS ' + dir + ';\n')
        out.write('CREATE SCHEMA ' + dir + ';\n\n')
        out.write('USE ' + dir + ';\n\n')

    for subdir, dirs, files in os.walk(dir):
        for f in files:
            if f[-4:] == '.csv':
                buildTable(dir, f, out)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('ERR format: python3 csvToSql.py <path/to/csv>')
    else:
        createSchema(sys.argv[1])
