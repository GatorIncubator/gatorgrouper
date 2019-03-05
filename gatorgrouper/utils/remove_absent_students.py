"""Remove missing students from group assignment"""

import logging


def remove_missing_students(absentee_list, list_of_student_lists):
    """Remove missing students before group assignment"""

    logging.info("Removing absent students")
    list_of_student_lists_copy = list_of_student_lists[:]
    for name in absentee_list:
        logging.debug("Removing %s", name)
        for student_list in list_of_student_lists:
            if student_list[0] == name:
                list_of_student_lists_copy.remove(student_list)
    return list_of_student_lists_copy
