""""
Topological sort
modified from https://www.geeksforgeeks.org/detect-cycle-in-directed-graph-using-topological-sort/
designed for cycle detection

Input: list of edges
Output: whether or not there is a cycle
"""


# Stack to store the visited vertices in the Topological Sort
s = []

# Store Topological Order
tsort = []

# To ensure visited vertex
visited = [False for _ in range(100001)]

# Function to perform DFS
def dfs(u, edges):
    # Set the vertex as visited
    visited[u] = True

    for it in edges:
        if it[0] == u:
            if not visited[it[1]]:
                dfs(it[1], edges)

    # Push into the stack on complete visit of vertex
    s.append(u)


# Function to check and return if a cycle exists or not
def check_cycle(edges):
    # Stores the position of vertex in topological order
    pos = dict()
    ind = 0

    # Pop all elements from stack
    while len(s) != 0:
        pos[s[-1]] = ind

        # Push element to get Topological Order
        tsort.append(s[-1])

        ind += 1

        # Pop from the stack
        s.pop()

    for edge in edges:
        a = edge[0]
        b = edge[1]
        first = pos[a] if a in pos else 0
        second = pos[b] if b in pos else 0

        # If parent vertex does not appear first
        if first > second:
            # Cycle exists
            return True

    # Return False if cycle does not exist
    return False


# Driver Code
if __name__ == "__main__":
    n = int(input())
    edges = [(tuple(map(int, input().split()))) for _ in range(n-1)]

    for i in range(n):
        if not visited[i]:
            dfs(i, edges)

    # If cycle exists
    if check_cycle(edges):
        print('Yes')
    else:
        print('No')
