from mygraph import MyGraph
from dfs import DFS
from johnson_simple_cycle import Johnson
from tajan_scc import Tarjan_SCC
from topology import Topology


if __name__ == "__main__":
    # Create test graphs
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