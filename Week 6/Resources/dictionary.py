# Dependencies
import os
import csv

employee_csv_path = os.path.join("..", "PythonScripts\Resources", "employees.csv")
    with open(employee_csv_path, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['first_name'], row['last_name'])



    >>> print(row)
        OrderedDict([('first_name', 'John'), ('last_name', 'Cleese')])
