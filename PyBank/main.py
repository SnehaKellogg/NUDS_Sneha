#Import necessary packages
import os
import csv
import sys

#define the file used
bankbudget = os.path.join("Resources", "budget_data.csv")


#open csv and use it to create lists of header items
with open(bankbudget, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    headers = next(reader, None)
    column = {}
    for h in headers:
        column[h] = []

    for row in reader:
        for h,v in zip(headers,row):
            column[h].append(v)

    #Check type for the profit loss
    #print(type(column['Profit/Losses'][1]))

    #convert string to float for this column entries
    profits = [float(i) for i in column['Profit/Losses']]
    #print(type(profits[1])) #//confirm the change

    #find the difference
    difference = [profits[i+1]-profits[i] for i in range(len(profits)-1)]

    #account for 1st missing element
    missing = 0
    difference = [missing] + difference

    ##Open this section to create a csv with additional columns
    # #zip this new column in the initial disctionary
    # analysis = zip(column['Date'], profits, difference)
    #
    # output_file = os.path.join("budget_final.csv")
    # #  Open the output file
    # with open(output_file, "w", newline="") as datafile:
    #     writer = csv.writer(datafile)
    # # Write the header row
    #     writer.writerow(["Date", "Profits", "Difference"])
    #
    # #Write in zipped rows
    #     writer.writerows(analysis)


    #Perform analysis and print the results:
    sys.stdout = open('finances.txt', 'w')
    print(f"Financial Analysis \n"
          f"-----------------------\n"
          f"Total Months: {len(column['Date'])} \n"
          f"Total: ${int(sum(profits))} \n"
          f"Average Change: ${round((sum(difference)/(len(difference)-1)),2)} \n"
          f"Greatest Increase in Profits: {column['Date'][difference.index(max(difference))]} (${int(max(difference))}) \n"
          f"Greatest Decrease in Profits: {column['Date'][difference.index(min(difference))]} (${int(min(difference))}) ")

