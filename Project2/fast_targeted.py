__author__ = 'Amit Srivastava'

import random
import provided_code as provided
import UPA as upa
import time

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
    otime = time.clock()
    fast = fast_targeted_order(graph)
    diff = time.clock() - otime
    fasttime = diff
    # print 'Fast:', fast
    otime = time.clock()
    slow = provided.targeted_order(graph)
    diff = time.clock() - otime
    # print 'Slow:', slow
    slowtime = diff
    return (n, fasttime, slowtime)

import matplotlib.pyplot as plt
def main():
    x = []
    yfast = []
    yslow = []
    for n in range(10, 1000, 10):
        times = compare_func(n)
        x.append(n)
        yfast.append(times[1])
        yslow.append(times[2])
    plt.plot(x, yfast, '-b', label='fast_targeted_order')
    plt.plot(x, yslow, '-r', label='targeted_order')
    # ylinear = [i * yfast[0] for i in x]
    # yquad = [ylinear[i] * ylinear[i] for i in range(len(x))]
    # plt.loglog(x, ylinear, '-g', label='linear')
    # plt.loglog(x, yquad, '-y', label='quad')
    plt.legend(loc='upper right')
    plt.xlabel('num of nodes n')
    plt.ylabel('running time (time.clock())')
    plt.title('Simple plot comparison of running times (desktop Python)')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
