__author__ = 'am'

import UPATrial as uh
import degrees as graph_util

def generate_UPA(n, m):
    '''
    UPA Algorithm to generate random undirected graphs
    :param n: number of nodes
    :param m: integer (1 <= m <= n)
    :return:A directed graph
    '''
    gE = graph_util.make_complete_graph(m)
    dpat = uh.UPATrial(m)
    for i in range(m, n):
        # V1 = select_random_nodes(gE, m, indeg, totindeg)
        V1 = dpat.run_trial(m)
        gE[i] = set(V1)
        for neighbour in V1:
            gE[neighbour].add(i)
    return gE

def main():
    print generate_UPA(10, 3)

if __name__ == '__main__':
    main()
