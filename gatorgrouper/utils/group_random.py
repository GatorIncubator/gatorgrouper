""" group using randomization approach """

import copy
import logging
import itertools
from random import shuffle
from .group_scoring import score_groups


# pylint: disable=bad-continuation
def group_random_group_size(responses: str, grpsize: int) -> List[List[str]]:
    """ Calculate number of groups based on desired students per group """
    # number of groups = number of students / minimum students per group
    numgrp = int(len(responses) / grpsize)

    group_random_num_group(responses, numgrp)


def group_random_num_group(responses, numgrp):
    """ group responses using randomization approach """
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
    scores, ave = score_groups(groups)
    logging.info("scores: %d", scores)
    logging.info("average: %d", ave)
    return groups


def shuffle_students(responses):
    """ Shuffle the responses """
    shuffled_responses = responses[:]
    shuffle(shuffled_responses)
    return shuffled_responses
