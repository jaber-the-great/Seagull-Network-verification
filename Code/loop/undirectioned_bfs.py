# DFS for loop detection
# Input: number of vertices, list of edges
# Output: True/False
# M.Y @UCSB RMP 23

from collections import defaultdict
from mygraph import *
from collections import deque

class Undirected_BFS:
    def __init__(self, mygraph):
        self.graph = mygraph.get_graph()
        self.nodes = mygraph.get_nodes()
        self.visited = set()
        self.parent = dict()

    def name(self):
        return ("Breadth First Search")

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        if not u in self.nodes:
            self.nodes.append(u)
        if not v in self.nodes:
            self.nodes.append(v)

    def bfs(self, node):
        q = deque()
        self.parent[node] = -1
        q.append(node)

        while q != []:
            u = q.pop()
            try:
                for v in self.graph[u]:
                    if not v in self.visited:
                        self.visited.add(v)
                        q.append(v)
                        self.parent[v] = u
                    elif self.parent[u] != v:
                        return True
            except:
                pass

        return False

    def detect_loop(self):
        for node in self.nodes:
            if not node in self.visited and self.bfs(node):
                return True

        return False

if __name__ == "__main__":
    g1 = MyGraph(5)
    g1.add_undirected_edge(1, 0)
    g1.add_undirected_edge(1, 2)
    g1.add_undirected_edge(2, 0)
    g1.add_undirected_edge(2, 3)

    alg = Undirected_BFS(g1)
    print("Loop in undirected graph ")
    print(alg.detect_loop())
