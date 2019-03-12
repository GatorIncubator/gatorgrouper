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


def test_compatibility_objective_weights():
    """ Test if objective_weights returns the objective weights of students """
    a = [1, 1]
    b = [0, 0.5]
    objective_weights = (2.0, 1.0)
    output = group_graph.compatibility(a, b, objective_weights)
    expected_output = 1.75
    assert output == expected_output


def test_compatibility_objective_measures():
    """ Test if objective_measures returns the objective measure of students """
    a = [0, 1]
    b = [0.75, 0.75]
    objective_measures = ("avg", "match")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 0.375
    assert output == expected_output


def test_compatability_measure_average():
    """ Test if measure of different student scores return an average """
    a = [1, 1]
    b = [0, 1]
    output = group_graph.compatibility(a, b)
    expected_output = 1.5
    assert output == expected_output


def test_compatability_measure_max():
    """ Test if measure of different student scores return a maximum """
    a = [1, 0]
    b = [0, 0.5]
    objective_measures = ("max", "max")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 1.5
    assert output == expected_output


def test_compatability_measure_min():
    """ Test if measure of different student scores return a minimum """
    a = [1, 0]
    b = [0, 0.5]
    objective_measures = ("min", "min")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 0
    assert output == expected_output


def test_compatability_measure_int():
    """ Test if measure of different student scores are both equal """
    a = [1, 0]
    b = [0, 0.5]
    objective_measures = ("match", "match")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 0
    assert output == expected_output


def test_compatability_measure_diff():
    """ Test if measure of different student scores returns an absolute value difference """
    a = [1, 0]
    b = [0, 0.5]
    objective_measures = ("diff", "diff")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 1.5
    assert output == expected_output


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
