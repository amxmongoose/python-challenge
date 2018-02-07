import csv
import os
from collections import defaultdict
from collections import Counter


election_data = ["election_data_1", "election_data_2"]

for voter_results in election_data:

    file = os.path.join('raw_data/' + voter_results + '.csv')

    candidates = []
    total_votes = []
    votes = []
    vote_Percent = []

    with open(file, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        next(csvReader, None)
            
        for row in csvReader:
            candidates.append(row[0])
            votes.append(int(row[0]))

    total_votes = len(votes)

    vote_Percent = vote[0]
        
    for v in range(len(candidates)):
        votes = votes[r]
        vote_Percent = votes[r]/total_votes*100
        
        output = os.path.join('output/' + str(election_data) + '.csv'))
        
    # Zip lists together
    electionresults = zip(candidate,votes,vote_Percent)

    with open(output, 'w') as writefile:

        writefile.writelines('Election Results\n')
        writefile.writelines('-'*40 + '\n')
        writefile.writelines('Total Vote ' + str(total_votes) + '\n')
        writefile.writelines('candidates: ' + str(candidates) + '\n')
        writefile.writelines('Votes: ' + int(votes) + '\n')
        writefile.writelines('Vote Percentage: ' + int(vote_Percent) + '\n')
        
        
