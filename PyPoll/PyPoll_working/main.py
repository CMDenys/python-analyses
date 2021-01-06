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
li = 'Li'
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


#find percent vote for each candidate.  Found answer for formatting % here: https://www.kite.com/python/answers/how-to-format-a-number-as-a-percentage-in-python
khan_per_votes = float(len(khan_votes) / len(total_votes_cast))
khan_pv_rounded3 = "{:.3%}".format(khan_per_votes)

correy_per_votes = float(len(correy_votes) / len(total_votes_cast))
correy_pv_rounded3 = "{:.3%}".format(correy_per_votes)

li_per_votes = float(len(li_votes) / len(total_votes_cast))
li_pv_rounded3 = "{:.3%}".format(li_per_votes)

otooley_per_votes = float(len(otooley_votes) / len(total_votes_cast))
otooley_pv_rounded3 = "{:.3%}".format(otooley_per_votes)


print('Election Results')
print('-----------------------------------')
print(f'Total Votes: {len(total_votes_cast)}')
print('-----------------------------------')
print(f'Khan: {khan_pv_rounded3} ({len(khan_votes)})')
print(f'Correy: {correy_pv_rounded3} ({len(correy_votes)})')
print(f'Li: {li_pv_rounded3} ({len(li_votes)})')
print(f"O'Tooley: {otooley_pv_rounded3} ({len(otooley_votes)})")

#specify file to write text to
output_path = os.path.join('..', 'output', 'charliesPyPoll.csv')
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------------------'])
    csvwriter.writerow([(f'Total Votes: {len(total_votes_cast)}')])
    csvwriter.writerow(['-------------------------------------'])
    csvwriter.writerow([(f'Khan: {khan_pv_rounded3} ({len(khan_votes)})')])
    csvwriter.writerow([(f'Correy: {correy_pv_rounded3} ({len(correy_votes)})')])
    csvwriter.writerow([(f'Li: {li_pv_rounded3} ({len(li_votes)})')])
    csvwriter.writerow([(f"O'Tooley: {otooley_pv_rounded3} ({len(otooley_votes)})")])
