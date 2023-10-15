import csv

filename = "sample.csv"
with open(filename, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        name = row[0]
        code = row[1]
        print(name)
        print(code)
        print("----")
