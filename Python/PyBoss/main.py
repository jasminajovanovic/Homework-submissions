
import csv
import os

file1_path = os.path.join('.', "employee_data.csv")
output_file = os.path.join('.', "outputfile.csv")

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

def print_ssn(ssn):
    hidden_ssn="***-**-"
    for i in range(7, 11):
        hidden_ssn=hidden_ssn+ssn[i]
    return hidden_ssn

def reformat_dob(dob):
    new_dob = ""
    year, month, day = dob.split("-")
    new_dob=month+'/'+day+'/'+year 
    return new_dob
    
with open(file1_path, 'r') as file1:
    csvreader1 = csv.DictReader(file1)
    # list comprehension to create a list with new format
    new_list = [
        (row['Emp ID'], row['Name'].split(" ")[0],row['Name'].split(" ")[1], reformat_dob(row['DOB']), print_ssn(row['SSN']), us_state_abbrev[row['State']])
        for row in csvreader1
    ]

# write new format to csv file
with open(output_file, "w", newline='') as outfile:
    csvwriter = csv.writer(outfile, delimiter=",")
    for row in new_list:
        csvwriter.writerow(row)
    


