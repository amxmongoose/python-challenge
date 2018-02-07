import os
import csv

election_data = ['election_data_1', 'election_data_2']
#Always ask yourself if there is a better way, and then ask the internet!
#In my opinion, csv.DictReader is easier to work with than csv.Reader
for votes_results in election_data:
    #input file name 
    print (votes_results)
    candidate_data = os.path.join('raw_data/' + votes_results + '.csv')
    #output file name
    resultsCSV = os.path.join('output/', + votes_results + '_scrubbed','.csv')
    
    with open(candidate_data, 'r') as f_in, open(resultsCSV, 'w') as f_out:
        d_reader = csv.DictReader(f_in)
        fieldnames=['Total Votes','Candidates','% Total Votes','Votes','Winner']
        d_writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        d_writer.writeheader()
        #save memory! extract, transform, then load
        for record in d_reader:
            record['total Votes'] = int(record['Voter ID'])
            d_writer.writerow(record)
