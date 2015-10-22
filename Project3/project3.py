"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster



######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    min_dist = (float("inf"), -1, -1)
    for uidx in range(len(cluster_list)):
        for vidx in range(len(cluster_list)):
            if uidx == vidx:
                continue
            dist = pair_distance(cluster_list, uidx, vidx)
            min_dist = min(min_dist, dist)
    return min_dist



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    if len(cluster_list) <= 3:
        mind = slow_closest_pair(cluster_list)
    else:
        mid = int(math.ceil(len(cluster_list) / 2.0))
        leftd = fast_closest_pair(cluster_list[0 : mid])
        rightd = fast_closest_pair(cluster_list[mid :])
        mind = min(leftd, (rightd[0], rightd[1] + mid, rightd[2] + mid))
        xm_1 = cluster_list[mid - 1].horiz_center()
        xmi = cluster_list[mid].horiz_center()
        midx = (xm_1 + xmi) / 2.0
        cps = closest_pair_strip(cluster_list, midx, mind[0])
        mind = min(cps, mind)
    return mind

def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """
    slist = []
    #cluster_list.sort(key = lambda cluster: cluster.horiz_center())
    # idd = {}
    for idx in range(len(cluster_list)):
        clus = cluster_list[idx]
        # idd[clus] = idx
        if abs(clus.horiz_center() - horiz_center) < half_width:
            slist.append((clus, idx))
    slist.sort(key = lambda cluster: cluster[0].vert_center())
    min_dist = (float("inf"), -1, -1)
    for uidx in range(len(slist) - 1):
        minv = min(uidx +3, len(slist) - 1)
        for vidx in range(uidx + 1, minv + 1):
            dist = pair_distance(cluster_list, slist[uidx][1], slist[vidx][1])
            min_dist = min(min_dist, dist)
    return min_dist

# print closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0),
#                      alg_cluster.Cluster(set([]), 1, 0, 1, 0),
#                      alg_cluster.Cluster(set([]), 2, 0, 1, 0),
#                      alg_cluster.Cluster(set([]), 3, 0, 1, 0)], 1.5, 1.0)

######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while len(cluster_list) > num_clusters:
        mind = fast_closest_pair(cluster_list)
        cluster_list[mind[1]].merge_clusters(cluster_list[mind[2]])
        cluster_list.remove(cluster_list[mind[2]])
    return cluster_list


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations

    return []

print fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0),
                         alg_cluster.Cluster(set([]), 1, 0, 1, 0)])

print fast_closest_pair([alg_cluster.Cluster(set([]), 0.32, 0.16, 1, 0),
                         alg_cluster.Cluster(set([]), 0.39, 0.4, 1, 0),
                         alg_cluster.Cluster(set([]), 0.54, 0.8, 1, 0),
                         alg_cluster.Cluster(set([]), 0.61, 0.8, 1, 0),
                         alg_cluster.Cluster(set([]), 0.76, 0.94, 1, 0)])

