""" Test group graph algorithm"""
import itertools
from networkx import Graph
import pytest
from gatorgrouper.utils import group_graph


def test_recursive_kl_error():
    """ Test if ValueError is called if numgrp is not a power of 2 and not at least 2 """
    G = Graph()
    with pytest.raises(ValueError) as excinfo:
        group_graph.recursive_kl(G, numgrp=1)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "numgrp must be a power of 2 and at least 2."


def test_recursive_kl_two():
    """ Test if recursive Kernighan-Lin algorithm returns two groups recursively """
    G = Graph()
    student1 = (1, 4)
    student2 = (2, 3)
    G.add_edge(student1, student2)
    actual_output = group_graph.recursive_kl(G, 2)

    assert actual_output in ([{student2}, {student1}], [{student1}, {student2}])


def test_recursive_kl_multi():
    """ Test if recursive Kernighan-Lin algorithm returns more than two groups """
    G = Graph()
    student1 = (1, 4)
    student2 = (2, 3)
    student3 = (5, 7)
    student4 = (6, 8)
    students = [student1, student2, student3, student4]
    group_list = list(itertools.combinations(students, 2))
    G.add_edges_from(group_list)
    actual_output = group_graph.recursive_kl(G, 2)
    assert len(actual_output) == 2
    assert len(actual_output[0]) == 2
    assert len(actual_output[1]) == 2


def test_total_cut_size():
    """ Test if cut size of subsets in partition match """
    G = Graph()
    G.add_edges_from([(1, 4), (2, 3)])
    partition = [(1, 2), (3, 4)]
    output = group_graph.total_cut_size(G, partition)
    expected_output = 2
    assert output == expected_output


def test_compatibility_length():
    """ Test if exception message is raised by unequal students' scores """
    a = tuple([1.0])
    b = tuple([2.0, 0.5])
    with pytest.raises(Exception) as excinfo:
        group_graph.compatibility(a, b)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Tuples passed to compatibility() must have same size."


def test_compatibility_measure_callable():
    """ Gives a callable measure to compatibility and tests if it is used """

    def score(a, b):
        return a + b

    a = [1, 1]
    b = [0, 0.5]
    output = group_graph.compatibility(a, b, objective_measures=[score, score])
    assert output == sum([1, 1.5])


def test_compatibility_measure_preset():
    """ Test all preset measures """
    a = [1, 1]
    b = [0, 0.5]

    output = group_graph.compatibility(a, b, objective_measures=["avg", "avg"])
    assert output == sum([0.5, 0.75])
    output = group_graph.compatibility(a, b, objective_measures=["max", "max"])
    assert output == sum([1, 1])
    output = group_graph.compatibility(a, b, objective_measures=["min", "min"])
    assert output == sum([0, 0.5])
    output = group_graph.compatibility(a, b, objective_measures=["match", "match"])
    assert output == sum([0, 0])
    output = group_graph.compatibility(a, b, objective_measures=["diff", "diff"])
    assert output == sum([1, 0.5])


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


def test_compatibility_measure_average():
    """ Test if measure of different student scores return an average """
    a = [1, 1]
    b = [0, 1]
    output = group_graph.compatibility(a, b)
    expected_output = 1.5
    assert output == expected_output


def test_compatibility_measure_max():
    """ Test if measure of different student scores return a maximum """
    a = [1, 0]
    b = [0, 0.5]
    objective_measures = ("max", "max")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 1.5
    assert output == expected_output


def test_compatibility_measure_min():
    """ Test if measure of different student scores return a minimum """
    a = [1, 0]
    b = [0, 0.5]
    objective_measures = ("min", "min")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 0
    assert output == expected_output


def test_compatibility_measure_match():
    """ Test if measure of different student scores are both equal """
    a = [1, 0]
    b = [1, 0.5]
    objective_measures = ("match", "match")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    assert output == sum([1, 0])


def test_compatibility_measure_diff():
    """ Test if measure of different student scores returns an absolute value difference """
    a = [1, 0]
    b = [0, 0.5]
    objective_measures = ("diff", "diff")
    output = group_graph.compatibility(a, b, objective_measures=objective_measures)
    expected_output = 1.5
    assert output == expected_output


def test_compatibility_measure_error():
    """ Test if wrong measure raises Exception error """
    a = tuple([1.0, 0.8])
    b = tuple([2.0, 0.5])
    with pytest.raises(Exception) as excinfo:
        group_graph.compatibility(a, b, objective_measures=["su", "mu"])
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Invalid measure"


def test_group_graph_partition():
    """
    Test for using recursive Kernighan-Lin algorithm that checks the output of
    the group_graph_partition function with preferences as input
    """
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
    preference = {
        "one": {"seven", "five"},
        "two": {"three", "six"},
        "three": {"two", "four"},
        "four": {"four", "three"},
        "five": {"six", "one"},
        "six": {"five"},
        "seven": {"six"},
        "eight": {"seven"},
    }
    output = group_graph.group_graph_partition(students, 4, preferences=preference)
    assert len(output[0]) == 2
