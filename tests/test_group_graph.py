""" Test group graph algorithm"""
from gatorgrouper.utils import group_graph
from networkx import Graph


def test_recursive_kl():
    """ Test if groups made match recursion"""
    weights = [[0, 0], [0, 0.5], [0.5, 0], [0.75, 0.75], [0.8, 0.1], [0, 1], [1, 0], [1, 1]]
    vertex_weight_pairs = enumerate([{"weight": w} for w in weights])
    G = Graph()
    G.add_nodes_from(vertex_weight_pairs)
    groups = []
    for i in kernighan_lin_bisection(G):
        subgraph = G.subgraph(subset)
        groups.extend(recursive_kl(subgraph, numgrp=next_numgrp))
    assert i in groups is True


def test_main():
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
    weights = [[0, 0], [0, 0.5], [0.5, 0], [0.75, 0.75], [0.8, 0.1], [0, 1], [1, 0], [1, 1]]
    groups = group_graph.group_graph_partition(students, 4)
    assert weights in groups
