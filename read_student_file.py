""" GatorGrouper randomly assigns a list of students to groups """
from random import shuffle
import argparse
import itertools
import sys
import xlrd


def read_student_file():
    """Reads the student identifies from the specific file,
       returning the identifiers in a list"""

    workbook = xlrd.open_workbook('categories.xlsx')
    sheet = workbook.sheet_by_name('Form Responses 1')
    data = [[sheet.cell_value(r, c) for c in range(1, sheet.ncols)] for r in range(1, sheet.nrows)]

    # initializing an empty list called student_identifiers which will be returned by the function
    student_identifiers = list()

    # iterate through each line in "data" where each line represents the information submitted by each student
    for line in data:
        # create an empty list named temp for each student's information
        temp = list()

        # now iterate through all of the elements contained in each line from the data set
        # if the element was 'Yes' then it will be replaced with True and appended to the temp list
        # if the element was 'No' then it will be replaced with False and appended to the temp list
        # if the element was not 'Yes' or 'No' then append the element to the temp list. This is
        # how the student's name gets added to the list
        for word in line:
            if word == 'Yes':
                temp.append(True)
            elif word == 'No':
                temp.append(False)
            else:
                temp.append(word)

        # add all of the modified student information to the student_identifiers
        student_identifiers.append(temp)

    # The following lines can be uncommented to print out the student_identifiers with one
    # students information on each line
    #for i in range(0, len(student_identifiers)):
        #print(student_identifiers[i])

    return student_identifiers
