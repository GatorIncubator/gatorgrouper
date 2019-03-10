""" Test group graph algorithm"""
# from gatorgrouper.utils import group_graph
from networkx import Graph
from gatorgrouper.utils import group_graph


def test_recursive_kl():
    """ Test if groups made match recursion"""
    group = [{0, 2}, {4, 7}, {3, 5}, {1, 6}]
    weights = [[0, 0], [0, 0.5], [0.5, 0], [0.75, 0.75], [0.8, 0.1], [0, 1], [1, 0], [1, 1]]
    vertex_weight_pairs = enumerate([{"weight": w} for w in weights])
    G = Graph()
    G.add_nodes_from(vertex_weight_pairs)
    output = group_graph.recursive_kl(G, 4)
    alloutput =[]
    for i in output:
        if i =
        alloutput.append(output[i])
    assert [item for item in alloutput] in group
