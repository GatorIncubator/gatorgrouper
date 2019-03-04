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
        sniffer = csv.Sniffer()
        has_header = sniffer.has_header(str(csvdata))

    # transform into desired output
    responses = list()
    # with open('students.csv', 'rb') as csvfile:
    #     sniffer = csv.Sniffer()
    #     has_header = sniffer.has_header(csvfile.read(2048))
    #     csvfile.seek(0)
    # handling files not containing headers
    if has_header is True:
        for record in csvdata[1:]:
            temp = list()
            temp.append(record[0].replace('"', ""))
            for value in record[1:]:
                if value == "True":
                    temp.append(True)
                elif value == "False":
                    temp.append(False)
            responses.append(temp)
    else:
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
