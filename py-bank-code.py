import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

print('Financial Results')

total_months = 0
total = 0
average = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = "" 

with open(budget_data, 'r') as file_handler:
    csv_reader = csv.reader(file_handler)
    next(csv_reader)

    previous_profit = 0
    profit_changes = []

    for row in csv_reader:
        total_months += 1
        total += int(row[1])
        
        if total_months > 1:
            profit_change = int(row[1]) - previous_profit
            profit_changes.append(profit_change)
            if profit_change > greatest_increase:
                greatest_increase = profit_change
                greatest_increase_month = row[0]
            if profit_change < greatest_decrease:
                greatest_decrease = profit_change
                greatest_decrease_month = row[0]
        previous_profit = int(row[1])

if total_months > 1:
    average = sum(profit_changes) / len(profit_changes)

print("Total Months:", total_months)
print("Total:", total)
print("Average Change:", round(average, 2))
print("Greatest Increase in Profits:", greatest_increase_month, "($", greatest_increase, ")")
print("Greatest Decrease in Profits:", greatest_decrease_month, "($", greatest_decrease, ")")

