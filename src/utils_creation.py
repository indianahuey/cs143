"""
    Authors: Indiana, Becky, Irmak
    Date: 2 Dec 2022

    Function for graph creation.
"""

from gerrychain.updaters import cut_edges

def graph_of_partition(partition):
    """ Return dual graph of partition,
        given partition. 
    """
    # init adjacency matrix
    dual_graph = [[0 for j in range(len(partition))] for i in range(len(partition))]
    # for each cut edge
    for u, v in cut_edges(partition):
        # dict<district key: vertex set>
        plan = partition.assignment.parts
        # district that u is in
        district_u = None 
        # district that v is in
        district_v = None
        # for each district
        for district_key in plan:
            district_set = plan[district_key]
            # try to locate u district
            if u in district_set:
                district_u = int(district_key)
            # otherwise try to locate v district
            # (elif as we know u and v not in same district by def cut edge)
            elif v in district_set:
                district_v = int(district_key)
            # stop early if located districts that u,v are in
            if district_u != None and district_v != None:
                break
        # add undirected edge to dual graph
        # -1 as district keys [1,n] while adjacency matrix [0,n-1]
        dual_graph[district_u-1][district_v-1] = 1
        dual_graph[district_v-1][district_u-1] = 1
    return dual_graph