import os
import csv

budget_data_csv = os.path.join('budget_data.csv')

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)


file = open(budget_data_csv, 'r')
numline_months = len(file.readlines())
numline_months = numline_months - 1
print(numline_months)

with open (budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = None
    for row in csvreader:
        if header is None:
            header = row
            mySums=[0]*len(row)
            continue
        else:
            for i,x in enumerate(row):
                try:
                    converted=float(x)
                except ValueError:
                    converted = 0
                mySums[i]+=converted

                print(mySums)