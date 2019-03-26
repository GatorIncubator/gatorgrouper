"""Contains all of the group creation algorithms"""

import logging
import random
import itertools
from typing import List, Union
from gatorgrouper.utils import group_scoring


# pylint: disable=bad-continuation
# pylint: disable=dangerous-default-value
def group_random_group_size(
    responses: str, grpsize: int, conflicts=[]
) -> List[List[str]]:
    """
    Calculate number of groups based on desired students per group.
    Conflicts is an optional argument that should list 3-tuples with
    conflict relations between two students in the format:
    (str1, str2, int), where str1 and str2 are students and in is a
    corresponding conflict weight.
    """
    # number of groups = number of students / minimum students per group
    numgrp = int(len(responses) / grpsize)

    return group_random_num_group(responses, numgrp, conflicts)


# pylint: disable=dangerous-default-value
# pylint: disable=too-many-locals
def group_random_num_group(
    responses: str, numgrp: int, conflicts=[]
) -> List[List[str]]:
    """
    Group responses using randomization approach
    Conflicts is an optional argument that should list 3-tuples with
    conflict relations between two students in the format:
    (str1, str2, int), where str1 and str2 are students and in is a
    corresponding conflict weight.
    """
    intensity = 100
    # Intensity is the value that represents the number of attempts made to group
    optimized_groups = list()
    # Optimized Groups holds the groups after scoring maximization
    top_ave = -10000000
    # Top Average is our check to see if the group made is better than the group we have
    while intensity > 0:
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
        # a list of the conflict scores to affect group scores
        conflict_scores = []
        for grp in groups:
            # iterate through groups
            for confs in conflicts:
                # iterate through conflicts given as args
                if (confs[0] in grp) and (confs[1] in grp):
                    # if either name in the 3-tuple is in the group
                    conflict_scores.append(confs[2])
                    # add the conflict to the list of conflict scores
        conf_ave = 0  # assume no conflicts
        if conflict_scores:
            # if there are conflicts, calculate the average
            conf_ave = sum(conflict_scores) / len(conflict_scores)
        # calculates average of the conflict scores
        scores, ave = [], 0
        scores.append(group_scoring.score_group(groups))
        ave = sum(scores) / len(scores)
        logging.info("scores: %d", str(scores))
        logging.info("average: %d", ave)
        intensity -= 1
        # subtract conflict average from general average
        ave = ave - conf_ave
        if ave > top_ave:
            top_ave = ave
            optimized_groups = groups
    return optimized_groups


def shuffle_students(
    responses: Union[str, List[List[Union[str, bool]]]]
) -> List[List[Union[str, bool]]]:
    """ Shuffle the responses """
    shuffled_responses = responses[:]
    random.shuffle(shuffled_responses)
    return shuffled_responses


# group_rrobin.py
def group_rrobin_num_group(responses, numgrps):
    """ group responses using round robin approach """

    # setup target groups
    groups = list()  # // integer div
    responsesToRemove = list()
    logging.info("target groups: %d", numgrps)
    for _ in range(numgrps):
        groups.append(list())

    # choose a random column from the student responses as the priority
    # column to distribute students by
    indices = list(range(0, numgrps))
    random.shuffle(indices)
    target_group = itertools.cycle(indices)
    priorityColumn = random.randint(1, len(responses[0]) - 1)
    logging.info("column priority: %d", priorityColumn)

    # iterate through the responses and check if the priority column is true
    # if it is, add that response to the next group
    for response in responses:
        if response[priorityColumn] is True:
            groups[target_group.__next__()].append(response)
            responsesToRemove.append(response)

    # remove the responses that were already added to a group
    responses = [x for x in responses if x not in responsesToRemove]

    # disperse anyone not already grouped
    while responses:
        groups[target_group.__next__()].append(responses[0])
        responses.remove(responses[0])

    # scoring and return
    scores, ave = [], 0
    scores, ave = group_scoring.calculate_avg(groups)
    logging.info("scores: %s", str(scores))
    logging.info("average: %d", ave)
    return groups
