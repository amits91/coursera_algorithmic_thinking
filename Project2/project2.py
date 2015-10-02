'''
Project 2: Algorithmic thinking
'''
__author__ = 'Amit Srivastava'

from collections import deque

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


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

print largest_cc_size(EX_GRAPH2)