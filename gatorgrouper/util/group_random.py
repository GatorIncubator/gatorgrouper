""" Promotes diversity by grouping using randomization approach. """

import copy
import logging
import itertools
import random
import group_scoring


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
