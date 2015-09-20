'''
Algorithmic Thinking
Code for Application 1
'''
__author__ = 'asrivas'
import degrees
import random_graph as rndgraph
import parse_graph as citation
import matplotlib.pyplot as plt

norm_in_deg_dist = degrees.norm_in_deg_dist(citation.citation_graph)

plt.xlabel('in-degrees')
plt.ylabel('Distribution')
plt.title('LogLog graph of in-degree distribution')

plt.loglog(norm_in_deg_dist.keys(), norm_in_deg_dist.values(), basex=2, basey=2, linestyle='None',
           marker='x', markeredgecolor='red', label='Citation Graph')
plt.legend(loc='upper right')
plt.show()
# print degrees.print_info(citation.citation_graph)
