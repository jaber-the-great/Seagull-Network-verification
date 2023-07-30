# Topological sort based loop detection
# Input: number of vertices, list of edges
# Output: True/False




class Topology:
    def __init__(self):
        # Stack
        self.s = []
        # Store Topological Order
        self.tsort = []
        # To ensure visited vertex
        self.visited = set()
        self.graph = dict()
        self.nodes = set()


    def name(self):
        return ("Topology Sorting")

    def add_edge(self, u, v):
        self.nodes.add(u)
        self.nodes.add(v)
        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = [v]

    # Function to perform Topology
    def dfs(self, u):
        # Set the vertex as visited
        self.visited.add(u)

        try:
            for node in self.graph[u]:
                # Visit connected vertices
                if not node in self.visited:
                    self.dfs(node)
        except:
            pass

        # Push into the stack on
        # complete visit of vertex
        self.s.append(u)

    def detect_loop(self):
        # Stores the position of
        # vertex in topological order
        pos = dict()
        ind = 0

        for node in self.nodes:
            if not node in self.visited:
                self.dfs(node)

        # Pop all elements from stack
        while (len(self.s) != 0):
            pos[self.s[-1]] = ind

            # Push element to get
            # Topological Order
            self.tsort.append(self.s[-1])

            ind += 1

            # Pop from the stack
            self.s.pop()

        for i in self.nodes:
            try:
                for it in self.graph[i]:
                    first = 0 if i not in pos else pos[i]
                    second = 0 if it not in pos else pos[it]

                    # If parent vertex
                    # does not appear first
                    if first > second:
                        # Cycle exists
                        return True
            except:
                pass

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

    alg = Topology(g1)
    print("Loop in first graph ")
    print(alg.detect_loop())

    g2 = MyGraph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)

    alg = Topology(g2)
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

    alg = Topology(g3)
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

    alg = Topology(g4)
    print("Loop in fourth graph ")
    print(alg.detect_loop())

    g5 = MyGraph(5)
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    g5.add_edge(1, 4)
    g5.add_edge(2, 4)
    g5.add_edge(2, 3)

    alg = Topology(g5)
    print("Loop in fifth graph ")
    print(alg.detect_loop())
