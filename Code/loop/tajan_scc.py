# Johnson's algorithm for finding simple loops
# Original code from https://github.com/qpwo/python-simple-cycles/blob/master/johnson.py
# Add graph data structure and wrapped the code inside a Python class

# Input: number of vertices, list of edges
# Output: True/False
# Questions contact: ocmelodyyu@gmail.com

from collections import defaultdict
from mygraph import *

class Tarjan_SCC:
    def __init__(self, mygraph):
        # make a copy of the graph
        self.graph =  mygraph.get_graph()

    def dfs(self, node):
        self.index[node] = self.index_counter[0]
        self.lowlink[node] = self.index_counter[0]
        self.index_counter[0] += 1
        self.stack.append(node)

        try:
            successors = self.graph[node]
            for successor in successors:
                if successor not in self.index:
                    self.dfs(successor)
                    self.lowlink[node] = min(self.lowlink[node], self.lowlink[successor])
                elif successor in self.stack:
                    self.lowlink[node] = min(self.lowlink[node], self.index[successor])
        except:
            pass

        if self.lowlink[node] == self.index[node]:
            connected_component = []

            while True:
                successor = self.stack.pop()
                connected_component.append(successor)
                if successor == node: break
            self.result.append(connected_component[:])


    def loop_dfs(self, node):
        self.index[node] = self.index_counter[0]
        self.lowlink[node] = self.index_counter[0]
        self.index_counter[0] += 1
        self.stack.append(node)

        try:
            successors = self.graph[node]
            for successor in successors:
                if successor not in self.index:
                    if self.loop_dfs(successor):
                        return True

                    self.lowlink[node] = min(self.lowlink[node], self.lowlink[successor])
                elif successor in self.stack:
                    self.lowlink[node] = min(self.lowlink[node], self.index[successor])
        except:
            pass

        if self.lowlink[node] == self.index[node]:
            connected_component = []
            count = 0
            while True:
                successor = self.stack.pop()
                count += 1
                if count > 1:
                    return True
                connected_component.append(successor)
                if successor == node: break
            self.result.append(connected_component[:])

        return False

    def strongly_connected_components(self):
        self.index_counter = [0]
        self.stack = []
        self.lowlink = {}
        self.index = {}
        self.result = []
        for node in self.graph:
            if node not in self.index:
                self.dfs(node)

        return self.result

    def detect_loop(self):
        self.index_counter = [0]
        self.stack = []
        self.lowlink = {}
        self.index = {}
        self.result = []
        for node in self.graph:
            if node not in self.index:
                if self.loop_dfs(node):
                    return True

        return False
#tests
if __name__ == "__main__":
    # Create a graph given in the above diagram
    g1 = MyGraph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)

    alg = Tarjan_SCC(g1)
    print("Loop in first graph ")
    print(alg.strongly_connected_components())
    print(alg.detect_loop())

    g2 = MyGraph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)

    alg = Tarjan_SCC(g2)
    print("Loop in second graph ")
    print(alg.strongly_connected_components())
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

    alg = Tarjan_SCC(g3)
    print("Loop in third graph ")
    print(alg.strongly_connected_components())
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

    alg = Tarjan_SCC(g4)
    print("Loop in fourth graph ")
    print(alg.strongly_connected_components())
    print(alg.detect_loop())

    g5 = MyGraph(5)
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    g5.add_edge(1, 4)
    g5.add_edge(2, 4)
    g5.add_edge(2, 3)

    alg = Tarjan_SCC(g5)
    print("Loop in fifth graph ")
    print(alg.strongly_connected_components())
    print(alg.detect_loop())
