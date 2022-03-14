import sys
import csv
#sys.argv[0] = python file Name
#sys.argv[1] = next arguement
#etc...


def main(fileName,choice):
    file = open(fileName+".txt", "r")
    fileFormat =''

    if choice == '-c':
        fileFormat = 'HW2.csv'
    elif choice == '-j':
        fileFormat = 'HW2.json'
    elif choice == '-x':
        fileFormat = 'HW2.xml'

    with open(fileFormat, 'w', encoding = 'UTF8') as f:
        a = True
        while a:
            writer = csv.writer(f)
            text = file.readline()
            if not text:
                a = False
            else: 
                x = text.split()
                writer.writerow(x)

main(sys.argv[1],sys.argv[2]) 
