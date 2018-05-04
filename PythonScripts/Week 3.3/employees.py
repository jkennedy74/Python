# Dependencies
import os
import csv

csv_path = os.path.join('..',"PythonScripts\Resources", "employees.csv")
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # pdb.set_trace()

    for row in reader:
         print(row['first_name'], row['last_name'])
