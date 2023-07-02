from mygraph import MyGraph
from dfs import DFS
from johnson_simple_cycle import Johnson
from tajan_scc import Tarjan_SCC
from topology import Topology


if __name__ == "__main__":
    # Create graph using file
    f = open("input.txt", 'r')
    N = int(f.readline())
    g4 = MyGraph(N)
    for i in range(N):
        line = f.readline()
        edge =[int(x) for x in line.split()]
        g4.add_edge(edge[0], edge[1])

    print("input graph from file: ")
    print(g4.get_graph())

    # Create graph using API
    g1 = MyGraph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)

    g2 = MyGraph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)

    g3 = MyGraph(7)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 0)
    g3.add_edge(1, 3)
    g3.add_edge(1, 4)
    g3.add_edge(1, 6)
    g3.add_edge(3, 5)
    g3.add_edge(4, 5)

    g5 = MyGraph(5)
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    g5.add_edge(1, 4)
    g5.add_edge(2, 4)
    g5.add_edge(2, 3)

    print("Cycle detection using different algorithms:")

    print("DFS: ", end="\t\t")
    for g in [g1, g2, g3, g4, g5]:
        alg = DFS(g)
        print(alg.detect_loop(), end = " ")
    print("")

    print("Topology: ", end=" \t")
    for g in [g1, g2, g3, g4, g5]:
        alg = Topology(g)
        print(alg.detect_loop(), end = " ")
    print("")

    print("Tajan: ", end=" \t")
    for g in [g1, g2, g3, g4, g5]:
        alg = Tarjan_SCC(g)
        print(alg.detect_loop(), end = " ")
    print("")

    print("Johnson: ", end=" \t")
    for g in [g1, g2, g3, g4, g5]:
        alg = Johnson(g)
        print(alg.detect_loop(), end = " ")
    print("")
