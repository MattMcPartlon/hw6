from heapq import heappush, heappop
from math import inf, floor
from typing import DefaultDict,Tuple, Dict
import networkx as nx
import numpy as np
import sys
from collections import defaultdict

def dijkstra(G: nx.Graph, w:DefaultDict,  s) ->Tuple[Dict,Dict]:
    distances, parents = defaultdict(lambda : np.INF), defaultdict(lambda:s)
    Q = []
    #TODO
    return distances,parents

def relax(w, u, v, distances, parents) -> None:
    #TODO
    pass


def random_dijkstra_instance(n, p=0.2, min_w=0, max_w=10,
                             directed=True, return_target=False):
    """Returns input for dijkstra function
    Returns a (random) directed, weighted graph and a source vertex
     for the graph.

    :param n: order of the returned graph
    :param p: the edge probability in G
    :param min_w: minimum edge weight in G
    :param max_w: maximum edge weight in G
    :return: A tuple (G,w,source) if return target is False, ow. returns
    (G,w,source,target) tuple.
    """
    G = nx.generators.gnp_random_graph(n, p, directed=directed)
    w = defaultdict(lambda : defaultdict(lambda : np.Inf))
    for (u, v) in G.edges():
        wt = np.random.uniform(min_w, max_w)
        G.edges[u, v]['weight'] = wt
        w[u][v]=wt
    source, target = list(G.nodes)[0], list(G.nodes)[-1]
    if return_target:
        return G,w, source, target
    return G,w, source


def test_dijkstra(n, p=0.2, min_w=0, max_w=10, directed=True):
    """Tests the dijkstra implementation on a random weighted graph with
    n vertices.

    :param n: order of the  graph to test on
    :param p: the edge probability in G
    :param min_w: minimum edge weight in G
    :param max_w: maximum edge weight in G
    :param directed: whether or not the graph is directed.
    :return: True iff the distance output of dijkstra is the same
    as that generated by networkx's built in dijkstra function.
    """
    G, w, s = random_dijkstra_instance(n, p, min_w, max_w, directed)
    expected_ds, expected_path = nx.single_source_dijkstra(G, s)
    print(expected_path)
    print(expected_ds)
    actual_ds, parents = dijkstra(G, w, s)

    for v in G.nodes:
        assert actual_ds[v] == expected_ds[v]
    return True


if __name__ == "__main__":
    #feel free to modify code - add value for p, change min/max wt, etc.
    n = 40
    if len(sys.argv)>1:
        #run as python dijkstra.py n
        n = int(sys.argv[1])
    test_dijkstra(n)
