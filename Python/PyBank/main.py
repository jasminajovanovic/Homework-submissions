import os
import csv

total_profit = 0
monthly_records = []
total_change = 0
monthly_change = 0
total_monthly_change = 0
greatest_profit_increase = [0,""]
smallest_profit_increase = [0,""]
monthly_change_list = []

csvpath = os.path.join('.', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_profit += int(row[1])
        monthly_records.append(row)
    
    for i in range(len(monthly_records)):
        
        # skip the first row, since we don't know what the delta is
        if i != 0:
            previous_month_total = int(monthly_records[i-1][1])
            this_month_total = int(monthly_records[i][1])
            monthly_change = this_month_total - previous_month_total 
            monthly_change_list.append(monthly_change)
        
        if (greatest_profit_increase[0] < monthly_change):
            greatest_profit_increase[0] = monthly_change
            greatest_profit_increase[1] = monthly_records[i][0]
        if (smallest_profit_increase[0] >= monthly_change):
            smallest_profit_increase[0] = monthly_change
            smallest_profit_increase[1] = monthly_records[i][0]
            
            
    print ("Last month profit: " + str(int(monthly_records[-1][1])) + " and first month profit: " + str(int(monthly_records[0][1])))    
    #total_monthly_change = int(monthly_records[-1][1])-int(monthly_records[0][1])
    total_monthly_change = sum(monthly_change_list)
    total_months = csvreader.line_num -1
    print ("Total months:" + str(total_months))
    print ("Total: " + str(total_profit))
    print ("Total monthly change is: " + str(total_monthly_change))
    print ("Average monthly change is: " + str(round(total_monthly_change/(total_months-1),2)))
    print ("Greatest monthly increase is: " + str(greatest_profit_increase [1] + " " + str(greatest_profit_increase[0])))
    print ("Smallest monthly increase is: " + str(smallest_profit_increase[1] + " " + str(smallest_profit_increase[0])))
    