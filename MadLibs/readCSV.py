import csv
with open('nouns.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)