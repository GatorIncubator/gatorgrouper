""" group using round robin approach"""

import logging
import random
import itertools
from gatorgrouper.utils import group_scoring


def group_rrobin_group_size(responses, grpsize):
    """ group responses using round robin approach """

    # setup target groups
    groups = list()  # // integer div
    responsesToRemove = list()
    numgrps = len(responses) // grpsize
    logging.info("target groups: %d", numgrps)
    for _ in range(numgrps):
        groups.append(list())

    # choose a random column from the student responses as the priority
    # column to distribute students by
    indices = list(range(0, numgrps))
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
    scores, ave = group_scoring.score_groups(groups)
    logging.info("scores: %s", scores)
    logging.info("average: %s", ave)
    return groups


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
    target_group = itertools.cycle(indices)
    priorityColumn = random.randint(1, len(responses[0]) - 1)
    logging.info("column priority: %d", priorityColumn)

    # iterate through the responses and check if the priority column is true
    # if it is, add that response to the next group
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
    scores, ave = group_scoring.score_groups(groups)
    logging.info("scores: %s", scores)
    logging.info("average: %s", ave)
    return groups
