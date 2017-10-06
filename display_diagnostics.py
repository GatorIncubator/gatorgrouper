""" Display information about what was generated """


def display_diagnostics(student_identifers, student_groups):
    print("Successfully placed",
          len(student_identifers), "students into",
          len(student_groups), "groups")
    print()
