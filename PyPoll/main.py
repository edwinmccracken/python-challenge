import os
import csv

poll_data_csv = os.path.join('election_data.csv')

with open(poll_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)