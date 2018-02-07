import os
import csv

budget_number = ['1', '2']

for budget_data in budget_number:

    file = os.path.join('raw_data', 'budget_data_' + str(budget_data) + '.csv')

    #create lists for months and revenues

    months = []
    revenue = []

    #open csv as read
    with open(file, 'r') as csvfile:

        csvread = csv.reader(csvfile)

        next(csvread, None)

        for row in csvread:

            months.append(row[0])
            revenue.append(int(row[1]))

    total_months = len(months)

    #create greatest monthly revenue increase and decrease

    greatest_increase = revenue[0]
    greatest_decrease = revenue[0]
    total_revenue = 0

    #loop through revenue and calculate greatest increase and greatest decrease

    for r in range(len(revenue)):

        if revenue[r] >= greatest_increase:

            greatest_increase = revenue[r]
            greatest_increase_month = months[r]

        elif revenue[r] <= greatest_decrease:

            greatest_decrease = revenue[r]
            greatest_decrease_month = months[r]

        total_revenue += revenue[r]

    #calculate average_change

    average_change = round(total_revenue/total_months, 2)

    #create output file

    output = os.path.join('Output','budget_results_' + str(budget_data) + '.txt')

#print summary to output file

    with open(output, 'w') as writefile:

        writefile.writelines('Financial Analysis\n')
        writefile.writelines('-'*20 + '\n')
        writefile.writelines('Total Months: ' + str(total_months) + '\n')
        writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
        writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
        writefile.writelines('Greatest Increase in Revenue: ' + greatest_increase_month + ' $' + str(greatest_increase) + '\n')
        writefile.writelines('Greatest Decrease in Revenue: ' + greatest_decrease_month + ' ($' + str(greatest_decrease) + ')')





