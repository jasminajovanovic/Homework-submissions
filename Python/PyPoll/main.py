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
    outputfile.write("Total votes cast: " + str(total_votes) + "\n")
    print ("Total votes cast: " + str(total_votes))
    outputfile.write("--------------------------\n")
    print ("--------------------------")
    for candidate in candidates_list.keys():
        votes = candidates_list[candidate]
        outputfile.write(candidate + " received " + str(votes) + " (" + "{:.2%}".format(votes/total_votes) + ") votes\n")
        print (candidate + " received " + str(votes) + " (" + "{:.2%}".format(votes/total_votes) + ") votes")
    outputfile.write("--------------------------\n")
    print ("--------------------------")
    outputfile.write("The winner is: " + winner + "\n")
    print ("The winner is: " + winner)
