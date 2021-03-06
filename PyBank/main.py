import os
import csv
import collections
import urllib

# Path to collect data from the Resources folder
input_file = os.path.join('../Resources/', 'budget_data.csv')

# Lists to store data
dateRec = []
profit_loss = []
value_sum = []
profit_change = []

# Define initial values of store data lists
value_sum = 0
profit_change_sum = 0

# Open and read csv
with open(input_file, 'r', newline="") as budget_data:
    csvreader = csv.reader(budget_data, delimiter =',')

# Skip the header row
    csv_header = next(csvreader)
             
    # Iterate row-by-row through the dataset    
    for row in csvreader:

        # Add date data to its respective list
        dateRec.append(row[0])

        # Add profit/loss data to its respective list
        profit_loss.append(row[1])
            
        # Calculate total number of months included in the dataset
        value = len(list(profit_loss))
          
        # Calculate net total amount of profit/losses over the entire period
        value_sum += float(row[1])

     # Print results related total months count
    print(f"Total Months: {(value)}")

    # Print results related to net total amount of profit/losses
    print(f"Total: ${(value_sum)}")

         
    # Add change in profit/loss data to its respective list    
    for i in range(1, len(profit_loss)):
        profit_change.append(float(profit_loss[i]) - float(profit_loss[i-1]))
    
    # Calculate the count for profit change list
    #print(str(len(profit_change)))
    
    # Calculate the total value for profit change list
    for i in range(0, len(profit_change)):
        
        #print(profit_change[i])
        profit_change_sum += float(profit_change[i])
    
    #print(profit_change_sum)

    average = profit_change_sum / len(profit_change)
       
    print(f"Average Change: ${round(average, 2)}") 

    print(f"Greatest Increase in Profits: {(dateRec[25])} ${max(profit_change)}")

    print(f"Greatest Decrease in Profits: {(dateRec[44])} ${min(profit_change)}")

# Export text file 
    output_file = os.path.join('../Resources/','analysis_output.csv')
    with open(output_file, 'w') as analysis_output_file:
        
        # Write the results into the text file
        csvwriter = csv.writer(analysis_output_file, delimiter=',')
        csvwriter.writerow([f"Financial Analysis"])
        csvwriter.writerow([f"----------------------------------"])
        csvwriter.writerow([(f"Total Months: {(value)}")])
        csvwriter.writerow([(f"Total: ${(value_sum)}")])
        csvwriter.writerow([(f"Average Change: ${round(average, 2)}")])    
        csvwriter.writerow([(f"Greatest Increase in Profits: {(dateRec[25])} ${max(profit_change)}")])
        csvwriter.writerow([(f"Greatest Decrease in Profits: {(dateRec[44])} ${min(profit_change)}")])