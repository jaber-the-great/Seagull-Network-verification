#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Purpose: Floyd Warshall for cycle detection in directed graphs
Input: # of vertices, adjacency list
Output: binary
Name: Sucheer Maddury, Leland High School, CA
@UCSB RMP '23
'''
import math
import sys
from mygraph import *
from collections import defaultdict


# In[4]:


class FloydWarshall:
    def __init__(self, mygraph):
        self.V = len(mygraph.graph)
        
        #row is source, column is destination
        #adjacency list is k, v: src, dest
        self.graph = [[9999999 for i in range(self.V)] for i in range(self.V)]
        for src in mygraph.graph:
            for dest in mygraph.graph[src]:
                self.graph[src][dest]=-1
            self.graph[src][src]=0
    def detect_loop(self):
        # NOTE: This algorithm is originally made for negative loop detection, I modified it for general loop detection
        dist=[[0 for i in range(self.V+1)]for j in range(self.V+1)]

        for i in range(self.V):
            for j in range(self.V):
                dist[i][j] = self.graph[i][j]

        for k in range(self.V):

            for i in range(self.V):


                for j in range(self.V):

                    if (dist[i][k] + dist[k][j] < dist[i][j]):
                            dist[i][j] = dist[i][k] + dist[k][j]

        for i in range(self.V):
            if (dist[i][i] < 0):
                return True

        return False


# In[5]:





# In[ ]:




