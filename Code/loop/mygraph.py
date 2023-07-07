# Simple Graph
# Input: number of vertices, add edges
# Output: adj based graph
# Questions contact: ocmelodyyu@gmail.com

class MyGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {v: dict() for v in range(self.V)}
        self.nodes = []

    def add_edge(self, u, v):
        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = [v]

        if not u in self.nodes:
            self.nodes.append(u)
        if not v in self.nodes:
            self.nodes.append(v)

    def add_undirected_edge(self, u, v):
        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = [v]

        try:
            self.graph[v].append(u)
        except:
            self.graph[v] = [u]

        if not u in self.nodes:
            self.nodes.append(u)
        if not v in self.nodes:
            self.nodes.append(v)

    def add_node(self, n):
        self.nodes.append(n)

    def get_graph(self):
        return self.graph

    def get_nodes(self):
        return self.nodes

    def load_directed_graph(self, file):
        f = open(file, 'r')
        self.V = 1#int(f.readline())
        self.graph = {v: dict() for v in range(self.V)}

        line = f.readline()
        while line:
            edge = [int(x) for x in line.split()]
            self.add_edge(edge[0], edge[1])
            self.add_node(edge[0])
            self.add_node(edge[1])
            line = f.readline()

    def load_undirected_graph(self, file):
        f = open(file, 'r')
        self.V = 1
        self.graph = {}

        line = f.readline()
        while line:
            edge = [int(x) for x in line.split()]
            self.add_undirected_edge(edge[0], edge[1])
            line = f.readline()