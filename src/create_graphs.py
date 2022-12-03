"""
    Authors: Indiana, Becky, Irmak
    Date: 2 Dec 2022

    Create base dual graph and pickle it.
"""

import pickle as pkl
import geopandas as gpd
from gerrychain import Graph, Partition
from utils_creation import graph_of_partition

def main():
    # import VTDs
    VTDs = gpd.read_file('../data/PA-shapefiles-master/PA/PA.shp')

    # dual graph from VTDs
    VTDs_graph = Graph.from_geodataframe(VTDs)

    # other relevant graphs
    G_2011 = graph_of_partition(Partition(VTDs_graph, 'CD_2011'))
    G_ts = graph_of_partition(Partition(VTDs_graph, 'TS'))
    G_2018 = graph_of_partition(Partition(VTDs_graph, 'REMEDIAL'))

    # pickle graphs
    with open('../objects/VTDs_graph.pkl', 'wb') as f:
        pkl.dump(VTDs_graph, f)

    with open('../objects/G_2011.pkl', 'wb') as f:
        pkl.dump(G_2011, f)

    with open('../objects/G_ts.pkl', 'wb') as f:
        pkl.dump(G_ts, f)

    with open('../objects/G_2018.pkl', 'wb') as f:
        pkl.dump(G_2018, f)

if __name__ == '__main__':
    main()