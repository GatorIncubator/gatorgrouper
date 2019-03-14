""" Reads CSV data file """

import csv
from pathlib import Path


def read_csv_data(filepath):
    """ Read the responses from the CSV, returning them in a list of lists """

    # handle nonexistant files
    if Path(filepath).is_file() is False:
        print("filenotfound")
        return ""
    # read the raw CSV data
    with open(filepath, "r") as csvfile:
        has_header = csv.Sniffer().has_header(csvfile.read(1024))

    with open(filepath, "r") as csvfile:
        csvdata = list(csv.reader(csvfile))
    # transform into desired output
    responses = list()
    if has_header is True:
        for record in csvdata[1:]:
            temp = list()
            temp.append(record[0].replace('"', ""))
            for value in record[1:]:
                if value.lower() == "true":
                    temp.append(True)
                elif value.lower() == "false":
                    temp.append(False)
                else:
                    temp.append(float(value))
            responses.append(temp)
    else:
        for record in csvdata:
            temp = list()
            temp.append(record[0].replace('"', ""))
            for value in record[1:]:
                if value.lower() == "true":
                    temp.append(True)
                elif value.lower() == "false":
                    temp.append(False)
                else:
                    temp.append(float(value))
            responses.append(temp)
    return responses
