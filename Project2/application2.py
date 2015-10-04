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

def print_compute_resilience(graph, order_func=random_order, style='-b', label='default'):
    print_gi(graph)
    num_nodes = len(graph)
    attack = order_func(graph)
    cr = proj.compute_resilience(graph, attack)
    cx = range(num_nodes + 1)
    print '------------'
    print label
    print 'Random Nodes:', attack
    print "Y:", cr
    print "X:", cx
    plt.plot(cx, cr, style, label=label)
    # cx = range(num_nodes)
    # percent_cc_vs_rem_nodes = [(cr[i] * 1.0)/(num_nodes - i) for i in cx]
    # print percent_cc_vs_rem_nodes
    # plt.plot(cx, percent_cc_vs_rem_nodes, style, label=label)
    plt.scatter([0.2 * num_nodes, ],[0, ], 50, color='black')

def main():
    print 'Computer Node Graph'
    print_gi(cgraph)
    print 'Random UER Graph'
    print_gi(ergraph)
    print 'Random UPA Graph'
    print_gi(upgraph)
    print_compute_resilience(cgraph , provided.targeted_order, '-b', 'computer network')
    print_compute_resilience(ergraph, provided.targeted_order, '-r', 'ER(p=' + str(PROB) + ')')
    print_compute_resilience(upgraph, provided.targeted_order, '-g', 'UPA(m=' + str(M) + ')')
    plt.xlabel('Number of nodes removed')
    plt.ylabel('Size of Largest Connect component')
    plt.title('Simple plot of resilience of undirected graphs (targeted order)')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':
    main()

