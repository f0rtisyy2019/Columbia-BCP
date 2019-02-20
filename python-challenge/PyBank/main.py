import os
import csv

total_month = 0
total = 0
average_change = 0
greatest_inc = 0
greatest_dec = 0
greatest_inc_month = ""
greatest_dec_month = ""
previous = 0
change = []

budgetCSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'budget_data.csv')
with open(budgetCSV, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)

	for row in csvreader:
		total_month += 1
		profit = int(row[1])
		total += profit

		if (total_month > 1):
			current_change = profit - previous
			change.append(current_change)
			if current_change > greatest_inc:
				greatest_inc = current_change
				greatest_inc_month = row[0]
			if current_change < greatest_dec:
				greatest_dec = current_change
				greatest_dec_month = row[0]

		previous = profit
	average_change = sum(change) / (total_month - 1) 

results = ['Financial Analysis']
results.append('----------------------------')
results.append(f"Total Months: {total_month}")
results.append(f"Total: ${total}")
results.append("Average  Change: $%.2f" % average_change)
results.append(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
results.append(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")

result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results.txt')
f = open(result_file, 'w+')
for result in results:
	print(result)
	f.write(result + '\n')
f.close()