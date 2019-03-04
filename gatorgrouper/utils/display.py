""" Various display functions """

import logging


def display_student_groups(student_groups):
    """ Display the student groups with labels """
    group_counter = 1
    place_counter = 0
    for student_group in student_groups:
        # print("Group", group_counter)
        print("\033[0;32m" + "\033[1m" + "\033[4m" + "Group", group_counter)
        for student in student_group:
            place_counter += 1
            # print(student[0])
            print("\033[0m" + student[0])  # converts the students back to original font
        print()
        group_counter = group_counter + 1
    logging.info("Found %d students", place_counter)


def display_welcome_message():
    """ Display a welcome message """
    print()
    print("GatorGrouper: Automatically Assign Students to Groups")
    print("https://github.com/GatorEducator/gatorgrouper")
    print()


def create_escaped_string_from_list(student_identifers):
    """ Return a string that lists the student identifiers """
    student_list = ""
    for student in student_identifers:
        student_list = student_list + str(student) + "\n"
    return student_list
