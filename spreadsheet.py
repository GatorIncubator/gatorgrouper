import csv
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def create_csv():

    file_name = './students.csv'
    logging.info(
        "Authenticating to Google Sheets to obtain Google Form data")
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'authorizationKey/keyFile.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Compsci280 Lab4 Survey Results").sheet1

    # Extract and print all of the values
    list_of_hashes = sheet.get_all_records()

    # Iterates through the list_of_hashes and creates a list of lists with the
    # format ['username', True, False, True]

    logging.info("Creating a list of lists of students")
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
        formated_entry.insert(
            0, formated_entry.pop(
                formated_entry.index(username)))
        formated_list.append(formated_entry)

    logging.info("Writing formatted data to CSV file")
    logging.debug("CSV file name: " + file_name)
    with open(file_name, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in formated_list:
            wr.writerow(item)
