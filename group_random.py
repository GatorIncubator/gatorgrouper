""" group using randomization approach """

import copy
import logging
import itertools
from random import shuffle

from group_scoring import *

def group_random(responses, grpsize):
    """ group responses using randomization approach """
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
        for group in groups:
            if outliers:
                group.append(outliers[0])
                outliers = outliers[1:]
            else:
                break
    score_groups(groups, grpsize)
    return groups


def shuffle_students(responses):
    """ Shuffle the responses """
    shuffled_responses = responses[:]
    shuffle(shuffled_responses)
    return shuffled_responses
