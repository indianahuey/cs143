""" Authors: Indiana, Becky, Irmak
    Date: 2 Dec 2022

    Analysis on ensembles.
"""

import pickle as pkl
import matplotlib.pyplot as plt
from utils_analysis import *

def main():
    """ Load relevant graphs
    """
    # gerrymandered 2011 enacted plan
    with open('../objects/G_2011.pkl', 'rb') as f:
        G_2011 = pkl.load(f)

    # gerrymandered TS proposed plan
    with open('../objects/G_ts.pkl', 'rb') as f:
        G_ts = pkl.load(f)

    # non-gerrymandered 2018 enacted plan
    with open('../objects/G_2018.pkl', 'rb') as f:
        G_2018 = pkl.load(f)


    """ Load ensembles
    """
    # ensembles of number of cut edges
    with open('../ensembles/cut_edges/cut_edges_2011.pkl', 'rb') as f:
        cut_edges_2011 = pkl.load(f)

    with open('../ensembles/cut_edges/cut_edges_2018.pkl', 'rb') as f:
        cut_edges_2018 = pkl.load(f)

    with open('../ensembles/cut_edges/cut_edges_random.pkl', 'rb') as f:
        cut_edges_random = pkl.load(f)

    # ensembles of graphs
    with open('../ensembles/graphs/graphs_2011.pkl', 'rb') as f:
        graphs_2011 = pkl.load(f)

    with open('../ensembles/graphs/graphs_2018.pkl', 'rb') as f:
        graphs_2018 = pkl.load(f)

    with open('../ensembles/graphs/graphs_random.pkl', 'rb') as f:
        graphs_random = pkl.load(f)


    """ Check for convergence
    """
    plt.figure()
    plt.title('Cut Edges from 10 Steps')
    plt.hist(cut_edges_2011[:10], color='red', alpha=0.85, bins=15)
    plt.hist(cut_edges_2018[:10], color='green', alpha=0.85, bins=15)
    plt.hist(cut_edges_random[:10], color='grey', alpha=0.85, bins=15)
    plt.show()

    plt.figure()
    plt.title('Cut Edges from 100 Steps')
    plt.hist(cut_edges_2011[:100], color='red', alpha=0.85, bins=15)
    plt.hist(cut_edges_2018[:100], color='green', alpha=0.85, bins=15)
    plt.hist(cut_edges_random[:100], color='grey', alpha=0.85, bins=15)
    plt.show()

    plt.figure()
    plt.title('Cut Edges from 30,000 Steps')
    plt.hist(cut_edges_2011, color='red', alpha=0.85, bins=15)
    plt.hist(cut_edges_2018, color='green', alpha=0.85, bins=15)
    plt.hist(cut_edges_random, color='grey', alpha=0.85, bins=15)
    plt.show()


    """ Do analysis
    """
    ensemble = graphs_random
    graphs = [G_2011, G_ts, G_2018]
    colors = ['red', 'orange', 'green']
    linestyles = ['dashed', 'dashed', 'dashdot']

    visualize(avg_vertex_degree, ensemble, graphs, colors, linestyles, 'Average Vertex Degree')
    visualize(min_vertex_degree, ensemble, graphs, colors, linestyles, 'Minumum Vertex Degree')
    visualize(max_vertex_degree, ensemble, graphs, colors, linestyles, 'Maximum Vertex Degree')
    visualize(avg_shortest_paths, ensemble, graphs, colors, linestyles, 'Average Shortest Paths')


if __name__ == '__main__':
    main()