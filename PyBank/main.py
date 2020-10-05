#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#Initializing values for the results
MonthCount=0
Total=0
PrevMonth=0
AverageChange=0
IncMonth=""
DecMonth=""
GreatestIncrease=0
GreatestDecrease=0


# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        MonthCount+=1
        Total+=int(row[1])
        
        if MonthCount>1:
            Change=int(row[1])-PrevMonth
            AverageChange+=Change
            if Change>GreatestIncrease:
                IncMonth=row[0]
                GreatestIncrease=Change
            if Change<GreatestDecrease:
                DecMonth=row[0]
                GreatestDecrease=Change

        PrevMonth=int(row[1])

AverageChange=round(AverageChange/(MonthCount-1),2)

#Print the results
print("Financial Analysis \n-------------------------")
print(f"Total Months: {MonthCount}")
print(f"Total: ${Total}")
print(f"Average Change: ${AverageChange}")
print(f"Greatest Increase in Profits: {IncMonth} [${GreatestIncrease}]")
print(f"Greatest Decrease in Profits: {DecMonth} [${GreatestDecrease}]")

#Copy Data into a txt file
results=open("PyBank/analysis/results.txt","w")
results.write("Financial Analysis \n-------------------------\n")
results.write(f"Total Months: {MonthCount}\n")
results.write(f"Total: ${Total}\n")
results.write(f"Average Change: ${AverageChange}\n")
results.write(f"Greatest Increase in Profits: {IncMonth} [${GreatestIncrease}]\n")
results.write(f"Greatest Decrease in Profits: {DecMonth} [${GreatestDecrease}]")