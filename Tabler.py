from bs4 import BeautifulSoup
import sys

html = open(sys.argv[1])

soup = BeautifulSoup(html.read(), 'html.parser')

headers = [] 
for raw_header in soup.select('thead tr th'): #.text.strip()
    headers.append(raw_header.text.strip())
    print(raw_header.text.strip())


data = []
for raw_row in soup.select('tbody tr'):
    row = []
    for raw_row_data in raw_row.select('td'):
        row.append(raw_row_data.text.strip())
        #print(raw_row_data.text.strip())
        pass
    data.append(row)


for row in data:
    print(row[0])