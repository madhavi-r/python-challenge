import os
import csv

profit_loss = []
months = []
month_change = []
count = 0
i = 0

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

        max_profit = profit_loss.index(max(profit_loss))
        max_profit_month = months[max_profit]
        min_profit = profit_loss.index(min(profit_loss))
        min_profit_month = months[min_profit]
    #calculate average change            
    for i in range(1, len(profit_loss)):
        change = profit_loss[i] - profit_loss[i-1]
        month_change.append(change)
        count += 1
    i += 1
    
average_change = round(float(sum(month_change)/count),2)

print("Financial Analysis")
print("______________________________________________")
print(f"Total Months : {str(total_months)}")
print(f"Total : ${str(total_of_profit_loss)}")
print(f"Average Change : ${str(average_change)}")
print(f"Greatest Increase in Profits : {str(max_profit_month)} (${str(max(month_change))})")
print(f"Greatest Decrease in Profits : {str(min_profit_month)} (${str(min(month_change))})")

budgetoutput = os.path.join('budget.txt')

budgetfile = open('budget.txt','w')
    
budgetfile.write("Financial Analysis\n") 
budgetfile.write("______________________________________________\n")
budgetfile.write("Total Months : " + str(total_months) + "\n")
budgetfile.write("Total : $" + str(total_of_profit_loss) + "\n")
budgetfile.write("Average Change : $" + str(average_change)+ "\n")
budgetfile.write("Greatest Increase in Profits : " + str(max_profit_month) + " ($" + str(max(month_change)) + ")\n")
budgetfile.write("Greatest Decrease in Profits : " + str(min_profit_month) + " ($" + str(min(month_change)) + ")")
    
budgetfile.close()