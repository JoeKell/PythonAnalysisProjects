#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os
import csv
from decimal import *
getcontext().prec = 4

election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#Initializing values for the results
VoteCount=0
Winner=""
CandidateArray=[]
TallyArray=[]
PercentArray=[]

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        VoteCount+=1
        if row[2] in CandidateArray:
            TallyArray[CandidateArray.index(row[2])]+=1
        else:
            CandidateArray.append(row[2])
            TallyArray.append(1)

#Assign percents
for Tally in TallyArray:
    PercentArray.append('%.3f'%((Tally*100)/VoteCount))   

#Find the Winner
Winner=CandidateArray[TallyArray.index(max(TallyArray))]

#Print the results
# print("Financial Analysis \n-------------------------")
# print(f"Total Months: {MonthCount}")
# print(f"Total: ${Total}")
# print(f"Average Change: ${AverageChange}")
# print(f"Greatest Increase in Profits: {IncMonth} [${GreatestIncrease}]")
# print(f"Greatest Decrease in Profits: {DecMonth} [${GreatestDecrease}]")

#Copy Data into a txt file
results=open("PyPoll/analysis/results.txt","w")
results.write("Election Results \n-------------------------\n")
results.write(f"Total Votes: {VoteCount}\n-------------------------\n")
for i in range(len(CandidateArray)):
    results.write(f"{CandidateArray[i]}: {PercentArray[i]}% [{TallyArray[i]}]\n")
results.write("-------------------------\n")
results.write(f"Winner: {Winner}\n")
results.write("-------------------------")