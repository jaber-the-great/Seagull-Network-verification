# DFS for loop detection
# Input: number of vertices, list of edges
# Output: True/False
# M.Y @UCSB RMP 23

from collections import defaultdict
from mygraph import *

class DFS:
    def __init__(self, mygraph = None):
        # To ensure visited vertex
        self.visited = set()
        self.stack = set()

        if mygraph == None:
            self.graph = dict()
            self.nodes = set()
        else:
            self.graph = mygraph.get_graph()
            self.nodes = mygraph.get_nodes()

    def name(self):
        return ("Depth First Search")

    def add_edge(self, u, v):
        self.nodes.add(u)
        self.nodes.add(v)
        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = [v]

    # Function to perform DFS
    def dfs(self, u):
        # Set the vertex as visited
        self.visited.add(u)
        self.stack.add(u)

        try:
            for node in self.graph[u]:
                # Visit connected vertices
                if not node in self.visited:
                    if self.dfs(node):
                        return True

                elif node in self.stack:
                    return True
        except:
            pass

        # Push into the stack on
        # complete visit of vertex
        self.stack.remove(u)
        return False

    def detect_loop(self):
        for node in self.nodes:
            if not node in self.visited:
                if self.dfs(node):
                    return True

        # Return false if cycle
        # does not exist
        return False

