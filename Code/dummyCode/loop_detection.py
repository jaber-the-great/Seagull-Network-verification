import os
import time

from mygraph import MyGraph
from dfs import DFS
from johnson_simple_cycle import Johnson
from tajan_scc import Tarjan_SCC
from topology import Topology
from undirectioned_bfs import Undirected_BFS
from dsu import DSU

def load_graph(file):
    f = open(file, 'r')
    lines = f.readlines()
    edges = set()
    nodes = set()
    for line in lines:
        if (line.startswith("D")):
            ll = line.split()
            if len(ll) < 2:
                continue
            edges.add((ll[1], ll[2]))
            nodes.add(ll[1])
            nodes.add(ll[2])
    #print(len(edges))
    num_nodes = len(nodes)
    g = MyGraph(num_nodes)
    for st, ed in edges:
        g.add_edge(st, ed)
    return g

def benchmark(alg):
    rounds = 10
    for round in range(rounds):
        t1 = time.time()
        result = alg.detect_loop()
        t2 = time.time()
        t = (t2 - t1) / rounds
    return result, f"{t:0,.8f}"

def benchmark2(file):
    rounds = 10
    dsu = DSU()
    dsu.load_file(file)

    for round in range(rounds):
        t1 = time.time()
        result = dsu.detect_loop()
        t2 = time.time()
        t = (t2 - t1) / rounds
    return result, f"{t:0,.8f}"

if __name__ == "__main__":
    # Create graph using file
    for file in os.listdir("data/"):
        if not file.endswith("txt"):
            continue

        test_file = "data/" + file
        print("test using file ",  file)

        g = load_graph(test_file)

        alg = Topology(g)
        print("\tTopology Sort: ", end = " ")
        result, runtime = benchmark(alg)
        print("\t\t result = ", result, " time = ", runtime, " second", end = " ")
        print("")


        alg = DFS(g)
        print("\t\t\tDFS:   ", end = " ")
        result, runtime = benchmark(alg)
        print("\t\t result = ", result, " time = ", runtime, " second", end = " ")
        print("")

        alg = Undirected_BFS(g)
        print("\tBFS (undirected): ", end = " ")
        result, runtime = benchmark(alg)
        print("\t\t result = ", result, " time = ", runtime, " second", end=" ")
        print("")


        alg = Tarjan_SCC(g)
        print("\t\tTarjan SCC: ", end = " ")
        result, runtime = benchmark(alg)
        print("\t\t result = ", result, " time = ", runtime, " second", end=" ")
        print("")


        alg = Johnson(g)
        print("\tJohn's algorithm: ", end = " ")
        result, runtime = benchmark(alg)
        print("\t\t result = ", result, " time = ", runtime, " second", end=" ")
        print("")

