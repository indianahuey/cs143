"""
    Authors: Indiana, Becky, Irmak
    Date: 2 Dec 2022

    Functions for graph analysis.
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall


def metric_ensemble(metric, graph_ensemble):
    """ Return list of metric values,
        given list of graphs---
        i.e. apply metric to ensemble.
    """
    ensemble = []
    for graph in graph_ensemble:
        ensemble.append(metric(graph))
    return ensemble


def visualize(metric, graph_ensemble, graphs, colors, linestyles, title):
    """ Plot distribution of metric values
        from graph ensemble, and place metric
        values of graphs in distribution.
    """
    # plot ensemble distribution
    plt.figure()
    plt.hist(
        metric_ensemble(metric, graph_ensemble),
        color='grey'
    )

    # plot specific graphs in distribution
    for i, G in enumerate(graphs):
        plt.axvline(
            metric(G),
            color=colors[i],
            linestyle=linestyles[i]
        )

    plt.title(title)
    plt.show()


def avg_vertex_degree(dual_graph):
    """ Return mean vertex degree,
        given graph.
    """
    total = 0
    for v in dual_graph:
        total += sum(v)
    return total / len(dual_graph)


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


def shortest_paths(dual_graph):
    """ Return length of shortest paths
        between all pairs of vertices.
    """
    dual_graph = csr_matrix(dual_graph)
    dist_matrix, predecessors = floyd_warshall(
        csgraph=dual_graph,
        directed=False,
        return_predecessors=True
    )
    return dist_matrix, predecessors


def avg_shortest_paths_vertex(dist_matrix, v):
    """ Return the average length of shortest paths
        between vertex v and all other vertices.
    """
    return sum(dist_matrix[v]) / (len(dist_matrix)-1)


def avg_shortest_paths_dist_matrix(dist_matrix):
    """ Return the average length of all shortest paths
        (between pairs of vertices) in the graph.
    """
    num_vertices = len(dist_matrix)
    num_pairs = (num_vertices * (num_vertices - 1)) / 2
    return np.sum(np.triu(dist_matrix)) / num_pairs


def avg_shortest_paths(graph):
    """ Return average of all pairs shortest paths,
        given graph.
    """
    dist_matrix, predecessors = shortest_paths(graph)
    return avg_shortest_paths_dist_matrix(dist_matrix)


def max_shortest_paths(graph):
    """ Return longest of all pairs shortest paths,
        given graph.
    """
    dist_matrix, predecessors = shortest_paths(graph)
    return max([max(v) for v in dist_matrix])


def avg_betweenness(graph):
    """ Return average of all vertex betweenness,
        given graph.
    """
    # adj matrix to nx graph
    nx_graph = nx.from_numpy_array(np.array(graph))
    # dict<node: betweenness>
    betweenness = nx.betweenness_centrality(nx_graph)
    return sum(betweenness.values()) / len(betweenness)


def min_betweenness(graph):
    """ Return min of all vertex betweenness,
        given graph.
    """
    # adj matrix to nx graph
    nx_graph = nx.from_numpy_array(np.array(graph))
    # dict<node: betweenness>
    betweenness = nx.betweenness_centrality(nx_graph)
    return min(betweenness.values())


def max_betweenness(graph):
    """ Return max of all vertex betweenness,
        given graph.
    """
    # adj matrix to nx graph
    nx_graph = nx.from_numpy_array(np.array(graph))
    # dict<node: betweenness>
    betweenness = nx.betweenness_centrality(nx_graph)
    return max(betweenness.values())