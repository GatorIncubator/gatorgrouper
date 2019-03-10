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

    # setup cyclical group target
    indices = list(range(0, numgrps))
    target_group = itertools.cycle(indices)
    priorityColumn = random.randint(1,len(responses[0])-1)
    logging.info("column priority: %d", priorityColumn)

    # iterate through the response column
    for response in responses:
        logging.info("Responses looks like: " + str(responses))
        logging.info("Response looks like: " + str(response))
        if response[priorityColumn] is True:
            logging.info("Value for response at column " + str(priorityColumn) + " is true")
            logging.info("Groups looked like " + str(groups))
            groups[target_group.__next__()].append(response)
            logging.info("Groups now looks like " + str(groups))
            responsesToRemove.append(response)

    responses = [x for x in responses if x not in responsesToRemove]
    logging.info("Responses culled, looks like: " + str(responses))
    # disperse anyone not already grouped
    while responses:
        logging.info("Responses looks like: " + str(responses))
        logging.info("Response looks like: " + str(responses[0]))
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
