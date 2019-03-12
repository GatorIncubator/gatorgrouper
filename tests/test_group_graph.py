""" Test group graph algorithm"""
from networkx import Graph
import pytest
from gatorgrouper.utils import group_graph


def test_recursive_kl():
    """ Test if groups made match recursion from Kernighan-Lin algorithm """
    G = Graph()
    with pytest.raises(ValueError) as excinfo:
        group_graph.recursive_kl(G, numgrp=1)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "numgrp must be a power of 2 and at least 2."


# Need to parametrize test_total_cut_size because it would, but should not, handle
# groups of 1
def test_total_cut_size():
    """ Test if cut size of subsets in partition match """
    G = Graph()
    G.add_edges_from([(1, 4), (2, 3)])
    partition = [(1, 2), (3, 4)]
    output = group_graph.total_cut_size(G, partition)
    expected_output = 2
    assert output == expected_output


def test_compatibility_length():
    """ Test if exception message is raised by unequal students scores """
    a = (1.0, "python")
    b = (2.0, "java")
    with pytest.raises(Exception) as excinfo:
        group_graph.compatibility(a, b)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Tuples passed to compatibility() must have same size."

# Run objective_weights test case using None

def test_compatibility_objective_weights():
    """ Test if objective_weights is empty """
    a = [1, 1]
    b = [0, 0.5]
    objective_weights = (2.0, 1.0)
    output = group_graph.compatibility(a, b, objective_weights)
    expected_output = 1.75
    assert output == expected_output


def test_compatibility_objective_measures():
    """ Test if objective measures  """
    a = [0, 1]
    b = [0.75, 0.75]
    objective_measures = ("avg", "match")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 0.375
    assert output == expected_output


# def test_compatibility_measure():
#     """ Test compatibility between students """
#     a_score = 2
#     b_score = 2
#     output = group_graph.compatibility(a_score, b_score)
#     expected_output = something #whatever measure is called
#     assert output == expected_output
#
# # Need test cases for every branch of compatibility function
#
#
# def
def test_group_graph_partition():
    """ Tests that the output of the group_graph_partition is correct """
    students = [
        ["one", 0, 0],
        ["two", 0, 0.5],
        ["three", 0.5, 0],
        ["four", 0.75, 0.75],
        ["five", 0.8, 0.1],
        ["six", 0, 1],
        ["seven", 1, 0],
        ["eight", 1, 1],
    ]
    assert group_graph.group_graph_partition(students, 4)
