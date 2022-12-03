"""
    Authors: Indiana, Becky, Irmak
    Date: 2 Dec 2022

    Generates and pickles ensembles.
"""

import numpy as np
import pickle as pkl
from gerrychain import Partition, constraints, MarkovChain
from gerrychain.updaters import cut_edges, Tally
from gerrychain.tree import recursive_tree_part
from gerrychain.proposals import recom
from gerrychain.accept import always_accept
from functools import partial
from utils_creation import graph_of_partition

np.random.seed(123456)

# number of generated plans in each ensemble
NUM_STEPS = 30000

def main():
    print(f'Steps = {NUM_STEPS}')

    """ Load base VTDs dual graph
    """
    with open('../objects/VTDs_graph.pkl', 'rb') as f:
        VTDs_graph = pkl.load(f)

    print('Loaded base dual graph...')


    """ Set population variables
    """
    # total population
    total_pop = 0
    for v in VTDs_graph.nodes():
        total_pop += VTDs_graph.nodes()[v]['TOTPOP']

    # ideal population
    num_districts = 18
    ideal_pop = total_pop / num_districts
    
    # population difference % allowed
    pop_tolerance = 0.02


    """ Create initial partitions from base dual graph
    """
    # gerrymandered
    part_2011 = Partition(VTDs_graph, 'CD_2011', {'cut edges': cut_edges, 'district pop': Tally('TOTPOP', alias = 'district pop')})

    # non-gerrymandered
    part_2018 = Partition(VTDs_graph, 'REMEDIAL', {'cut edges': cut_edges, 'district pop': Tally('TOTPOP', alias = 'district pop')})

    # random
    plan_random = recursive_tree_part(VTDs_graph, range(num_districts), ideal_pop, 'TOTPOP', pop_tolerance, 10)
    part_random = Partition(VTDs_graph, plan_random, {'cut edges': cut_edges, 'district pop': Tally('TOTPOP', alias = 'district pop')})


    """ Set proposal method: ReCom
    """
    rw_proposal = partial(
        recom,
        pop_col = 'TOTPOP',
        pop_target = ideal_pop,
        epsilon = pop_tolerance,
        node_repeats = 1
    )


    """ Initalize population contraints
    """
    pop_constraint_2011 = constraints.within_percent_of_ideal_population(
        part_2011, 
        pop_tolerance, 
        pop_key = 'district pop')

    pop_constraint_2018 = constraints.within_percent_of_ideal_population(
        part_2018, 
        pop_tolerance, 
        pop_key = 'district pop')
    
    pop_constraint_random = constraints.within_percent_of_ideal_population(
        part_random, 
        pop_tolerance, 
        pop_key = 'district pop')
    

    """ Initialize random walks
    """
    random_walk_2011 = MarkovChain(
        proposal = rw_proposal, 
        constraints = [pop_constraint_2011],
        accept = always_accept,
        initial_state = part_2011, 
        total_steps = NUM_STEPS) 

    random_walk_2018 = MarkovChain(
        proposal = rw_proposal, 
        constraints = [pop_constraint_2018],
        accept = always_accept,
        initial_state = part_2018, 
        total_steps = NUM_STEPS) 
    
    random_walk_random = MarkovChain(
        proposal = rw_proposal, 
        constraints = [pop_constraint_random],
        accept = always_accept,
        initial_state = part_random, 
        total_steps = NUM_STEPS) 


    print('Starting random walks...')

    """ Run random walks
    """
    # init lists of number of cut edges
    num_cut_edges_ensemble_2011 = []
    num_cut_edges_ensemble_2018 = []
    num_cut_edges_ensemble_random = []

    # init lists of graphs
    graph_ensemble_2011 = []
    graph_ensemble_2018 = []
    graph_ensemble_random = []

    # walk starting from 2011 partition
    for part in random_walk_2011:
        # add number of cut edges to ensemble
        num_cut_edges_ensemble_2011.append(len(part['cut edges']))
        # add graph of partition to ensemble
        graph_ensemble_2011.append(graph_of_partition(part))
    print('Finished random walk from 2011 partition...')

    # walk starting from 2018 partition
    for part in random_walk_2018:
        # add number of cut edges to ensemble
        num_cut_edges_ensemble_2018.append(len(part['cut edges']))
        # add graph of partition to ensemble
        graph_ensemble_2018.append(graph_of_partition(part))
    print('Finished random walk from 2018 partition...')

    # walk starting from random partition
    for part in random_walk_random:
        # add number of cut edges to ensemble
        num_cut_edges_ensemble_random.append(len(part['cut edges']))
        # add graph of partition to ensemble
        graph_ensemble_random.append(graph_of_partition(part))
    print('Finished random walk from random partition...')


    print('Pickling...')

    """ Pickle ensembles
    """
    # pickle num cut edges ensembles
    with open('../ensembles/cut_edges/cut_edges_2011.pkl', 'wb') as f:
        pkl.dump(num_cut_edges_ensemble_2011, f)

    with open('../ensembles/cut_edges/cut_edges_2018.pkl', 'wb') as f:
        pkl.dump(num_cut_edges_ensemble_2018, f)

    with open('../ensembles/cut_edges/cut_edges_random.pkl', 'wb') as f:
        pkl.dump(num_cut_edges_ensemble_random, f)

    # pickle graph ensembles
    with open('../ensembles/graphs/graphs_2011.pkl', 'wb') as f:
        pkl.dump(graph_ensemble_2011, f)

    with open('../ensembles/graphs/graphs_2018.pkl', 'wb') as f:
        pkl.dump(graph_ensemble_2018, f)

    with open('../ensembles/graphs/graphs_random.pkl', 'wb') as f:
        pkl.dump(graph_ensemble_random, f)

    print('Done.')


if __name__ == '__main__':
    main()
