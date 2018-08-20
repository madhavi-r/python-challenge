import os
import csv

profit_loss = []
months = []
i = 0
positive_change = []
negative_change = []
count = 0


budgetdatapath = os.path.join('budget_data.csv')

with open(budgetdatapath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter='\t')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        months.append(row[0])
        total_months = len(months)
        profit_loss.append(int(row[1]))
        total_of_profit_loss = sum(profit_loss)
        #calculate average change
        
        
print(f"Total Months : {str(total_months)}")
print(f"Total of Profit/Losses : {str(total_of_profit_loss)}")
#print(f"Positive Change : {str(total_positive)}")
    

