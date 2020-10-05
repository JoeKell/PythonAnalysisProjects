#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read through each row of data after the header
    for row in csv_reader:


#Copy Data into a txt file
results=open("PyBank/analysis/results.txt","w")
results.write("Financial Analysis \n-------------------------")
results.write("Total Months:")
results.write(f"Total: ${}")
results.write("Average Change:")
results.write(f"Greatest Increase in Profits: {} [${}]")
results.write(f"Greatest Decrease in Profits: {} [${}]")