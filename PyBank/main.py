#Import modules
import os
import csv

#Connect the file path
budget_data_csv = os.path.join('budget_data.csv')

#Set up open statement and loop
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    revenue = []
    date = []
    rev_change = []

    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])

#Set the titles of the analysis
    print("Financial Analysis")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))

 #Figure out the revenue change, min and max values and dates of min and max change
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])

#Print results of 
    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")


with open("FinalResults.txt", "w") as txt_file:

    txt_file.write("Financial Analysis\n")
    txt_file.write(f"Total Months: {len(date)}\n")
    txt_file.write(f"Total Revenue: {sum(revenue)}\n")
    txt_file.write(f"Avereage Revenue Change: ${round(avg_rev_change)}\n")
    txt_file.write(f"Greatest Increase in Revenue Date: {max_rev_change_date}\n")
    txt_file.write(f"Greatest Increase in Revenue Amount: {max_rev_change}\n")
    txt_file.write(f"Greatest Decrease in Revenue: {min_rev_change_date}\n")
    txt_file.write(f"Greatest Decrease in Revenue Amount: {min_rev_change}\n")