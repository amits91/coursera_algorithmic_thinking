'''
Algorithmic Thinking
Application: 1
DPA graphs
'''
__author__ = 'asrivas'
import degrees as graph_util
# import random
# print random.sample(xrange(100), 10)
import numpy as nm
# print nm.random.choice(range(5), 2, True, [0, .1, .8, 0, 0.1])

def select_random_nodes(digraph, m):
    '''
    Randomly select nodes based on probability as per DPA
    :param V: input indeg dictionaries
    :return: a list of selected nodes V1
    '''
    indeg = graph_util.compute_in_degrees(digraph)
    sum = 0
    for node in digraph.keys():
        sum = sum + indeg[node]
    prob = [(indeg[j] + 1.0)/(sum + len(digraph)) for j in digraph.keys()]
    # print digraph.keys()
    # print prob
    V1 = nm.random.choice(digraph.keys(), m, True, prob )
    return V1

# print select_random_nodes(graph_util.EX_GRAPH1, 2)
# print range(3, 6)

def DPA(n, m):
    '''
    DPA Algorithm to generate random directed graphs
    :param n: number of nodes
    :param m: integer (1 <= m <= n)
    :return:A directed graph
    '''
    gE = graph_util.make_complete_graph(m)
    for i in range(m, n):
        V1 = select_random_nodes(gE, m)
        gE[i] = set(V1)
    return gE

# dpg = DPA(10, 4)
# for i in dpg.keys():
#     print i, '=>', dpg[i]
