# Directory for the source code

### Loop detection code:
* Put all of the source code in a new directory called loop
* Use proper commenting/docstrings for explaining your code
* Define the input and output format of the code

## Implemented algorithms in python:
1. BFS
2. DFS
3. Union-Find
4. Floyd Warshall
5. Tarjan’s
6. Floyd’s Tortoise and Hare 
7. Topological sort
8. Johnson’s 

## Algorithm specification:
### Input:
* First line: N, number of nodes in the graph
* Following lines: two space separated numbers representing and edge in the graph
* In case of forwarding graph: Number of edges = N -1 

### Algorithm specification:
* We do not represent the graph using linkedlist, matrix or adjacency list due to limitations of Multi-Party Computation 
* We may not need to use conventional graph loop detection in our algorithm:
  * If our forwarding graph is loop free(it is a tree), then we have 1 connected component

### Output:
* Stop the algorithm when the loop is detected (eg do not need to discover all of the nodes in BFS if you detect a loop)
* Output is true or false 