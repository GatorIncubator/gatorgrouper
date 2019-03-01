from typing import List, Set, Tuple
from math import log
from networkx import Graph
from networkx.algorithms.community import kernighan_lin_bisection
from networkx.algorithms.cuts import cut_size


def recursive_kl(graph: Graph, num_groups=2) -> List[Set[int]]:
    """
    Recursively use Kernighan-Lin bisection to create a k-way graph partition
    """
    power = log(num_groups, 2)
    if power != int(power) or power < 1:
        raise ValueError("num_groups must be a power of 2 and at least 2.")
    if num_groups == 2:
        return list(kernighan_lin_bisection(graph))
    else:
        next_num_groups = num_groups / 2
        groups = []
        for subset in kernighan_lin_bisection(graph):
            subgraph = graph.subgraph(subset)
            groups += recursive_kl(subgraph, num_groups=next_num_groups)
        return groups


def compatibility(a: Tuple[int], b: Tuple[int], preferences=[]) -> int:
    """
    Returns a score representing the compatibility between student a and student b.
    The maximum of each a[i] and b[i] in the tuples is scaled by preferences[i],
    and the score is the sum of all of these scaled values.
    """
    if not len(a) == len(b):
        raise Exception("Tuples passed to compatibility() must have same size")
    if not preferences:
        preferences = [1] * len(a)
    adjusted_scores = [max(_a, _b) * _p for _a, _b, _p in zip(a, b, preferences)]
    return sum(adjusted_scores)


def group_graph_partition(
    responses: List[str], weights: List[Tuple[int]], grpsize: int
) -> List[str]:
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
    partition = recursive_kl(G, num_groups=2)
    groups = []
    print("Partition:")
    for p in partition:
        groups += [responses[i] for i in p]
        print([G.nodes[i]["weight"] for i in p])
    # TODO: this is only the total edge cut size when we are bipartitioning...
    print("Total cut size:", cut_size(G, partition[0], weight="weight"))
    return groups


if __name__ == "__main__":
    # Create graph and populate with node weights
    students = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    weights = [
        (0, 0),
        (0, 0.5),
        (0.5, 0),
        (0.75, 0.75),
        (0.8, 0.1),
        (0, 1),
        (1, 0),
        (1, 1),
    ]
    group_graph_partition(students, weights, 4)
