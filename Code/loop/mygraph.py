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

    def load_graph(self, file):
        f = open(file, 'r')
        self.V = int(f.readline())
        self.graph = {v: dict() for v in range(self.V)}
        for i in range(self.V):
            line = f.readline()
            edge = [int(x) for x in line.split()]
            self.add_edge(edge[0], edge[1])
