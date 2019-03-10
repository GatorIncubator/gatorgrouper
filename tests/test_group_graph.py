""" Test group graph algorithm"""
# from gatorgrouper.utils import group_graph
from networkx import Graph
from gatorgrouper.utils import group_graph


def test_recursive_kl():
    """ Test if groups made match recursion"""
    group = [{0, 2}, {4, 7}, {3, 5}, {1, 6}]
    weights = [[0, 0], [0, 0.5], [0.5, 0], [0.75, 0.75], [0.8, 0.1], [0, 1], [1, 0], [1, 1]]
