import pdfminer.high_level as pdfh
import docx
import sys

if __name__ == "__main__":
    try:
        result = ''
        if sys.argv[1][-3:] == 'pdf':
            print(sys.argv[1][-3:])
            result = pdfh.extract_text(sys.argv[1])
        elif sys.argv[1][-4:] == 'docx' or sys.argv[1][-3:] == 'doc':
            doc = docx.Document(sys.argv[1])
            result = [p.text for p in doc.paragraphs]
        print(result)

    except:
        print("ERR NO FILE, FORMAT: python DocScrapper.py <pdf U doc>")
        

# open connection to Word Document
#doc = docx.Document("zen_of_python.docx")
 
# read in each paragraph in file
