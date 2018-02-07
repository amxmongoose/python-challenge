import csv
import os
from collections import defaultdict
from collections import Counter


election_data = ["election_data_1", "election_data_2"]

for voter_results in election_data:

    election_dataCSV = os.path.join('raw_data/' + voter_results + '.csv')

    election_resultsCSV = os.path.join('output/' + voter_results + '.csv')

    candidate = []
    total_votes = []
    votes = []
    #vote_Percent = []
    total_votes = 0

    with open(election_dataCSV, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        next(csvReader, None)
            
        for row in csvReader:
            candidate = (row(2))
            candidate.append(row[2])
            votes.append(row[0])
            total_votes = sum(1 for row in csvFile))
            
            print(total_votes)
            #vote_Percent = 0

            # Calculate percentages and append to the list
            #vote_Percent.append(int(votes)/(total_votes)*100)

        # Zip lists together
        cleanCSV = zip(candidate,votes)

    with open(election_resultsCSV, 'w', newline="") as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(["Candidate","Votes","Vote Percentage","Total Votes"])

        # Write the zipped lists to a csv
        csvWriter.writerows(cleanCSV)
        
