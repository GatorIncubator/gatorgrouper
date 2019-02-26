""" group using round robin approach"""

import logging
from random import shuffle
from itertools import cycle
from .group_scoring import score_groups


def group_rrobin_group_size(responses, grpsize):
    """ group responses using round robin approach """

    # setup target groups
    groups = list()  # // integer div
    numgrps = len(responses) // grpsize
    logging.info("target groups: %d", numgrps)
    for _ in range(numgrps):
        groups.append(list())

    # setup cyclical group target
    indices = list(range(0, numgrps))
    target_group = cycle(indices)

    # randomize the order in which the columns will be drained
    columns = list()
    for col in range(1, len(responses[0])):
        columns.append(col)
    shuffle(columns)
    logging.info("column priority: %d", columns)

    # iterate through the response columns
    for col in columns:
        for response in responses:
            if response[col] is True:
                groups[target_group.__next__()].append(response)
                responses.remove(response)

    # disperse anyone not already grouped
    while responses:
        groups[target_group.__next__()].append(responses[0])
        responses.remove(responses[0])

    # scoring and return
    scores, ave = [], 0
    scores, ave = score_groups(groups)
    logging.info("scores: %d", scores)
    logging.info("average: %d", ave)
    return groups


def group_rrobin_num_group(responses, numgrps):
    """ group responses using round robin approach """

    # setup target groups
    groups = list()  # // integer div
    logging.info("target groups: %d", numgrps)
    for _ in range(numgrps):
        groups.append(list())

    # setup cyclical group target
    indices = list(range(0, numgrps))
    target_group = cycle(indices)

    # randomize the order in which the columns will be drained
    columns = list()
    for col in range(1, len(responses[0])):
        columns.append(col)
    shuffle(columns)
    logging.info("column priority: %d", columns)

    # iterate through the response columns
    for col in columns:
        for response in responses:
            if response[col] is True:
                groups[target_group.__next__()].append(response)
                responses.remove(response)

    # disperse anyone not already grouped
    while responses:
        groups[target_group.__next__()].append(responses[0])
        responses.remove(responses[0])

    # scoring and return
    scores, ave = [], 0
    scores, ave = score_groups(groups)
    logging.info("scores: %d", scores)
    logging.info("average: %d", ave)
    return groups

def conflict_sorting(conflicts, severity, students):
    """ sort through student conflicts by severity """

    #setup groups for sorting
    student_conflicts = list()
    for _ in range(students):
        student_conflicts.append(list())

    #populate the lists in student_conflicts to contain all the imported information
    for i in range(student_conflicts):
        student_conflicts.insert(i, (severity, conflicts, students))

    #sort the student conflicts by severity
    student_conflicts.sort(key=lambda reverse=True)

    return student_conflicts
