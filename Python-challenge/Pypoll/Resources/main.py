import os
import csv

csvpath = os.path.join("election_data.csv")

count = 0
candidates = []
unique_candidate = []
vote_count = []
vote_percent = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        count = count + 1
        candidates.append(row[2])
    for x in set(candidates):
        unique_candidate.append(x)
        y = candidates.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)
        
    winner_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winner_vote_count)]
     
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

with open('results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")