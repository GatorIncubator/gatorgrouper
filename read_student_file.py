""" GatorGrouper randomly assigns a list of students to groups """


def read_student_file(students_file_name):
    """ Reads the student identifies from the specific file,
        returning the identifiers in a list """
    with open(students_file_name, 'r') as students_file:
        student_identifers = [line.strip() for line in students_file]
    return student_identifers
