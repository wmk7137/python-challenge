# Import Poll Data

import os
import csv

poll_data = os.path.join('Resources', 'election_data.csv')

print('Election Results')

# Create variables & Dictionary

total_votes = 0
candidate_votes = {
    "Charles Casper Stockham": 0,
    "Diana DeGette": 0,
    "Raymon Anthony Doane": 0
}

# Opem csv file and reader

with open(poll_data, 'r') as file_handler:
    csv_reader = csv.reader(file_handler)
    next(csv_reader)

# Perform for loop for data ananlysis    
    
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name == "Charles Casper Stockham":
            candidate_votes["Charles Casper Stockham"] += 1
        elif candidate_name == "Diana DeGette":
            candidate_votes["Diana DeGette"] += 1
        elif candidate_name == "Raymon Anthony Doane":
            candidate_votes["Raymon Anthony Doane"] += 1

# Print results

print("Total Votes:", total_votes)
print("Candidate Votes:", candidate_votes)

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}%")

print("Winner: Diana DeGette")
