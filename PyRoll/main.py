#Import necessary packages
import os
import sys
import csv

#define the file used
electorallist = os.path.join("Resources", "election_data.csv")

#open csv and use it to create lists of header items
with open(electorallist, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    headers = next(reader, None)
    column = {}
    for h in headers:
        column[h] = []

#create zipped version for the full list for use
    for row in reader:
        for h,v in zip(headers,row):
            column[h].append(v)

    # #Check exact headers
    #print(headers) #\\ ['Voter ID', 'County', 'Candidate']

    #create a set from list to remove duplicates
    votes = []
    names = []
    candidates = {*column['Candidate']}
    #convert the set to list so that it has indexes and is callable
    candidates = list(candidates)

    #adding vote entries to ensure it is in same index as candidates
    for c in candidates:
        votes.append(column['Candidate'].count(c))

    #Perform analysis and print the results:
    sys.stdout = open('election_results.txt', 'w')
    print(f"Election Results \n"
          f"-----------------------\n"
          f"Total Votes: {sum(votes)} \n"
          f"-----------------------\n")
    for i in range(len(votes)):
        print(f"{candidates[i]}: {round((votes[i]/sum(votes)*100),3)}% ({votes[i]}) \n")

    print(f"Winner: {candidates[votes.index(max(votes))]}")

