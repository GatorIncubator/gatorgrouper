""" Test group graph algorithm"""
from networkx import Graph
from gatorgrouper.utils import group_graph
import pytest


def test_recursive_kl():
    """ Test if groups made match recursion """
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
    a = 2
    b = 1
    with pytest.raises(Exception) as excinfo:
        group_graph.compatibility(a, b)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Tuples passed to compatibility() must have same size."


def test_compatibility():
    """ Test compatibility between students """
    a = 2
    b = 2
