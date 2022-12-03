"""
    Authors: Indiana, Becky, Irmak
    Date: 2 Dec 2022

    Functions for graph analysis.
"""

def min_vertex_degree(dual_graph):
    """ Return min vertex degree,
        given graph.
    """
    minimum = len(dual_graph) + 1
    for v in dual_graph:
        minimum = min(sum(v), minimum)
    return minimum


def max_vertex_degree(dual_graph):
    """ Return max vertex degree,
        given graph.
    """
    maximum = 0
    for v in dual_graph:
        maximum = max(sum(v), maximum)
    return maximum


def avg_vertex_degree(dual_graph):
    """ Return mean vertex degree,
        given graph.
    """
    total = 0
    for v in dual_graph:
        total += sum(v)
    return total / len(dual_graph)