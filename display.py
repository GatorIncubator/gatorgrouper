""" Various display functions """


def display_student_groups(student_groups):
    """ Display the student groups with labels """
    group_counter = 1
    for student_group in student_groups:
        print("Group", group_counter)
        for student in student_group:
            print(student)
        print()
        group_counter = group_counter + 1


def display_welcome_message():
    """ Display a welcome message """
    print()
    print("GatorGrouper: Automatically Assign Students to Groups")
    print("https://github.com/gkapfham/gatorgrouper")
    print()


def create_escaped_string_from_list(student_identifers):
    """ Return a string that lists the student identifiers """
    student_list = ""
    for student in student_identifers:
        student_list = student_list + student + "\n"
    return student_list
