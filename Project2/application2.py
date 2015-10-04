'''
Code for application2
'''
__author__ = 'am'

import provided_code as p
import UER as u
import UPA as upa

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

cgraph = p.load_graph(p.NETWORK_URL)
ergraph = u.generate_UER(1239, 0.002)
upgraph = upa.generate_UPA(1239, 3)


def main():
    print 'Computer Node Graph'
    print_gi(cgraph)
    print 'Random UER Graph'
    print_gi(ergraph)
    print 'Random UPA Graph'
    print_gi(upgraph)

if __name__ == '__main__':
    main()

