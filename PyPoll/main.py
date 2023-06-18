import os
import csv

#Initialize file paths
csvpath = os.path.join('Pypoll','Resources','election_data.csv')
output = os.path.join('Pypoll','analysis','Results.txt')

#initialize counters
totalv = 0
candidates = {}
winner = ""
winner_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csvheader = next(csvreader)
    for row in csvreader: #Evaluate each row and step each counter appropriately
        person = row[2]
        totalv += 1
        if person in candidates: #Add candidate to dictionary or increment candidate total votes
            candidates[person] += 1
        else:
            candidates[person] = 1

#Using a list to output results to txt
results = []
results.append("Election Results")
results.append("-----------------------")
results.append(f"Total votes: {totalv}")
results.append("-----------------------")

for person, votes in candidates.items():
    percent = (votes/totalv) * 100
    results.append(f"{person}: {percent:.3f}%, ({votes})")
    if votes > winner_votes:
        winner_votes = votes
        winner = person

results.append("-----------------------")
results.append(f"Winner: {winner}")
results.append("-----------------------")

#Output to terminal
for line in results:
    print(line)

#Output to txt file
with open(output, "w") as file:
    file.writelines(line + "\n" for line in results)

