# Simple Graph
# Input: number of vertices, add edges
# Output: adj based graph
# Questions contact: ocmelodyyu@gmail.com

class MyGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {v: dict() for v in range(self.V)}

    def add_edge(self, u, v):
        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = [v]

    def get_graph(self):
        return self.graph

    def load_graph(file):
        return
