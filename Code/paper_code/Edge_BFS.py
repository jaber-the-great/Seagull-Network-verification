# DFS for loop detection
# Input: number of vertices, list of edges
# Output: True/False


class Edge_BFS:
    def __init__(self, end_node):
        self.edges = []
        self.end_node = end_node

    def name(self):
        return("Breadth First Search")

    def add_edge(self, u, v):
        self.edges.append([u, v])

    def detect_loop(self):
        found_new_node = True
        starting_node = self.edges[-1][1]
        visited = set()
        visited.add(self.end_node)

        nodes = set()
        for e in self.edges:
            nodes.add(e[0])
            nodes.add(e[1])

        while found_new_node:
            found_new_node = False
            for e in self.edges:
                if e[1] in visited and not e[0] in visited:
                    found_new_node = True
                    visited.add(e[0])

        if len(visited) == len(nodes):
            return False
        else:
            return True