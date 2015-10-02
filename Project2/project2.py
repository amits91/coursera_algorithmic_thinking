'''
Project 2: Algorithmic thinking
'''
__author__ = 'Amit Srivastava'

# import example_graphs as eg
from collections import deque

def bfs_visited(ugraph, start_node):
    '''
    BFS implementation
    :param ugraph: Undirected Graph
    :param start_node: start node
    :return: set of visited nodes
    '''
    visited = {start_node: True}
    queue = deque()
    queue.appendleft(start_node)
    while len(queue) > 0:
        jnode = queue.pop()
        for hnode in ugraph[jnode]:
            if not visited.has_key(hnode):
                visited[hnode] = True
                queue.appendleft(hnode)
    # print visited
    return set(visited.keys())

# print bfs_visited(EX_GRAPH1, 1)

def cc_visited(ugraph):
    '''
    CC visited
    :param ugraph: Undirected Graph
    :return: set of connected components
    '''
    rem_nodes = set(ugraph.keys())
    ccs = []
    while len(rem_nodes) > 0:
        inode = rem_nodes.pop()
        # print inode
        wset = bfs_visited(ugraph, inode)
        # print 'visited', wset
        ccs.append(wset)
        rem_nodes.difference_update(wset)
        # print 'rem_nodes', rem_nodes
    return ccs

# print cc_visited(EX_GRAPH2)
def largest_cc_size(ugraph):
    '''
     Takes the undirected graph ugraph
     and returns the size (an integer) of the
      largest connected component in ugraph.
    :param ugraph:
    :return:
    '''
    cc_size = 0
    ccs = cc_visited(ugraph)
    for cci in ccs:
        if len(cci) > cc_size:
            cc_size = len(cci)

    return cc_size

# print largest_cc_size(EX_GRAPH2)

def remove_node(ugraph, node):
    '''
    remove node from graph
    :param ugraph:
    :param node:
    :return:
    '''
    print 'Node:', node
    print ugraph[node]
    if not ugraph.has_key(node):
        return
    for edge in ugraph[node]:
        print 'Before', ugraph[edge]
        # if node in ugraph[edge]:
        ugraph[edge].discard(node)
        print 'After', ugraph[edge]
    ugraph.pop(node)
    print ugraph

def compute_resilience(ugraph, attack_order):
    '''
    resilience
    :param ugraph:
    :param attack_order: list of nodes
    :return:
    '''
    res = [largest_cc_size(ugraph)]
    for node in attack_order:
        remove_node(ugraph, node)
        res.append(largest_cc_size(ugraph))
    return res

# print compute_resilience(eg.GRAPH3, [1, 2])
