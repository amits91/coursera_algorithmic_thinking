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
import dpa_helper as dh


# print nm.random.choice(range(5), 2, True, [0, .1, .8, 0, 0.1])

def totalindeg(indeg):
    sum = 0
    for node in indeg.keys():
        sum = sum + indeg[node]
    return sum


def select_random_nodes(digraph, m, indeg=None, sum=-1):
    '''
    Randomly select nodes based on probability as per DPA
    :param V: input indeg dictionaries
    :return: a list of selected nodes V1
    '''
    if indeg == None:
        indeg = graph_util.compute_in_degrees(digraph)
        sum = totalindeg(indeg)
    prob = [(indeg[j] + 1.0) / (sum + len(digraph)) for j in digraph.keys()]
    # print digraph.keys()
    # print prob
    V1 = nm.random.choice(digraph.keys(), m, True, prob)
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

def newDPA(n, m):
    '''
    DPA Algorithm to generate random directed graphs
    :param n: number of nodes
    :param m: integer (1 <= m <= n)
    :return:A directed graph
    '''
    gE = graph_util.make_complete_graph(m)
    dpat = dh.DPATrial(m)
    for i in range(m, n):
        # V1 = select_random_nodes(gE, m, indeg, totindeg)
        V1 = dpat.run_trial(m)
        gE[i] = set(V1)
    return gE

def print_gi(dig):
    tot = 0
    for i in dig.keys():
        tot = tot + len(dig[i])

    avg = (tot * 1.0) / len(dig)
    print ": Nodes", len(dig),
    print "avg out-degree", avg
    return avg

def print_comparison(dig, dpaF, label='oDPA'):
    print 'Original graph',
    avg = print_gi(dig)
    if avg < 1:
        m = 1
    else:
        m = int(avg)
    print label, len(dig), 'm =', m,
    newavg = print_gi(dpaF(len(dig), m))
    if newavg < avg:
        oless = True
    else:
        oless = False
    for i in range(2):
        if newavg < avg:
            if oless == False:
                break
            m = m + 1
            print label, len(dig), 'm =', m,
            newavg = print_gi(dpaF(len(dig), m))
        else:
            m = m - 1
            if m == 0 or oless == True:
                break
            print label, len(dig), 'm =', m,
            newavg = print_gi(dpaF(len(dig), m))



# print_comparison(graph_util.EX_GRAPH0, DPA)
# print_comparison(graph_util.EX_GRAPH0, newDPA, 'nDPA')
# print_comparison(graph_util.EX_GRAPH1, DPA)
# print_comparison(graph_util.EX_GRAPH1, newDPA, 'nDPA')
# print_comparison(graph_util.EX_GRAPH2, DPA)
# print_comparison(graph_util.EX_GRAPH2, newDPA, 'nDPA')

import parse_graph as pg
cg = pg.load_graph(pg.CITATION_URL)
print_gi(cg)
# dcg = DPA(len(cg), 15)
# ndcg = newDPA(len(cg), 14)
print_comparison(cg, newDPA, 'nDPA')
print_comparison(cg, DPA)

