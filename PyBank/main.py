import os
import csv

budget_data_csv = os.path.join('budget_data.csv')

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)