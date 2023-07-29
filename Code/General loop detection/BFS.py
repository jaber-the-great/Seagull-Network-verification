#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Purpose: BFS for cycle detection in directed graphs
Input: # of vertices, adjacency list
Output: binary
Name: Sucheer Maddury, Leland High School, CA
@UCSB RMP '23
'''

import math
import sys
from mygraph import *
from collections import defaultdict


# In[16]:


class BFS:
    def __init__(self, mygraph):
        self.graph = mygraph.get_graph()
        self.V = len(self.graph)
        self.indegree = {v: 0 for v in range(self.V)}
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def indegree_calc(self):
        # Calculates indegree, or the number of incoming edges for each vertex/node
        for key in self.graph:
            for dest in self.graph[key]:
                self.indegree[dest]+=1
    def detect_loop(self):
        self.indegree_calc()
        
        # Adds all zero-indegree vertexes to a queue
        queue=[]
        for i in range(len(self.indegree)):
            if self.indegree[i]==0:
                queue.append(i)
        
        '''
        Iteratively removes vertexes/nodes from a queue and:
        - Adds 1 to # of visited nodes
        - Decreases indegree by 1 for all neighboring nodes
        - Adds any new zero-indegree nodes to the queue
        '''
        cnt=0
        while(queue):
            nu=queue.pop(0)
            for v in self.graph[nu]:
                self.indegree[v]-=1
                if self.indegree[v]==0:
                    queue.append(v)
            cnt+=1
            
        # If # of visited nodes != # of total nodes, the graph has a cycle
        if cnt==self.V:
            return False
        else:
            return True

