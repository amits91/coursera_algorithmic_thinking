__author__ = 'Amit Srivastava'
'''
Generates Random Graph
'''

import random

def generate_UER(n, p):
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
                graph[end].add(start)
    return graph

if __name__ == "__main__":
    print generate_UER(10, 0.1)
