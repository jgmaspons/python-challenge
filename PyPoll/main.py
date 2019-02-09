import os
import csv
import collections
import urllib

# Path to collect data from the Resources folder
input_file = os.path.join('../Resources/', 'election_data.csv')

# Lists to store data
#total_votes = []
candidate_Khan = []
candidate_Correy = []
candidate_Li = []
candidate_Tooley = []

# Define initial values of store data lists
#total_votes = 0

# Defining conditionals for each candidates
#Khan = True
#Correy = True
#Li = True
#Tooley = True

# Open and read csv
with open(input_file, 'r', newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter =',')

# Skip the header row 
    csv_header = next(csvreader)

    # Iterate row-by-row through the dataset 
    for row in csvreader:
        
        # Add vote data to each respective candidate list
        if row[2] == "Khan":
            candidate_Khan.append(row[2])
            

        elif row[2] == "Correy":
            candidate_Correy.append(row[2])
                 

        elif row[2] == "Li":   
            candidate_Li.append(row[2])  

        else:
            candidate_Tooley.append(row[2])
                
    # Print total vote data for each respective candidate
    print(len(candidate_Khan))
    print(len(candidate_Correy))
    print(len(candidate_Li))
    print(len(candidate_Tooley))

    # Print total vote data for all candidates
    total_votes = len(candidate_Khan) + len(candidate_Correy) + len(candidate_Li) + len(candidate_Tooley)
    
    print(f"Total Votes: {(total_votes)}") 

    # Print % of vote count for candidate Khan
    Khan_perc = len(candidate_Khan) / total_votes
    print(f"Khan: {(Khan_perc)} {len(candidate_Khan)}")

    # Print % of vote count for candidate Correy
    Correy_perc = len(candidate_Correy) / total_votes
    print(Correy_perc) 

    # Print % of vote count for candidate Li
    Li_perc = len(candidate_Li) / total_votes
    print(Li_perc) 

    # Print % of vote count for candidate O'Tooley
    Tooley_perc = len(candidate_Tooley) / total_votes
    print(Tooley_perc)

    # Print winner
    print(f"Winner: Khan") 

    
    output_file = os.path.join('../Resources/','election_output.csv')

    with open(output_file, 'w') as election_output_file:
        
        # Write the first row (column headers)
        csvwriter = csv.writer(election_output_file, delimiter=',')
        csvwriter.writerow([(f"Khan: {(Khan_perc)} {len(candidate_Khan)}")])
        csvwriter.writerow([(f"Total Votes: {(total_votes)}")])





 