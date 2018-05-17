import os
import csv

# C:\PythonScripts\Resources (My Path)
csvpath = os.path.join('..', 'PythonScripts\Resources', 'web_starter.csv')
with open(csvpath, 'r', encoding = 'utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        print(row)


# Specify the file to write to
output_path = os.path.join("..", "PythonScripts\Resources", "web_ender.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
        # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)

    # 'id','title','url','isPaid','price','numSubscribers','numReviews','numPublishedLectures','instructionalLevel','contentInfo','publishedTime'
    csvwriter.writerow(['id','title','url','isPaid','price','numSubscribers','numReviews','numPublishedLectures','instructionalLevel','contentInfo','publishedTime'])
        