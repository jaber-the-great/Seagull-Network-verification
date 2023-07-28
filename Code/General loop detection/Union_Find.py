#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Purpose: Union-Find for cycle detection in directed graphs
Input: # of vertices, adjacency list
Output: binary
Name: Sucheer Maddury, Leland High School, CA
@UCSB RMP '23
'''

import math
import sys
from mygraph import *
from collections import defaultdict


# In[2]:


# Adapted from GeeksforGeeks
class UnionFind:
    def __init__(self, mygraph):
        self.graph = mygraph.get_graph()
        self.V = len(self.graph)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def find_parent(self, parent, i):
        # Finds subset of some element i via recursion
        if parent[i] == i:
            return i
        if parent[i] != i:
            return self.find_parent(parent, parent[i])
 
    def union(self, parent, x, y):
        # Unionizes of two subsets
        parent[x] = y
 
    def detect_loop(self):
 
        # Begins all subsets as single element sets
        parent = [0] * (self.V)
        for i in range(self.V):
            parent[i] = i
 
        # Iteratively goes through all edges and finds subsets of both nodes of each edge: If both subsets ==, cycle exists
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
        return False

