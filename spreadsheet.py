import gspread
import csv
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Compsci280 Lab4 Survey Results").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

# Iterates through the list_of_hashes and creates a list of lists with the
#format ['username', True, False, True]


formated_list = list()
for entry in list_of_hashes:
    formated_entry = list()
    for question, response in entry.items():
        if question == 'Email Address':
            email = entry[question].partition('@')
            username = email[0]
            formated_entry.append(username)
        elif response == 'Yes':
            formated_entry.append(True)
        elif response == 'No':
            formated_entry.append(False)
    formated_entry.insert(0, formated_entry.pop(formated_entry.index(username)))
    formated_list.append(formated_entry)

with open('./data.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for item in formated_list:
        wr.writerow(item)

sheet.export(format='csv')
#https://gspread.readthedocs.io/en/latest/ for figuring out how to make csv.
