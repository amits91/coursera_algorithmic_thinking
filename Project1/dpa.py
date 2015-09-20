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

def totalindeg(indeg):
    sum = 0
    for node in indeg.keys():
        sum = sum + indeg[node]
    return sum


def select_random_nodes(digraph, m, indeg=None, sum = -1):
    '''
    Randomly select nodes based on probability as per DPA
    :param V: input indeg dictionaries
    :return: a list of selected nodes V1
    '''
    if indeg == None:
        indeg = graph_util.compute_in_degrees(digraph)
        sum = totalindeg(indeg)
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
    indeg = graph_util.compute_in_degrees(gE)
    totindeg = totalindeg(indeg)
    for i in range(m, n):
        V1 = select_random_nodes(gE, m, indeg, totindeg)
        gE[i] = set(V1)
        for j in V1:
            indeg[j] = indeg[j] + 1
        indeg[i] = 0
        totindeg = totindeg + len(V1)
    return gE

def print_gi(dig):
    print "Nodes", len(dig)
    tot = 0
    for i in dig.keys():
        tot = tot + len(dig[i])

    avg = (tot * 1.0)/len(dig)
    print "avg out-degree", avg

# print_gi(graph_util.EX_GRAPH2)
#
# dpg = DPA(10, 2)
# for i in dpg.keys():
#     print i, '=>', dpg[i]
# print_gi(dpg)

# import parse_graph as pg
# cg = pg.load_graph(pg.CITATION_URL)
# print_gi(cg)
# dcg = DPA(len(cg), 15)
# print_gi(dcg)
#
# # Gives output
# # Loaded graph with 27770 nodes
# # Nodes 27770
# # avg out-degree 12.7032048974
# # Nodes 27770
# # avg out-degree 12.3318329132