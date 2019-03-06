""" Functions for creating groups via graph partitioning """
from typing import List, Set, Tuple
from math import log
from networkx import Graph
from networkx.algorithms.community import kernighan_lin_bisection
from networkx.algorithms.cuts import cut_size


def recursive_kl(graph: Graph, numgrp=2) -> List[Set[int]]:
    """
    Recursively use Kernighan-Lin algorithm to create a k-way graph partition
    """
    power = log(numgrp, 2)
    if power != int(power) or power < 1:
        raise ValueError("numgrp must be a power of 2 and at least 2.")
    if numgrp == 2:
        # Base case for recursion: use Kernighan-Lin to create 2 groups
        return list(kernighan_lin_bisection(graph))
    next_numgrp = numgrp / 2
    groups = []
    for subset in kernighan_lin_bisection(graph):
        subgraph = graph.subgraph(subset)
        groups.extend(recursive_kl(subgraph, numgrp=next_numgrp))
    return groups


def total_cut_size(graph: Graph, partition: List[int]) -> float:
    """
    Computes the sum of weights of all edges between different subsets in the partition
    """
    cut = 0.0
    for i, subset1 in enumerate(partition):
        for subset2 in partition[i:]:
            cut += cut_size(graph, subset1, T=subset2)
            print(subset1, subset2, cut)
    return cut


def compatibility(a: Tuple[int], b: Tuple[int], preferences=None) -> int:
    """
    Returns a score representing the compatibility between student a and student b.
    The maximum of each a[i] and b[i] in the tuples is scaled by preferences[i],
    and the score is the sum of all of these scaled values.
    """
    if not len(a) == len(b):
        raise Exception("Tuples passed to compatibility() must have same size")
    if preferences is None:
        preferences = [1] * len(a)
    adjusted_scores = [max(_a, _b) * _p for _a, _b, _p in zip(a, b, preferences)]
    return sum(adjusted_scores)


def group_graph_partition(
    responses: List[str], weights: List[Tuple[int]], numgrp=2
) -> List[str]:
    """
    Form groups using recursive Kernighan-Lin algorithm
    """
    # Create graph and populate with node weights
    vertex_weight_pairs = enumerate([{"weight": w} for w in weights])
    G = Graph()
    G.add_nodes_from(vertex_weight_pairs)

    # Add edges between distinct vertices, weighted by compatibility score
    for i, w1 in enumerate(weights):
        for j, w2 in enumerate(weights[:i]):
            score = compatibility(w1, w2)
            G.add_edge(i, j, weight=score)
            print(i, j, w1, w2, score)

    # Partition the vertices
    partition = recursive_kl(G, numgrp=numgrp)
    groups = []
    print("Partition:")
    for p in partition:
        groups.append([responses[i] for i in p])
        print([G.nodes[i]["weight"] for i in p])
    print("Total cut size:", total_cut_size(G, partition))
    return groups


if __name__ == "__main__":
    students = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    student_weights = [
        (0, 0),
        (0, 0.5),
        (0.5, 0),
        (0.75, 0.75),
        (0.8, 0.1),
        (0, 1),
        (1, 0),
        (1, 1),
    ]
    student_groups = group_graph_partition(students, student_weights, 4)
    print(student_groups)
