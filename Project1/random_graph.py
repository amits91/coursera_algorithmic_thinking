__author__ = 'Amit Srivastava'
'''
Generates Random Graph
'''

import random


def generate_undir_random_graph_ER(n, p):
    '''
    :param n:
    :param p:
    :return: None
    '''
    nodes = range(n)
    edges = set()
    for i in nodes:
        for j in nodes:
            if i == j:
                continue
            a = random.randrange(0, 1)
            if a < p :
                edges.add(tuple(set([i, j])))
    print "n:", n, "p:", p, "len(E):", len(edges)
    print edges

# generate_undir_random_graph_ER(10, 0)
# generate_undir_random_graph_ER(10, .1)

def generate_random_directed_graph(n, p):
    '''
    :param n: Total number of nodes
    :param p: Probability of an edge
    :return: dictionary of directed graph
    '''
    nodes = range(n)
    graph = {}
    for node in nodes:
        graph[node] = set([])

    for start in nodes:
        for end in nodes:
            if start == end:
                continue
            a = random.random()
            if a < p :
                graph[start].add(end)
    return graph

# print generate_random_directed_graph(10, 0.1)
