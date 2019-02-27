""" Reads CSV data file """

import csv
from pathlib import Path


def read_student_file(filepath):
    """ Read the responses from the CSV, returning them in a list of lists """

    # handle nonexistant files
    # if Path(filepath).is_file() is False:
    #     return "filenotfound"
try:
    f = open(fname, 'rb') 
except IOError:
    print ("Could not read file:", fname)
    sys.exit()

with f:
    reader = csv.reader(f)
    for row in reader:
        pass #do stuff here

    # read the raw CSV data
    with open(filepath, "rU") as csvfile:
        csvdata = list(csv.reader(csvfile, delimiter=","))

    # transform into desired output
    responses = list()
    for record in csvdata:
        temp = list()
        temp.append(record[0].replace('"', ""))
        for value in record[1:]:
            if value == "True":
                temp.append(True)
            elif value == "False":
                temp.append(False)
        responses.append(temp)
    return responses
