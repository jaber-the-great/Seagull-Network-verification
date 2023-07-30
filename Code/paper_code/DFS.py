# DFS for loop detection
# Input: number of vertices, list of edges
# Output: True/False


from collections import defaultdict


class DFS:
    def __init__(self):
        # To ensure visited vertex
        self.visited = set()
        self.stack = set()

        self.graph = dict()
        self.nodes = set()


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

