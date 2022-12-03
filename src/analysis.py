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
    plt.hist(cut_edges_2011, color='red', edgecolor='white')
    plt.hist(cut_edges_2018, color='green', edgecolor='white')
    plt.hist(cut_edges_random, color='grey', edgecolor='white')
    plt.show()


if __name__ == '__main__':
    main()