"""
    Authors: Indiana, Becky, Irmak
    Date: 2 Dec 2022

    Create base dual graph and pickle it.
"""

import pickle as pkl
import geopandas as gpd
from gerrychain import Graph

def main():
    # import VTDs
    VTDs = gpd.read_file('../data/PA-shapefiles-master/PA/PA.shp')

    # dual graph from VTDs
    VTDs_graph = Graph.from_geodataframe(VTDs)

    # pickle graph
    with open('../objects/VTDs_graph.pkl', 'wb') as f:
        pkl.dump(VTDs_graph, f)

if __name__ == '__main__':
    main()