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
    # https://matplotlib.org/stable/gallery/color/named_colors.html
    colors = ['firebrick', 'olivedrab', 'burlywood']
    plt.figure()
    plt.title('Cut Edges from 10 Steps')
    plt.hist(cut_edges_2011[:10], color=colors[0], alpha=1, bins=15)
    plt.hist(cut_edges_2018[:10], color=colors[1], alpha=1, bins=15)
    plt.hist(cut_edges_random[:10], color=colors[2], alpha=1, bins=15)
    plt.ylabel('# Plans')
    plt.xlabel('# Cut Edges')
    plt.show()

    plt.figure()
    plt.title('Cut Edges from 100 Steps')
    plt.hist(cut_edges_2011[:100], color=colors[0], alpha=0.9, bins=15)
    plt.hist(cut_edges_2018[:100], color=colors[1], alpha=0.9, bins=15)
    plt.hist(cut_edges_random[:100], color=colors[2], alpha=0.9, bins=15)
    plt.ylabel('# Plans')
    plt.xlabel('# Cut Edges')
    plt.show()

    plt.figure()
    plt.title('Cut Edges from 50,000 Steps')
    plt.hist(cut_edges_2011, color=colors[0], alpha=0.85, bins=15)
    plt.hist(cut_edges_2018, color=colors[1], alpha=0.85, bins=15)
    plt.hist(cut_edges_random, color=colors[2], alpha=0.85, bins=15)
    plt.ylabel('# Plans')
    plt.xlabel('# Cut Edges')
    plt.show()


    """ Do analysis
    """
    ensemble = graphs_random
    graphs = [G_2011, G_ts, G_2018]
    colors = ['firebrick', 'palevioletred', 'olivedrab']
    linestyles = ['dashed', 'dashdot', 'dotted']

    visualize(avg_vertex_degree, ensemble, graphs, colors, linestyles, 'Average Vertex Degree', 'Avg. Degree')
    visualize(min_vertex_degree, ensemble, graphs, colors, linestyles, 'Minumum Vertex Degree', 'Min Degree')
    visualize(max_vertex_degree, ensemble, graphs, colors, linestyles, 'Maximum Vertex Degree', 'Max Degree')

    return 0

    visualize(avg_shortest_paths, ensemble, graphs, colors, linestyles, 'Average Length of All Pairs Shortest Path', 'Avg. Length')
    visualize(max_shortest_paths, ensemble, graphs, colors, linestyles, 'Longest Length of All Pairs Shortest Path', 'Longest Length')

    visualize(avg_betweenness, ensemble, graphs, colors, linestyles, 'Average Vertex Betweenness Centrality', 'Avg. Betweenness')
    visualize(min_betweenness, ensemble, graphs, colors, linestyles, 'Minimum Vertex Betweenness Centrality', 'Min Betweenness')
    visualize(max_betweenness, ensemble, graphs, colors, linestyles, 'Maximum Vertex Betweenness Centrality', 'Max Betweenness')


if __name__ == '__main__':
    main()