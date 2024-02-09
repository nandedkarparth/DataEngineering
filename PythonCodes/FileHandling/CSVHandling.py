import csv
rows = []
with open("employees.csv", 'r') as file:
   csvreader = csv.reader(file)
   header = next(csvreader)
   for row in csvreader:
       rows.append(row)
print(header)
print(rows)