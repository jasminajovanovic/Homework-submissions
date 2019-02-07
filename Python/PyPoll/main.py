import os
import csv

input_file = os.path.join('.', "election_data.csv")
output_file = os.path.join('.', "election_output.txt")

candidates_list = {}
maxvotes = 0
winnner = ""

with open (input_file, 'r') as csvfile:
    csvreader = csv.DictReader (csvfile, delimiter =',')
    for row in csvreader:
        candidate = row.get("Candidate")
        if candidate not in candidates_list.keys():
            candidates_list[candidate] = 1
        else:
            candidates_list[candidate] += 1

total_votes = csvreader.line_num -1


for candidate, votes in candidates_list.items():
    if votes > maxvotes:
        maxvotes = votes
        winner = candidate

with open (output_file, "w", newline = '') as outputfile:
    outputfile.write("Election results\n")
    print ("Election Results")
    outputfile.write("--------------------------\n")
    print ("--------------------------")
    outputfile.write(f"Total votes cast: {total_votes} \n")
    print (f"Total votes cast: {total_votes}")
    outputfile.write("--------------------------\n")
    print ("--------------------------")
    for candidate in candidates_list.keys():
        votes = candidates_list[candidate]
        outputfile.write(f"{candidate} received {votes} ({votes/total_votes:.2%}) votes \n")
        print (f"{candidate} received {votes} ({votes/total_votes:.2%}) votes")
    outputfile.write("--------------------------\n")
    print ("--------------------------")
    outputfile.write(f"The winner is: {winner} \n")
    print (f"The winner is: {winner}")
