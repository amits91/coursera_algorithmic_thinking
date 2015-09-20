__author__ = 'Amit Srivastava'
'''
Algorithmic Thinking
Project 1: Degree distribution of directed graphs
'''

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


# print EX_GRAPH0
# print EX_GRAPH1
# print EX_GRAPH2

def make_complete_graph(num_nodes):
    '''
    Make a complete graph
    '''
    graph = {}
    for start in range(num_nodes):
        for end in range(num_nodes):
            if start == end:
                continue
            if graph.has_key(start):
                graph[start].add(end)
            else:
                graph[start] = set([end])
    if num_nodes == 1:
        graph[0] = set([])
    return graph


# print make_complete_graph(1)

def compute_in_degrees(digraph):
    '''
    compute_in_degrees
    '''
    in_deg = {}
    nodes = digraph.keys()
    for node in nodes:
        in_deg[node] = 0
    for start in nodes:
        for end in digraph[start]:
            in_deg[end] = in_deg[end] + 1

    return in_deg


# print compute_in_degrees(EX_GRAPH2)

def in_degree_distribution(digraph):
    '''
    compute in degree distribution
    '''
    indd = {}
    indeg = compute_in_degrees(digraph)
    for node in digraph.keys():
        deg = indeg[node]
        if indd.has_key(deg):
            indd[deg] = indd[deg] + 1
        else:
            indd[deg] = 1
    return indd


def norm_in_deg_dist(digraph):
    '''
    make normalized in degree distribution
    '''
    indd = in_degree_distribution(digraph)
    tot = len(digraph)
    norm_indd = {}
    for deg in indd.keys():
        norm_indd[deg] = (1.0 * indd[deg]) / tot
    return norm_indd


def print_info(digraph):
    '''
    debug
    '''
    print 'The graph has', len(digraph), 'nodes.'
    print 'indd:'
    print in_degree_distribution(digraph)
    print 'normalized:'
    print norm_in_deg_dist(digraph)


# print in_degree_distribution(EX_GRAPH2)
# print norm_in_deg_dist(EX_GRAPH2)
print print_info(EX_GRAPH0)
print print_info(EX_GRAPH1)
print print_info(EX_GRAPH2)
