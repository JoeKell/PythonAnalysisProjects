#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os
import csv

#The file the code reads from
HR_csv = os.path.join("PyBoss", "Resources", "employee_data.csv")

#The file the code writes to
results=open("PyBoss/output/new_employee_data.csv","w")
results.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")


#Imported from https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open and read csv
with open(HR_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #Skip the header
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        #Gather all of the old data
        EmpID=row[0]
        Name=row[1].split(" ")
        DOB=row[2].split("-")
        SSN=row[3].split("-")
        State=row[4]

        #Write the data results.write
        #results.write("214,Sarah,Simpson,12/04/1985,***-**-8166,FL\n")
        results.write(f"{EmpID},")
        results.write(f"{Name[0]},")
        results.write(f"{Name[1]},")
        results.write(f"{DOB[1]}/{DOB[2]}/{DOB[0]},")
        results.write(f"***-**-{SSN[2]},")
        results.write(f"{us_state_abbrev[State]}\n")

