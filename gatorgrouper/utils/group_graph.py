""" Functions for creating groups via graph partitioning """
from typing import List, Set, Tuple
from math import log
from networkx import Graph
from networkx.algorithms.community import kernighan_lin_bisection
from networkx.algorithms.cuts import cut_size

# pylint: disable=bad-continuation,too-many-locals


def recursive_kl(graph: Graph, numgrp=2) -> List[Set[int]]:
    """
    Recursively use the Kernighan-Lin algorithm to create a k-way graph partition.
    This function will either return two groups or more than two depending on the
    value of numgrp. Each group generated is different from the previous.
    """
    power = log(numgrp, 2)
    if power != int(power) or power < 1:
        raise ValueError("numgrp must be a power of 2 and at least 2.")
    # For a group of two bisect it and return two groups
    if numgrp == 2:
        # Base case for recursion: use Kernighan-Lin to create 2 groups
        return list(kernighan_lin_bisection(graph))
    # For the next group of two divide numgrp by 2
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
    # Edges are added from the nodes on the graph, creating subsets
    for i, subset1 in enumerate(partition):
        for subset2 in partition[i:]:
            # Sum of weights added from all subsets and set equal to cut
            cut += cut_size(graph, subset1, T=subset2)
    return cut


def compatibility(
    a: Tuple[int], b: Tuple[int], objective_weights=None, objective_measures=None
) -> int:
    """
    Returns a single score representing the compatibility between student a and student b.
    Each entry in a and b is compared according to a particular compatibility measure,
    and then scaled according to a weight representing the importance of that entry.
    The result is the sum of all these scaled scores.

    By passing in an objective_measures list, this function supports the following measures:
        "sum":      a[i] + b[i]
        "avg":      the mean of a[i] and b[i]
        "max":      the max of a[i] and b[i]
        "min":      the min of a[i] and b[i]
        "match":    1 if a[i] == b[i], 0 otherwise. Suitable for all data types supporting ==.
        "diff":     the difference between a[i] and b[i]
    Alternatively, a custom function may be passed in to use as a compatibility measure.
    If no measures are specified, "avg" is used as a default.
    """
    if not len(a) == len(b):
        # Raise an exception notice if student tuples don't match
        raise Exception("Tuples passed to compatibility() must have same size.")
    if objective_weights is None:
        # Return length
        objective_weights = [1] * len(a)
    if objective_measures is None:
        # Default to return average if set equal to None
        objective_measures = ["avg"] * len(a)
    scores = []
    for a_score, b_score, weight, measure in zip(
        a, b, objective_weights, objective_measures
    ):
        # Compare a[i] and b[i] using the appropriate compatibility measure
        if callable(measure):
            compat = measure(a_score, b_score)
        elif measure == "avg":
            compat = float(a_score + b_score) / 2
        elif measure == "max":
            compat = max(a_score, b_score)
        elif measure == "min":
            compat = min(a_score, b_score)
        elif measure == "match":
            compat = int(a_score == b_score)
        elif measure == "diff":
            compat = abs(a_score - b_score)
        else:
            raise Exception("Invalid measure")

        # Scale the compatibility of a[i] and b[i] using the i-th objective weight
        scores.append(compat * weight)
    return sum(scores)


def group_graph_partition(
    inputlist,
    numgrp=2,
    objective_weights=None,
    objective_measures=None,
    preferences=None,
    preferences_weight=1.1,
    preferences_weight_match=1.3,
):
    """
    Form groups using recursive Kernighan-Lin algorithm by reading in students list
    and weight list and partitioning the vertices.
    """
    # Read in students list and the weight list
    students = [item[0] for item in inputlist]
    weights = [item[1:] for item in inputlist]
    # Create graph and populate with node weights
    vertex_weight_pairs = enumerate([{"weight": w} for w in weights])
    G = Graph()
    G.add_nodes_from(vertex_weight_pairs)

    # Add edges between distinct vertices, weighted by compatibility score
    for i, w1 in enumerate(weights):
        for j, w2 in enumerate(weights[:i]):
            score = compatibility(
                w1,
                w2,
                objective_weights=objective_weights,
                objective_measures=objective_measures,
            )
            if preferences:
                # Scale the compatibility score based on students' preferences for each other
                prefs_j = preferences.get(students[j])
                prefs_i = preferences.get(students[i])
                match_j = students[i] in prefs_j if prefs_j else None
                match_i = students[j] in prefs_i if prefs_i else None
                if match_i and match_j:
                    score = score * preferences_weight_match
                elif match_i or match_j:
                    score = score * preferences_weight
            G.add_edge(i, j, weight=score)

    # Partition the vertices
    partition = recursive_kl(G, numgrp=numgrp)
    groups = []
    for p in partition:
        groups.append([inputlist[i] for i in p])
    return groups
