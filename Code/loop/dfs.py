# DFS for loop detection
# Input: number of vertices, list of edges
# Output: True/False
# M.Y @UCSB RMP 23

from collections import defaultdict
from mygraph import *

class DFS:
    def __init__(self, mygraph):
        self.graph = mygraph.get_graph()
        self.V = len(self.graph)
        # To ensure visited vertex
        self.visited = set()
        self.nodes = mygraph.get_nodes()
        self.stack = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not u in self.nodes:
            self.nodes.append(u)
        if not v in self.nodes:
            self.nodes.append(v)

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



if __name__ == "__main__":
    # Create a graph given in the above diagram
    g1 = MyGraph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)

    alg = DFS(g1)
    print("Loop in first graph ")
    print(alg.detect_loop())

    g2 = MyGraph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)

    alg = DFS(g2)
    print("Loop in second graph ")
    print(alg.detect_loop())

    g3 = MyGraph(7)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 0)
    g3.add_edge(1, 3)
    g3.add_edge(1, 4)
    g3.add_edge(1, 6)
    g3.add_edge(3, 5)
    g3.add_edge(4, 5)

    alg = DFS(g3)
    print("Loop in third graph ")
    print(alg.detect_loop())

    g4 = MyGraph(11)
    g4.add_edge(0, 1)
    g4.add_edge(0, 3)
    g4.add_edge(1, 2)
    g4.add_edge(1, 4)
    g4.add_edge(2, 0)
    g4.add_edge(2, 6)
    g4.add_edge(3, 2)
    g4.add_edge(4, 5)
    g4.add_edge(4, 6)
    g4.add_edge(5, 6)
    g4.add_edge(5, 7)
    g4.add_edge(5, 8)
    g4.add_edge(5, 9)
    g4.add_edge(6, 4)
    g4.add_edge(7, 9)
    g4.add_edge(8, 9)
    g4.add_edge(9, 8)

    alg = DFS(g4)
    print("Loop in fourth graph ")
    print(alg.detect_loop())

    g5 = MyGraph(5)
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    g5.add_edge(1, 4)
    g5.add_edge(2, 4)
    g5.add_edge(2, 3)

    alg = DFS(g5)
    print("Loop in fifth graph ")
    print(alg.detect_loop())
