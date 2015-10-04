'''
Code for application2
'''
__author__ = 'am'

import provided_code as provided
import project2 as proj
import UER as u
import UPA as upa
import random
import example_graphs as eg
import matplotlib.pyplot as plt

def print_gi(graph):
    '''
    Print graph info
    :param graph: undirected graph
    :return: None
    '''
    print ' Nodes:', len(graph)
    edges = 0
    for node in graph.keys():
        edges = edges + len(graph[node])
    print ' Edges:', edges/2

PROB = 0.002
M = 3
cgraph = provided.load_graph()
ergraph = u.generate_UER(len(cgraph), PROB)
upgraph = upa.generate_UPA(len(cgraph), M)

def random_order(graph):
    keys = graph.keys()
    random.shuffle(keys)
    return keys

def print_compute_resilience(graph, style='-b', label='default'):
    print_gi(graph)
    num_nodes = len(graph)
    attack = random_order(graph)
    cr = proj.compute_resilience(graph, attack)
    cx = range(num_nodes + 1)
    print '------------'
    print label
    print 'Random Nodes:', attack
    print "Y:", cr
    print "X:", cx
    plt.plot(cx, cr, style, label=label)

def main():
    print 'Computer Node Graph'
    print_gi(cgraph)
    print 'Random UER Graph'
    print_gi(ergraph)
    print 'Random UPA Graph'
    print_gi(upgraph)
    # print_compute_resilience(eg.GRAPH0)
    # print_compute_resilience(eg.GRAPH1)
    # print_compute_resilience(eg.GRAPH3)
    print_compute_resilience(cgraph, '-b', 'computer network')
    print_compute_resilience(ergraph, '-r', 'ER(p=' + str(PROB) + ')')
    print_compute_resilience(upgraph, '-g', 'UPA(m=' + str(M) + ')')
    plt.xlabel('Number of nodes removed')
    plt.ylabel('Size of Largest Connect component')
    plt.title('Simple plot of resilience of undirected graphs')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':
    main()

