""" group using randomization approach """

import copy
import logging
import itertools
from random import shuffle

from group_scoring import score_groups


def group_random_group_size(responses, grpsize):
    """ group responses using randomization approach """

    # use itertools to chunk the students into groups
    iterable = iter(responses)
    groups = list(iter(lambda: list(itertools.islice(iterable, grpsize)), []))

    # deal with the last, potentially partial group
    last_group_index = len(groups) - 1
    if len(groups[last_group_index]) < grpsize:

        # distribute them throughout the other groups
        logging.info(
            "Partial group identified; distributing across other groups.")
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
    scores, ave = score_groups(groups)
    logging.info("scores: " + str(scores))
    logging.info("average: " + str(ave))
    return groups
    
def group_random_num_groups(responses, numgrp):
    """ group responses using randomization approach """
    # number of students placed into a group
    stunum = 0
    iterable = iter(responses)
    # number of students in each group (without overflow)
    grpsize = int(len(responses) / numgrp)
    groups = list()
    for i in range(0, numgrp):
        group = list()
        while len(group) is not grpsize and stunum < len(responses):
            group.append(next(iterable))
            stunum = stunum + 1
        groups.append(group)
    # deal with the last remaining students
    if len(responses) % stunum is not 0:
        logging.info(
            "Overflow students identified; distributing into groups.")
    for x in range(0, len(responses) % stunum):
        groups[x].append(next(iterable))
        stunum = stunum + 1

    # scoring and return
    scores, ave = [], 0
    scores, ave = score_groups(groups)
    logging.info("scores: " + str(scores))
    logging.info("average: " + str(ave))
    return groups


def shuffle_students(responses):
    """ Shuffle the responses """
    shuffled_responses = responses[:]
    shuffle(shuffled_responses)
    return shuffled_responses
