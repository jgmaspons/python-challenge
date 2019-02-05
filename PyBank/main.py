import os
import csv
import collections
import urllib

# Path to collect data from the Resources folder
input_file = os.path.join('../Resources/', 'budget_data.csv')

# Lists to store data
dateRec = []
profit_loss = []
change_profit_loss = []
#avg_change_profit_loss = []

# Open and read csv
with open(input_file, 'r', newline="") as budget_data:
    csvreader = csv.reader(budget_data, delimiter =',')

# Read the header row first 
    csv_header = next(csvreader)

                    # Define the function and have it accept the 'budgetData' as its sole parameter
                    #def getAnalysis(budgetData):
    
    #Total number of months included in the dataset
    for row in csvreader:

        dateRec.append(row[0])
        profit_loss.append(row[1])
        
        value = len(list(budget_data))
        print(value)

    # Net total amount of Profit/Losses over the entire period
    #value_sum = 0
    #for row in csvreader:  

        #value_sum += float(row[1])

        
        #print(value_sum)               
                    
                    
    # The average of the changes in "Profit/Losses" over the entire period 
        #for row in csvreader:
            #dateRec.append(row[0])
            #profit_loss.append(row[1])
    
    
    for i in range(1, len(profit_loss)):
        
        change_profit_loss.append(float(profit_loss[i]) - float(profit_loss[i-1]))
 
        
        #print (max(change_profit_loss))
        #print(min(change_profit_loss))

        #avg_change_profit_loss = 
        #print(change_profit_loss)
        average_change = (sum(change_profit_loss)) / value
        print(average_change)
            
      

    # The greatest increase in profits (date and amount) over the entire period


    # The greatest decrease in losses (date and amount) over the entire period



                    # Read in the CSV file

                    #with open(input_file, 'r', newline="") as budget_data:

                        # Split the data on commas
                        #csvreader = csv.reader(budget_data, delimiter=',')
                        #csv_header = next(csvreader)

                        # Split the data on commas
                        
                        
                        # Write data to a .csv file
                        # with open(pybankCSV, "w", newline="") as csvfile:
                            # writer = csv.writer(csvfile)

                        # To save specific data input as a row in the csv file
                            # writer.writerow(["row1", "row2"])


                        #header = next(csvreader)

                        # Loop through the data
                    

                        
                        # Run the 'financialAnalysis()' function 
                        #getAnalysis(row)

                        #for row in csvreader:

                            #if float(row[1]) > 0:
                                #print(row)

   
