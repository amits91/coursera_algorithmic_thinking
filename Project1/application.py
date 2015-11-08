'''
Algorithmic Thinking
Code for Application 1
'''
__author__ = 'asrivas'
import degrees
import random_graph as rndgraph
import parse_graph as citation
import matplotlib.pyplot as plt
import dpa

def create_loglog_plot(dist, marker='x', color='red', label=''):
    '''
    :param dist: in degree distribution of directed graph
    :param marker: distinguishing marker
    :param label: label corresponding to the graph
    :return:
    '''
    plt.xlabel('in-degrees')
    plt.ylabel('Distribution')
    plt.title('LogLog plot of in-degree distribution')
    plt.grid(True)
    plt.loglog(dist.keys(), dist.values(), basex=2, basey=2, linestyle='None',
               marker=marker, markeredgecolor=color, label=label)

def create_simple_plot(dist, marker='x', color='red', label=''):
    '''
    :param dist: in degree distribution of directed graph
    :param marker: distinguishing marker
    :param label: label corresponding to the graph
    :return:
    '''
    plt.xlabel('in-degrees')
    plt.ylabel('Distribution')
    plt.title('simple plot of in-degree distribution')
    plt.plot(dist.keys(), dist.values(), linestyle='none',
               marker=marker, markeredgecolor=color, label=label)



citation_graph = citation.load_graph(citation.CITATION_URL)
citation_dist = degrees.norm_in_deg_dist(citation_graph)

create_loglog_plot(citation_dist, label='Citation')
# create_simple_plot(citation_dist, label='Citation')

# rnd_er_dist = degrees.norm_in_deg_dist(rndgraph.generate_random_directed_graph(2700, 0.06))
# # create_simple_plot(rnd_er_dist, marker='o', color='blue', label='Random ER')
# create_loglog_plot(rnd_er_dist, marker='o', color='blue', label='Random ER')

dpa_dist = degrees.norm_in_deg_dist(dpa.newDPA(27770, 14))
create_loglog_plot(dpa_dist, marker='.', color='green', label='DPA graph')

# dpa_dist = degrees.norm_in_deg_dist(dpa.DPA(27770, 14))
# create_loglog_plot(dpa_dist, marker='x', color='blue', label='old DPA graph')


plt.legend(loc='upper right')
plt.show()
# print degrees.print_info(citation.citation_graph)
