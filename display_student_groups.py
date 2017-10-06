""" GatorGrouper randomly assigns a list of students to groups """


def display_student_groups(student_groups):
    """ Display the student groups with labels """
    group_counter = 1
    for student_group in student_groups:
        print("Group", group_counter)
        for next in student_group:
            print(next)
        print()
        group_counter = group_counter + 1
