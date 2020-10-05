#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os
import csv

election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#Initializing values for the results
VoteCount=0
Winner=""
ElectionArray=[]

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        VoteCount+=1


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
for Candidate in ElectionArray:
    results.write(f"{Candidate[0]}: {Candidate[1]}% [{Candidate[2]}]\n")

results.write("-------------------------\n")
results.write(f"Winner: {Winner}\n")
results.write("-------------------------")