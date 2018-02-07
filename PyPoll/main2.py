import os
import csv
from collections import defaultdict
from collections import Counter

election_data = ["election_data_1", "election_data_2"]

for voter_results in election_data:
    election_dataCSV = os.path.join('raw_data/' + voter_results + '.csv')
    election_resultsCSV = os.path.join('output/' + voter_results + '.csv')

    with open(election_dataCSV, 'r') as f_in, open(election_resultsCSV, 'w') as f_out:
        
        d_reader = csv.DictReader(f_in)
        fieldnames = ('Voter ID', 'County', 'Candidate')
        d_writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        d_writer.writeheader()
        #for row in d_reader
        #c = Counter.(d_reader)
        #print(c)
        for record in d_reader:
            record['Voter ID']=int(record['Voter ID'])
            d_writer.writerow(record)

        next (f_in,None)

    with open(election_dataCSV, 'r') as csvFile:

        total_votes = 0
        total_votes = sum(1 for row in csvFile)
        candidaterow = 0
        next(csvFile,None)
        print(total_votes)

        #for row in csvFile:
            #candidaterow = [i for candidates in row(0)]
        print(candidaterow)
        #for candiaterow in csvReader:
            # Append data from the row
            #candidates.append(candiaterow[2])
           # print(candidates)
           # votes.append(row[0])
            # Calculate percentages and append to the list
            #winPercent.append(int(row[1])/(int(row[1]) + int(row[2]) + int(row[3]))*100)
            #lossPercent.append(int(row[2])/(int(row[1]) + int(row[2]) + int(row[3]))*100)
            #drawPercent.append(int(row[3])/(int(row[1]) + int(row[2]) + int(row[3]))*100)
    # Zip lists together
    #election_dataCSV = str(candidates)
    #print(candidates)
    #with open(election_resultsCSV, 'w', newline="") as csvFile:
        #csvWriter = csv.writer(csvFile, delimiter=',')
        # Write Headers into file
        #csvWriter.writerow(["Candiate","Votes","Vote Percentage",""])
        # Write the zipped lists to a csv
        #csvWriter.writerows(election_resultsCSV)
Total = str(total_votes)
print("Election Results")
print("-"*80)
print("Total Votes:" + Total)
print("-"*80)
#print str([candidates,vote_percentage,Votes])
print("-"*80)
#print(winner)
print("-"*80)