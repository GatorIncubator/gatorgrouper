""" Reads CSV data file """

import csv

def read_student_file(filepath):
    """ Reads the responses from the CSV file, returning them in a list of lists """

    # read the raw CSV data
    with open(filepath, 'rU') as csvfile:
        csvdata = list(csv.reader(csvfile, delimiter=','))

    # transform into desired output
    responses = list()
    for record in csvdata:
        temp = list()
        temp.append(record[0]) # handle identifiers separately
        for value in record[1:]: # handle string conversions
            if value == "1":
                temp.append("True")
            elif value == "0":
                temp.append("False")
        responses.append(temp)
    return responses
