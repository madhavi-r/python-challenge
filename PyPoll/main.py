import os
import csv

votes = []
candidates = []
candidate_votes = []
percent_list = []
candidates_dict = {}

electiondatapath = os.path.join('election_data.csv')

with open(electiondatapath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        votes.append(row[2])
        total_votes = len(votes)
        if row[2] not in candidates_dict:
            candidates_dict[row[2]] = 1
        else:
            candidates_dict[row[2]] += 1

    for key, value in candidates_dict.items() :
        candidates.append(key)
        candidate_votes.append(value)

    print("\nElection Results")
    print("_________________________________")
    print(f"Total Votes : {total_votes}")
    print("_________________________________")
    for i in range(0,len(candidate_votes)):
        percentage = format((((candidate_votes[i]/total_votes)*100)),'.3f')
        percent_list.append(percentage)
        print(f"{candidates[i]}: {percent_list[i]} % ({candidate_votes[i]})")
    

    print("_________________________________")
    print(f"Winner: {candidates[candidate_votes.index(max(candidate_votes))]}")
    print("_________________________________")

electionoutput = os.path.join('election.txt')

electionfile = open('election.txt','w+')
    
electionfile.write("\nElection Results") 
electionfile.write("\n______________________________________________")
electionfile.write("\nTotal Votes : " + str(total_votes))
electionfile.write("\n______________________________________________")
electionfile.write("\n" + str(candidates[0]) + ": " + str(percent_list[0]) +"% (" + str(candidate_votes[0]) + ")")
electionfile.write("\n" + str(candidates[1]) + ": " + str(percent_list[1]) +"% (" + str(candidate_votes[1]) + ")")    
electionfile.write("\n" + str(candidates[2]) + ": " + str(percent_list[2]) +"% (" + str(candidate_votes[2]) + ")")
electionfile.write("\n" + str(candidates[3]) + ": " + str(percent_list[3]) +"% (" + str(candidate_votes[3]) + ")")
electionfile.write("\n______________________________________________")
electionfile.write("\nWinner: " + str(candidates[candidate_votes.index(max(candidate_votes))]))
electionfile.write("\n______________________________________________")

electionfile.close()