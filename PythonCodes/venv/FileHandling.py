import csv
rows = []
with open("cpudatatextad.csv", 'r') as file:
   csvreader = csv.reader(file)
   header = next(csvreader)
   for row in csvreader:
       rows.append(row)
print(header)
print(rows)

with open('cpudatatextad.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[3:]
print(header)
print(rows)


#pip install notebook

#pip3 install jupyter

#python -m pip install jupyter