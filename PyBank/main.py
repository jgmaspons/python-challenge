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
change_profit_loss = []

# Define initial values of store data lists
value_sum = 0
change_profit_loss = 0

# Open and read csv
with open(input_file, 'r', newline="") as budget_data:
    csvreader = csv.reader(budget_data, delimiter =',')

# Read the header row first 
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
         
    # Add change in profit/loss data to its respective list
    #for i in len(list(profit_loss): 
        #change_profit_loss.append(float(profit_loss([i]) - float(profit_loss([i-1]))     


        # Add data to its range list
        
        #def average(change_profit_loss):
            #length = len(list(change_profit_loss)
                  
            #for average in change_profit_loss
                #change_profit_loss += float(row[
            #return length


        #avg_change_profit_loss = 
        #print(change_profit_loss)
        #average_change = sum(change_profit_loss) / value
        #print(average_change)
            
    # Print results related total months count
    print(value)

    # Print results related to net total amount of profit/losses
    print(value_sum)

    # Print results related to avg. change in profit/loss amount
    #print(average(change_profit_loss))
    #print(change_profit_loss)

    # The greatest increase in profits (date and amount) over the entire period


    # The greatest decrease in losses (date and amount) over the entire period


        #print (max(change_profit_loss))
        #print (min(change_profit_loss))

             