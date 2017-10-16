""" group using round robin approach"""

import logging
from random import shuffle
from itertools import cycle
from group_scoring import score_groups


def group_rrobin(responses, grpsize):
    """ group responses using round robin approach """

    # setup target groups
    groups = list() # // integer div
    numgrps = len(responses) // grpsize
    logging.info("target groups: " + str(numgrps))
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
    logging.info("column priority: " + str(columns))

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
    logging.info("scores: " + str(scores))
    logging.info("average: " + str(ave))
    return groups
