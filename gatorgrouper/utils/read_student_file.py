""" Reads CSV data file """

import csv


def read_student_file(filepath):
    """ Read the responses from the CSV, returning them in a list of lists """

    csvdata = list()
    try:
        # read the raw CSV data
        with open(filepath, "r") as csvfile:
            csvdata = list(csv.reader(csvfile, delimiter=","))
    except IOError:
        print("File Not Found!")

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
