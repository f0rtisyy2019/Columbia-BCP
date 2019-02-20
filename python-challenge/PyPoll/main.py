import os
import csv

election = {"winner": ""}
total_votes = 0
winner_votes = 0

electionCSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'election_data.csv')
with open(electionCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        if row[2] in election:
            election[row[2]] += 1
        else:
            election[row[2]] = 1

    for key, value in election.items():
        if key != "winner" and value > winner_votes:
            winner_votes = value
            election['winner'] = key

results = ['Election Results']
results.append('----------------------------')
results.append(f"Total Votes: {total_votes}")
results.append('----------------------------')
for key, value in election.items():
    if key != "winner":
        results.append(f"{key}: " + "{:.3%} ".format(value/total_votes) + f"({value})")
results.append('----------------------------')
results.append(f"Winner: {election['winner']}")
results.append('----------------------------')

result_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results.txt')
f = open(result_file, 'w+')
for result in results:
    print(result)
    f.write(result + '\n')
f.close()