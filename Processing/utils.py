import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community import k_clique_communities
import networkx.algorithms.community as nx_comm
from sklearn.cluster import SpectralClustering
from sklearn import metrics
import itertools
import numpy as np
import infomap
import random
from infomap import Infomap

def presentCommunities(G,communities):
    '''
    This function takes in a graph object
    and a list of its communities. It returns
    a visualisation of the communities each 
    with its own coloring
    '''
    plt.figure(figsize=(10,10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, edge_color='k',  with_labels=False,
            font_weight='light', node_size= 3, width= 0.2)
    # visualise the communities ground truth by coloring nodes.
    
    for idx,c in enumerate(communities):
        color = generate_color()

        # Make new random color
        nx.draw_networkx_nodes(G, pos, nodelist=c, node_color=color,node_size=3)
        
    plt.show()

def generate_color():
    '''
    This function generates a random Hex color
    '''
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    return color

def presentBioCommunities(G,communities):
    '''
    This function takes in a graph object
    and a list of its communities. It returns
    a visualisation of the communities each 
    with its own coloring
    '''
    plt.figure(figsize=(10,10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, edge_color='k',  with_labels=False,
            font_weight='light', node_size= 3, width= 0.2)

    # visualise the communities ground truth by coloring nodes.
    for idx,c in enumerate(communities):
        # Make new random color
        color = generate_color()
        nx.draw_networkx_nodes(G, pos, nodelist=c, node_color=color,node_size=3)
        
    plt.show()

def NMI_reshape(communities,n):
    '''
    This function prepares the community structure for NMI calculation.
    Turn [1,5,6],[2,3,4] into [0 1 1 1 0 0] format for NMI calculation.
    -----
    Input:
    communities = found community structre in form :[1,5,6],[2,3,4]
    n  = number of nodes in network
    -----
    Output 
    [0 1 1 1 0 0] format with community id for each node
    '''
    labelset = list(np.zeros(n)) # Define empty list of length number of nodes
    for communit_id, community in enumerate(communities):
        for node in community:
            labelset[node] = communit_id

    return labelset