#PyPoll

import os
import csv

#create path for file
csvpath = os.path.join('..', 'Resources', "election_data.csv")

#create lists to store data
total_votes_cast = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []

#define variables
khan = 'Khan'
correy = 'Correy'
li = 'li'
otooley = "O'Tooley"


#prompt to open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    #add all the rows in the data sheet to get the total vote count
    for row in csvreader:
        total_votes_cast.append(row[0])
        
        #define variable for candidate count and add each name to it's own list
        candidates = row[2]
        if candidates == khan:
            khan_votes.append(candidates)
        if candidates == correy:
            correy_votes.append(candidates)
        if candidates == li:
            li_votes.append(candidates)
        if candidates == otooley:
            otooley_votes.append(candidates)

#find percent vote for each candidate
khan_per_votes = float(len(khan_votes) / len(total_votes_cast) * 100)
khan_pv_round = round(khan_per_votes, 3)

correy_per_votes = float(len(correy_votes) / len(total_votes_cast) * 100)
correy_pv_round = round(correy_per_votes, 3)

li_per_votes = float(len(li_votes) / len(total_votes_cast) * 100)
li_pv_round = round(li_per_votes, 3)

otooley_per_votes = float(len(otooley_votes) / len(total_votes_cast) * 100)
otooley_pv_round = round(otooley_per_votes, 3)


print(f'Total Votes: {len(total_votes_cast)}')
print(f'Khan: {len(khan_votes)}  {(khan_pv_round)}%')
