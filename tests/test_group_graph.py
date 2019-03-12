""" Test group graph algorithm"""
from gatorgrouper.utils import group_graph
from networkx import Graph
import pytest


def test_recursive_kl():
    """ Test if groups made match recursion """
    # weights = [[0, 0], [0, 0.5], [0.5, 0], [0.75, 0.75], [0.8, 0.1], [0, 1], [1, 0], [1, 1]]
    # vertex_weight_pairs = enumerate([{"weight": w} for w in weights])
    G = Graph()
    with pytest.raises(ValueError) as excinfo:
        group_graph.recursive_kl(G,numgrp=1)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "numgrp must be a power of 2 and at least 2."


    # G = Graph()
    # G.add_nodes_from(vertex_weight_pairs)
    # groups = []
    # for i in kernighan_lin_bisection(G):
    #     subgraph = G.subgraph(subset)
    #     groups.extend(recursive_kl(subgraph, numgrp=next_numgrp))
    # assert i in groups is True

# Need to parametrize test_total_cut_size because it would, but should not, handle
# groups of 1

def test_total_cut_size():
    """ Test if cut size of subsets in partition match """
    G = Graph()
    G.add_edges_from([(1, 4), (2, 3)])
    partition = ([(1, 2), (3, 4)])
    output = group_graph.total_cut_size(G, partition)
    expected_output = 2
    assert output == expected_output


def test_compatibility_length():
    """ Test if compatibility score equates to summ of scaled scores """
    a = (2)
    b = (1)
    with pytest.raises(Exception) as excinfo:
        group_graph.compatibility(a, b)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Tuples passed to compatibility() must have same size."


# def test_main():
#     students = [
#         ["one", 0, 0],
#         ["two", 0, 0.5],
#         ["three", 0.5, 0],
#         ["four", 0.75, 0.75],
#         ["five", 0.8, 0.1],
#         ["six", 0, 1],
#         ["seven", 1, 0],
#         ["eight", 1, 1],
#     ]
#     group = []
#     weights = [[0, 0], [0, 0.5], [0.5, 0], [0.75, 0.75], [0.8, 0.1], [0, 1], [1, 0], [1, 1]]
#     output = group_graph.group_graph_partition(students[1:])
#     # assert output == None
#     # set(group) == set(students)
#     # for item in output:
#     #     group += item
#     # assert group == students
#
#     if set(group) == set(students):
#         check = all(elem == group[0] for elem in group)
#         assert check == True
#         assert group == students
#
#
# def test_main():
# students = [
#     ["one", 0, 0],
#     ["two", 0, 0.5],
#     ["three", 0.5, 0],
#     ["four", 0.75, 0.75],
#     ["five", 0.8, 0.1],
#     ["six", 0, 1],
#     ["seven", 1, 0],
#     ["eight", 1, 1],
# ]
# weights = [
#     [0, 0],
#     [0, 0.5],
#     [0.5, 0],
#     [0.75, 0.75],
#     [0.8, 0.1],
#     [0, 1],
#     [1, 0],
#     [1, 1],
# ]
# groups = group_graph.group_graph_partition(students, 4)
# assert weights in groups
