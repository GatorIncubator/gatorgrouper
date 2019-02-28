""" Reads CSV data file """

import csv
from pathlib import Path


def read_student_file(filepath):
    """ Read the responses from the CSV, returning them in a list of lists """

    # handle nonexistant files
    if Path(filepath).is_file() is False:
        return "filenotfound"

    # read the raw CSV data
    with open(filepath, "r") as csvfile:
        csvdata = list(csv.reader(csvfile, delimiter=","))

    # transform into desired output
    responses = list()
    for record in csvdata[1:]:
        temp = list()
        temp.append(record[0].replace('"', ""))
        for value in record[1:]:
            if value == "True":
                temp.append(True)
            elif value == "False":
                temp.append(False)
        responses.append(temp)
    return responses
