# Experiment using AS link snapshot to detect loops
# July, 25, 2023

import sys
import time

from dfs import DFS
from johnson_simple_cycle import Johnson
from tajan_scc import Tarjan_SCC
from topology import Topology
from edge_bfs import Edge_BFS
from dsu import DSU
import random

class As_Link_Graph:
    def __init__(self, file_name):
        self.file = file_name
        self.max_id = 1
        self.id_map = dict()
        self.edges = set()
        self.nodes = set()
        self.adj = dict()

    def generate_fib_graph(self, target_node):
        visited1 = []  # List to keep track of visited nodes.
        queue = []  # Initialize a queue
        FIB = []

        visited1.append(target_node)
        queue.append(target_node)

        while queue:
            s = queue.pop(0)
            # print (s, end = " ")
            if s in self.adj.keys():
                for neighbour in self.adj[s]:
                    # print("\t",neighbour )
                    if neighbour not in visited1:
                        tmp = [neighbour, s]
                        FIB.append(tmp)
                        visited1.append(neighbour)
                        queue.append(neighbour)

        return FIB

    def is_bidirectional_graph(self):
        cnt = 0
        for n in self.nodes:
            if not n in self.adj.keys():
                #print("node ", n, " has no neighbours")
                #cnt += 1
                continue
            for nbr in self.adj[n]:
                if not nbr in self.adj.keys() or not n in self.adj[nbr]:
                    print("node ", n, "neighour ", nbr, " does not have back edge")
                    cnt += 1
        return cnt == 0

# assign a unique id from node string
    def get_node_id(self, node):
        if not node in self.id_map.keys():
            n1 = self.max_id
            self.id_map[node] = self.max_id
            # print("assigned new node #", id_map[node], "to ", node)
            self.max_id += 1
        else:
            n1 = self.id_map[node]
        return n1

    def generate_as_link_graph(self):
        asfile = open(self.file, 'r')
        lines = asfile.readlines()

        #reset graph
        self.edges.clear()
        self.nodes.clear()
        self.adj.clear()

        for line in lines:
            if line.startswith('D'):
                vline = line.split()
                if len(vline) > 2:
                    n1 = self.get_node_id(vline[1])
                    n2 = self.get_node_id(vline[2])
                    if n1 == 65 and n2 == 3135:
                        print("found")
                    self.nodes.add(n1)
                    self.nodes.add(n2)

                    self.edges.add((n1, n2))
                    # create reversed edges for FIB alg
                    try:
                        self.adj[n2].append(n1)
                    except:
                        self.adj[n2] = [n1]

                    #bi-directional
                    self.edges.add((n2, n1))
                    # create reversed edges for FIB alg
                    try:
                        self.adj[n1].append(n2)
                    except:
                        self.adj[n1] = [n2]


    def get_stats(self):
        print("# of nodes:", len(self.nodes))
        print("# of edges:", len(self.edges))
        print("the graph is", "" if self.is_bidirectional_graph() else "not", "an undirected graph")
        print("max node # is", self.max_id - 1)


    def generate_random_nodes(self, count):
        random_nodes = []
        for i in range(count):
            random_nodes.append(random.randint(1, self.max_id))

        return random_nodes

def benchmark(alg, edges):
    rounds = 1
    t1 = time.time()
    for round in range(rounds):
        for e in edges:
            alg.add_edge(e[0], e[1])
    result = alg.detect_loop()
    t2 = time.time()
    t = (t2 - t1) / rounds
    return result, f"{t:0,.4f}"

def experiment001(file):
    asfile = open(file, 'r')
    lines = asfile.readlines()

    edges = []
    nodes = set()
    last_node = 0
    for line in lines:
        ll = line.split()
        nodes.add(ll[0])
        nodes.add(ll[1])
        last_node = int(ll[1])
        edges.append(list(map(int,ll)))

    print("nodes = ", len(nodes), " edges = ", len(lines))

    alg = Edge_BFS(last_node)
    print(alg.name() + ":", end=" ")
    result, runtime = benchmark(alg, edges)
    print("\t\t result = ", result, " time = ", runtime, " second", end=" ")
    print("")


    for ALG in [DSU, Topology, DFS, Tarjan_SCC, Johnson]:
        alg = ALG()
        print(alg.name() + ":", end=" ")
        result, runtime = benchmark(alg, edges)
        print("\t\t result = ", result, " time = ", runtime, "s", end=" ")
        print("")





def experiment(fib_graph_edges):
    alg = Edge_BFS(end_node)
    print(alg.name() + ":", end=" ")
    result, runtime = benchmark(alg, fib_graph_edges)
    print("\t\t result = ", result, " time = ", runtime, " second", end=" ")
    print("")

    for ALG in [DSU, Topology, DFS, Tarjan_SCC, Johnson]:
        alg = ALG()
        print(alg.name() + ":", end=" ")
        result, runtime = benchmark(alg, fib_graph_edges)
        print("\t\t result = ", result, " time = ", runtime, " second", end=" ")
        print("")



experiment001("data/280_AS_LCC_IPv6L.edgelist")
experiment001("data/1421_AS_LCC_Atlas.edgelist")
experiment001("data/test_edge_list1.txt")
experiment001("data/test_edge_list2.txt")

as_link_graph = As_Link_Graph('data/cycle-aslinks.l7.t1.c006274.20180101.txt')
as_link_graph.generate_as_link_graph()
as_link_graph.get_stats()

random_nodes = as_link_graph.generate_random_nodes(1)
for end_node in random_nodes:
    fib_graph_edges = as_link_graph.generate_fib_graph(end_node)
    print("fib graph len = ", len(fib_graph_edges))
    output = open('data/node-'+ str(end_node)+'-fib.edgelist', 'w')
    for e in fib_graph_edges:
        output.write(str(e[0]) + " " + str(e[1]) + '\n')
    output.close()
    experiment(fib_graph_edges)



    #print("node", end_node, "'s FIB", fib_graph)

