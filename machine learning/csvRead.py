import csv
with open('winequality-red.csv') as csvfile:
    readCsv = csv.reader(csvfile,delimiter=',')
    print(readCsv)
    
    for row in readCsv:
       print(row)
       

