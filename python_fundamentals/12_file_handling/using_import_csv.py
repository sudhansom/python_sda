import csv

with open("textfiles/covid-19_data.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)
        break
