import os
import csv

total_months = 0
total_sum = 0
max_increase = 0
max_increase_date = ""
max_decrease = 0
max_descrease_date = ""
previous = 0.0
average_change = 0

csvpath = os.path.join('budget_data.csv')
with open (csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader,None)

    for row in csvreader:
        current = float(row[1])
        if total_months == 0:
            max_increase == 0.0
            max_decrease = 0.0
            max_increase_date = row[0]
            max_descrease_date = row[0]
        else:
            analysis = current - previous
            average_change += analysis
            if analysis > max_increase:
                max_increase = analysis
                max_descrease_date = row[0]
            elif analysis < max_decrease:
                max_decrease = analysis
                max_descrease_date = row[0]
        previous = current
        total_months +=1
        total_sum += float(row[1])

average_change = average_change / (total_months-1)

results =[]
results.append("Financial Analusis")
results.append("--------------------------")
results.append(f"Total Months: {total_months}")
results.append(f"Total: ${round(total_sum)}")
results.append(f"Average change: ${round(average_change,2)}")
results.append(f"Greatest Increase in profits: {max_increase_date} (${round(max_increase)})")
results.append(f"Greatest Decrease in Profits: {max_descrease_date} (${round(max_decrease)})")

output = 'Results.txt'
with open (output,'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')