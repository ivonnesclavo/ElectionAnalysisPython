import os
import csv

#Path to Pybank csv
pybank_load = os.path.join('.','Pybank/Resources','budget_data.csv')

#Open and read csv
with open(pybank_load) as pybank_data:
    pybank_reader = csv.reader(pybank_data, delimiter = ',')
    
    #Skip header
    header = next(pybank_reader)
    
    #Set initial variables
    total_months = 1            #To count total number of months
    net_total = 0               #To calcultate the Net Total Profit/Loss      
    total_profit_change = 0     #To calculate total profit change
    min_profit = None           #To store minimum profit change
    max_profit = None           #To store maximum profit change
    min_profit_month = None     #To store month with minimum profit change
    max_profit_month = None     #To store month with maximum profit change
    first_row = next(pybank_reader)
    net_total = int(first_row[1])
    prev_month_profit = net_total
    
    #Loop through
    for row in pybank_reader:
        
        #Add up the total number of months
        total_months += 1
        
        # Extract and add the profit/loss for the current month to the net total
        profit_loss = int(row[1])
        net_total += profit_loss

        # Calculate the profit change for the current month
        profit_change = profit_loss - prev_month_profit

        # Update the previous month's profit/loss for the next iteration
        prev_month_profit = profit_loss

        # Check for the month with the minimum profit change
        if min_profit is None or profit_change < min_profit:
            min_profit = profit_change
            min_profit_month = row[0]

        # Check for the month with the maximum profit change
        if max_profit is None or profit_change > max_profit:
            max_profit = profit_change
            max_profit_month = row[0]

        # Accumulate profit changes
        total_profit_change += profit_change
        
average_profit_change = total_profit_change / (total_months)

# Print the Financial Analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total months: {total_months}")
print("-----------")
print(f"Total Profit/Loss: ${net_total}")
print("-----------")
print(f"Average Change: ${average_profit_change}")
print("-----------")
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})")
print("-----------")
print(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})")

#Export as text
pybank_output = os.path.join('.','Analysis-Results.txt')
with open(pybank_output,'w') as text_file_pybank:
    text_file_pybank.write("Financial Analysis\n")
    text_file_pybank.write("-------------\n")
    text_file_pybank.write(f"Total months: {total_months}\n")
    text_file_pybank.write("-------------\n")
    text_file_pybank.write(f"Total Profit/Loss: ${net_total}\n")
    text_file_pybank.write("-------------\n")
    text_file_pybank.write(f"Average Change: ${average_profit_change}\n")         
    text_file_pybank.write("-------------\n")
    text_file_pybank.write(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})\n")
    text_file_pybank.write("-------------\n")
    text_file_pybank.write(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})\n")

    