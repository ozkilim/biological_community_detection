import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community import k_clique_communities
import networkx.algorithms.community as nx_comm
from sklearn.cluster import SpectralClustering
from sklearn import metrics
import itertools
import numpy as np
import infomap
from infomap import Infomap

def presentCommunities(G,communities):
    '''
    This function takes in a graph object
    and a list of its communities. It returns
    a visualisation of the communities each 
    with its own coloring
    '''

    pos = nx.spring_layout(G)
    nx.draw(G, pos, edge_color='k',  with_labels=False,
            font_weight='light', node_size= 20, width= 0.9)

    # visualise the communities ground truth by coloring nodes.
    colors = "bgrcmykw"
    for idx,c in enumerate(communities):
        nx.draw_networkx_nodes(G, pos, nodelist=c, node_color=colors[idx],node_size=20)
        
    plt.show()