import os
import csv

election_data_csv = os.path.join("..", "PyPoll", "election_data.csv")

print ("Election Results")
print ("-----------------------------------------")

# This function will RETURN A LIST that contains the UNIQUE VALUES that appeared in the CANDIDATES COLUMN of the CSV
def unique(candidates_list):
    # Initialize a list
    unique_list = []
    x = "Khan"
    # traverse for all elements
    for x in candidates_list:
        # Check if NAME already exists in 'unique_list' OR not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

voters = []
counties = []
listOfCandidates = []

with open(election_data_csv, newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for column in reader:
        voters.append(column[0])
        counties.append(column[1])
        listOfCandidates.append(column[2])


#print ("----------------------------------------- ")
print ("Election Results")
print ("----------------------------------------- ")
totalVotesCast = len(voters)
print("There were a total of", totalVotesCast, "voters.")
print ("----------------------------------------- ")

candidateNames = unique(listOfCandidates)
electionResults = {}
for x in range(0, len(candidateNames)):
    nameOfCandidate = candidateNames[x]
    numVotesForCandidate = listOfCandidates.count(nameOfCandidate)
    proportionOfVoteWon = round(100*numVotesForCandidate/totalVotesCast, 2)

    print(nameOfCandidate, "had", numVotesForCandidate, "votes (won", proportionOfVoteWon, "% of all votes cast).")


    electionResults[nameOfCandidate] = numVotesForCandidate

# This line will find the DICTIONARY KEY that corresponds to the LARGEST VALUE in the DICTIONARY
print ("----------------------------------------- ")
print(max(electionResults, key=electionResults.get), "won the POPULAR VOTE")
print ("----------------------------------------- ")

