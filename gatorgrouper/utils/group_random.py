""" Promotes diversity by grouping using randomization approach. """

import copy
import logging
import itertools
import random
from typing import List, Union
from gatorgrouper.utils import group_scoring


# pylint: disable=bad-continuation
def group_random_group_size(responses: str, grpsize: int) -> List[List[str]]:
    """ Calculate number of groups based on desired students per group """
    # number of groups = number of students / minimum students per group
    numgrp = int(len(responses) / grpsize)

    # run number of groups through group_random_num_group
    group_random_num_group(responses, numgrp)


def group_random_num_group(responses: str, numgrp: int) -> List[List[str]]:
    """ group responses using randomization approach """

    #TODO: store-optimal option from multiple iterations

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

    #TODO: calculate conflict scores

    scores, ave = [], 0
    scores, ave = group_scoring.score_groups(groups)
    logging.info("scores: %d", scores)
    logging.info("average: %d", ave)
    return groups


# pylint: disable=bad-continuation
def shuffle_students(
    responses: Union[str, List[List[Union[str, bool]]]]
) -> List[List[Union[str, bool]]]:
    """ Shuffle the responses """
    shuffled_responses = responses[:]
    random.shuffle(shuffled_responses)
    return shuffled_responses
