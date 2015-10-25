'''
Generating random clusters
'''

import alg_cluster as ac
import random
import time
import project3 as prj

def gen_random_clusters(num_clusters):
    rndpts = set()
    while len(rndpts) < num_clusters:
        sign = random.choice([-1, 1])
        rndx = random.random() * sign
        sign = random.choice([-1, 1])
        rndy = random.random() * sign
        rndpts.add((rndx, rndy))
    cls = []
    for i in range(len(rndpts)):
        pts = rndpts.pop()
        cls.append(ac.Cluster(set([]), pts[0], pts[1], 0, 0))
    return cls

def compare_func(n):
    clus = gen_random_clusters(n)
    otime = time.clock()
    fast = prj.fast_closest_pair(clus)
    diff = time.clock() - otime
    fasttime = diff
    # print 'Fast:', fast
    otime = time.clock()
    slow = prj.slow_closest_pair(clus)
    diff = time.clock() - otime
    # print 'Slow:', slow
    slowtime = diff
    return (n, fasttime, slowtime)

import matplotlib.pyplot as plt
def main():
    x = []
    yfast = []
    yslow = []
    for n in range(2, 200, 1):
        times = compare_func(n)
        x.append(n)
        yfast.append(times[1])
        yslow.append(times[2])
    plt.plot(x, yfast, '-b', label='fast_closest_pair')
    plt.plot(x, yslow, '-r', label='slow_closest_pair')
    # ylinear = [i * yfast[0] for i in x]
    # yquad = [ylinear[i] * ylinear[i] for i in range(len(x))]
    # plt.loglog(x, ylinear, '-g', label='linear')
    # plt.loglog(x, yquad, '-y', label='quad')
    plt.legend(loc='upper left')
    plt.xlabel('num of initial clusters')
    plt.ylabel('running time (time.clock())')
    plt.title('Simple plot comparison of running times (desktop Python)')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
