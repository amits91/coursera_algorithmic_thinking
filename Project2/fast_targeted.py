__author__ = 'Amit Srivastava'

import random
import provided_code as provided
import UPA as upa

def degree(graph, n):
    return len(graph[n])

def fast_targeted_order(ugraph):
    graph = provided.copy_graph(ugraph)
    degree_sets = {}
    n = len(graph)
    V = range(n)
    for k in V:
        degree_sets[k] = set()
    for i in V:
        d = degree(graph, i)
        degree_sets[d].add(i)
    L = {}
    i = 0
    for k in range(n-1, -1, -1):
        while len(degree_sets[k]) > 0:
            u = random.choice(list(degree_sets[k]))
            # print u
            degree_sets[k].remove(u)
            for v in graph[u]:
                d = degree(graph, v)
                degree_sets[d].remove(v)
                degree_sets[d - 1].add(v)
            L[i] = u
            i = i + 1
            provided.delete_node(graph, u)
    return list(L.values())

def compare_func(n):
    graph = upa.generate_UPA(n, 5)
    fast = fast_targeted_order(graph)
    print 'Fast:', fast
    slow = provided.targeted_order(graph)
    print 'Slow:', slow

def main():
    compare_func(10)

if __name__ == '__main__':
    main()
