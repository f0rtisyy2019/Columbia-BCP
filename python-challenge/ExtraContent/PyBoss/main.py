import os
import csv
from datetime import datetime

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

employeeCSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'employee_data.csv')
employeeCSV2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'employee_data2.csv')
with open(employeeCSV, 'r') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=',')
    header = next(csvreader1)
    with open(employeeCSV2, 'w', newline='') as csvfile2:
        csvwriter2 = csv.writer(csvfile2, delimiter=',')
        csvwriter2.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        for row in csvreader1:
            list = []
            list.append(row[0])
            name = row[1].split(' ')
            list.append(name[0])
            list.append(name[1])
            newDob = datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')
            list.append(newDob)
            list.append("***-**-" + row[3][-4:])

            for state, st in us_state_abbrev.items():
                if state == row[4]:
                    list.append(st)
                    break
            csvwriter2.writerow(list)