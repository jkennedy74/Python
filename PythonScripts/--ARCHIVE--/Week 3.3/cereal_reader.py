
import os
import csv

csvpath = os.path.join('..', 'PythonScripts\Resources', 'cereal.csv')

# Open and read CSV # This is called a context manager. Parameters:  Path, ...
with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',') #Takes in the file and specifies a delimiter
   
    #  Each row is read as a row
    for row in csvreader:

         if float(row[7]) >= 5:
            print(row)
            