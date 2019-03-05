"""Contains all of the gorup creation algorithms"""

import copy
import logging
import itertools
import random
import group_scoring


# group_random.py
def group_random_group_size(responses, grpsize):
    """
    Forms equally sized groups based on desired group size using randomization
    approach.
    """

    # use itertools to chunk the students into groups
    iterable = iter(responses)
    groups = list(iter(lambda: list(itertools.islice(iterable, grpsize)), []))

    # deal with the last, potentially partial group
    last_group_index = len(groups) - 1
    if len(groups[last_group_index]) < grpsize:

        # distribute them throughout the other groups
        logging.info("Partial group identified; distributing across other groups.")
        lastgroup = groups[last_group_index]
        outliers = copy.deepcopy(lastgroup)
        groups.remove(lastgroup)
        while outliers:
            for group in groups:
                if outliers:
                    group.append(outliers[0])
                    outliers = outliers[1:]
                else:
                    break

    # scoring and return
    scores, ave = [], 0
    scores, ave = group_scoring.score_groups(groups)
    logging.info("scores: %d", scores)
    logging.info("average: %d", ave)
    return groups


def group_random_num_group(responses, numgrp):
    """
    Forms equally sized groups based on the desired number of groups using
    randomization approach.
    """
    # number of students placed into a group
    stunum = 0
    iterable = iter(responses)
    # number of students in each group (without overflow)
    grpsize = int(len(responses) / numgrp)
    groups = list()
    for _ in range(0, numgrp):
        group = list()
        while len(group) is not grpsize and stunum < len(responses):
            group.append(next(iterable))
            stunum = stunum + 1
        groups.append(group)
    # deal with the last remaining students
    if len(responses) % stunum != 0:
        logging.info("Overflow students identified; distributing into groups.")
    for _x in range(0, len(responses) % stunum):
        groups[_x].append(next(iterable))
        stunum = stunum + 1

    # scoring and return
    scores, ave = [], 0
    scores, ave = group_scoring.score_groups(groups)
    logging.info("scores: %d", scores)
    logging.info("average: %d", ave)
    return groups


def shuffle_students(responses):
    """ Shuffle the responses """
    shuffled_responses = responses[:]
    random.shuffle(shuffled_responses)
    return shuffled_responses


# group_rrobin.py
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
    target_group = itertools.cycle(indices)

    # randomize the order in which the columns will be drained
    columns = list()
    for col in range(1, len(responses[0])):
        columns.append(col)
    random.shuffle(columns)
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
    scores, ave = group_scoring.score_groups(groups)
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
    target_group = itertools.cycle(indices)

    # randomize the order in which the columns will be drained
    columns = list()
    for col in range(1, len(responses[0])):
        columns.append(col)
    random.shuffle(columns)
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
    scores, ave = group_scoring.score_groups(groups)
    logging.info("scores: %d", scores)
    logging.info("average: %d", ave)
    return groups
