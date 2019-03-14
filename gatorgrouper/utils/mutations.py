import sys
import random
from typing import List
from gatorgrouper.utils import group_genetic


def swap(grouping):
    # print("MUTATION")
    group_count = len(grouping)
    # print("TOTAL GROUPS: {}".format(group_count))
    # print("BEFORE: {}".format(grouping))
    first, second = random.sample(range(len(grouping)), 2)
    first_index = random.randrange(len(grouping[first]))
    second_index = random.randrange(len(grouping[second]))
    # print("swapping student {} in group {} with student {} in group {}".format(first_index, first, second_index, second))
    temp = grouping[second][second_index]
    grouping[second][second_index] = grouping[first][first_index]
    grouping[second][second_index] = temp
    # grouping[first][first_index], grouping[second][second_index] = grouping[second][second_index], grouping[first][first_index]
    # print("AFTER: {}".format(grouping))

    return grouping


def multi_swap(grouping):
    num_swaps = random.randrange(1, 6)
    for _ in range(num_swaps):
        grouping = swap(grouping)
    return grouping


def get():
    return [swap, multi_swap]
