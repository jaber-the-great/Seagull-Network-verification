# Loop detection using DSU
# Input: number of vertices, list of edges
# Output: True/False
# M.Y @UCSB RMP 23

from collections import defaultdict
from mygraph import *
from collections import deque

class optimized_dsu:
    def __init__(self, n):
        self.parent=[v for v in range(n+1)]
    def find(self,v):
        if self.parent[v] == v:
            return v

        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def join(self,a,b):
        #p_a = self.find(a)
        #p_b = self.find(b)

        #if p_a != p_b:
        self.parent[a] = b

class DSU:
    def load_file(self, file):
        f = open(file, "r")
        self.lines = f.readlines()

    def detect_loop(self):
        self.edges = []
        self.dsu = optimized_dsu(int(1e6))
        for line in self.lines:
            edge = [int(x) for x in line.split()]
            p0 = self.dsu.find(edge[0])
            p1 = self.dsu.find(edge[1])

            if p0 == p1:
                return True
            else:
                self.dsu.join(p0, p1)

        return False