#Import necessary packages
import os
import csv
# import numpy as np

#define the file used
electorallist = os.path.join("Resources", "election_data.csv")


#open csv and use it to create lists of header items
with open(electorallist, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    headers = next(reader, None)
    column = {}
    for h in headers:
        column[h] = []

    for row in reader:
        for h,v in zip(headers,row):
            column[h].append(v)

    # #Check exact headers
    print(headers) #\\ ['Voter ID', 'County', 'Candidate']

    #create a set from list to remove duplicates
    votes = []
    names = []
    candidates = {*column['Candidate']}
    candidates = list(candidates)
    for c in candidates:
        #names.append(column['Candidate'](c))
        votes.append(column['Candidate'].count(c))

    # print(votes, candidates)

    #Perform analysis and print the results:
    print(f"Election Results \n"
          f"-----------------------\n"
          f"Total Votes: {sum(votes)} \n"
          f"-----------------------\n")
    for i in range(len(votes)):
        print(f"{candidates[i]}: {round((votes[i]/sum(votes)*100),3)}% ({votes[i]}) \n")

    print(f"Winner: {candidates[votes.index(max(votes))]}")
