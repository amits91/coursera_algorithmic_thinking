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

generate_undir_random_graph_ER(10, 0)
generate_undir_random_graph_ER(10, .1)