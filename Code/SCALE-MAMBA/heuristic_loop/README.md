# Increamental approach for verifying network
* After initail verification using BFS or other loop detection algorithm, we don't need to perform all of the previous steps for detecting the loop when a change is applied to the network
* Increamental approach helps to reduce the cost of checking policies and making the system saclable
* Also, it eliminates the need to secretly share all of the graph information for each query

## Increamental verification
* When a nede X changes its next hop to destination D, it may result in loop/unreachability in the network
* This loop/reachability does not occure in the random parts of the graph
  * It would affect node X and the nodes that use node X to reach destination D (in other words, node X is their way point)
* If node X can reach to the destination following its next hop, it indicates that the destination is reachable by X and all of its predessessors and there is no loop in the graph
* * Otherwise, we can say that the new edge caused unreachability and loop in the system. 
