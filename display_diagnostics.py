""" GatorGrouper randomly assigns a list of students to groups """


def display_diagnostics(student_identifers, student_groups):
    """ Display information about what was generated """
    print("Successfully placed",
          len(student_identifers), "students into",
          len(student_groups), "groups")
    print()
