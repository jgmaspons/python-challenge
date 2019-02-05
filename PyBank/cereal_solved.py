import os
import csv

#cereal_csv = os.path.join("..", "Resources", "cereal.csv")

# Open and read csv
# with open(cereal_csv, newline="") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")


# NEW CODE
input_file = os.path.join('../Resources/', 'test1__data.csv')

with open(input_file, 'r', newline="") as test1__data:
    csvreader = csv.reader(test1__data, delimiter =',')
    csv_header = next(csvreader)


    # Read the header row first (skip this part if there is no header)
    # csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:

        # Convert row to float and compare to grams of fiber
        if float(row[1]) >= 1100000:
            print(row)
