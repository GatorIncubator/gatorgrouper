"""Integrate GatorGrouper with Google Sheets."""

import csv
import math
import logging
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from gatorgrouper.utils import group_genetic
from gatorgrouper.utils import constants


EMAIL_COL = None
PREFERENCES_COL = None
SKILLS_COLS = set()

STUDENTS = None
GROUPING_SIZE = None

def get(group_size):
    """Retrieve data from Google Sheets and write to a CSV file."""

    global EMAIL_COL
    global PREFERENCES_COL
    global SKILLS_COLS

    # formatted_records = list()
    # for entry in records:
    #     formatted_entry = list()
    #     for index, (question, response) in enumerate(entry.items()):
    #         if question == 'Email Address':
    #             EMAIL_COL = index - 1  # subtracting one because timestamp column not collected
    #             formatted_entry.append(response)
    #         elif "prefer" in question:
    #             PREFERENCES_COL = index - 1
    #             formatted_entry.append(response)
    #         elif "skill" in question:
    #             SKILLS_COLS.add(index - 1)
    #             formatted_entry.append(response)
    #     formatted_records.append(formatted_entry)

    global STUDENTS
    global GROUPING_SIZE

    # EMAIL_COL = 0
    # PREFERENCES_COL = 1
    # SKILLS_COLS = [2, 3, 4, 5, 6]

    DATA = pd.read_csv(constants.WORKBOOK_CSV, header=None)

    EMAILS = DATA.iloc[:, EMAIL_COL]

    STUDENTS = list()
    for current_row, email in enumerate(EMAILS):
        skills = list()
        for skill_col in SKILLS_COLS:
            skills.append(DATA.iat[current_row, skill_col])
        preferences_str = DATA.iat[current_row, PREFERENCES_COL]

        if isinstance(preferences_str, float) and math.isnan(preferences_str):
            preferences = []
        else:
            preferences = preferences_str.replace(" ", "").split(",")

        STUDENTS.append(Student(email, skills, preferences))

    # for student in STUDENTS:
    #     print(str(student) + "\n")

    GROUPING_SIZE = math.floor(len(STUDENTS) / group_size)
