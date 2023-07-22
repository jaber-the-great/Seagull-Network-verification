#!/usr/bin/env python
# coding: utf-8

# In[59]:


from tinysmpc.tinysmpc.tinysmpc import VirtualMachine, PrivateScalar, SharedScalar
from tinysmpc.tinysmpc.secret_sharing import Share
from equality_check import equal_to
from collections import defaultdict, deque
from copy import deepcopy


# In[69]:


def secure_bfs(edge_list, destination_node):

    # Build a reversed adjacency list for the graph
    rev_adj_list = defaultdict(list)
    incoming_count = defaultdict(int)

    for u, v in edge_list:
        rev_adj_list[v].append(u)  # Reverse the direction of the edges
        incoming_count[u] += 1

    queue = [destination_node]  # Start BFS from the destination node

    while queue:
        current_node = queue.pop(0)

        for neighbor in rev_adj_list[current_node]:
            incoming_count[neighbor] -= 1
            if incoming_count[neighbor] == 0:
                queue.append(neighbor)

    return any(incoming_count[node] > 0 for node in rev_adj_list)

def secure_bfs_with_decrypted_destination_nodes(edge_list, destination_node):

    # Build a reversed adjacency list for the graph
    rev_adj_list = defaultdict(list)
    incoming_count = defaultdict(int)

    for u, v in edge_list:
        rev_adj_list[v].append(u)  # Reverse the direction of the edges
        incoming_count[u] += 1

    for edge in edge_list:
        if equal_to(edge[1], destination_node):
            queue = [edge[1]]  # Start BFS from the destination node
            break

    while queue:
        current_node = queue.pop(0)

        for neighbor in rev_adj_list[current_node]:
            incoming_count[neighbor] -= 1
            if incoming_count[neighbor] == 0:
                queue.append(neighbor)

    return any(incoming_count[node] > 0 for node in rev_adj_list)

def create_nodes(count):
    machines = []
    numbers = []
    for i in range(count):
        machines.append(VirtualMachine(str(i+1)))
        numbers.append(PrivateScalar(i+1, machines[i]))
    return machines, numbers

def create_private_edge_list(edges, numbers):
    private_edge_list = []
    for edge in edges:
        tmp = []
        tmp.append(numbers[edge[0]-1])
        tmp.append(numbers[edge[1]-1])
        private_edge_list.append(tuple(tmp))
        
    return private_edge_list

def create_shared_edge_list(private_edge_list, computers):
    p_s_list = {}
    edge_list = []
    for edge in private_edge_list:
        tmp = []
        for node in edge:
            if not node in p_s_list:
                p_s_list[node] = node.share(computers)
                tmp.append(p_s_list[node])
            else:
                tmp.append(p_s_list[node])
        edge_list.append(tuple(tmp))
    
    return edge_list, p_s_list

def create_private_test(test, numbers):
    private_test = []
    for question in test:
        tmp = []
        tmp.append(create_private_edge_list(question[0], numbers))
        tmp.append(numbers[question[1]-1])
        private_test.append(tuple(tmp))
    
    return private_test

def create_shared_test(private_test, computers):
    shared_test = []
    for question in private_test:
        tmp = []
        s_question, p_s_list = create_shared_edge_list(question[0], computers)
        tmp.append(s_question)
        tmp.append(p_s_list[question[1]])
        shared_test.append(tuple(tmp))
    
    return shared_test

def test_alg(algorithm, test, answers):
    res = []
    for question in test:
        res.append(algorithm(question[0], question[1]))
    return res, answers

def decrypt_destination_nodes(shared_test, test):
    modified_shared_test = []
    for i in range(len(shared_test)):
        tmp = []
        tmp.append(deepcopy(shared_test[i][0]))
        tmp.append(test[i][1])
        modified_shared_test.append(tuple(tmp))

    return modified_shared_test


# In[40]:
if __name__ == "__main__":

    machines, numbers = create_nodes(6)

    c1 = VirtualMachine("c1")
    c2 = VirtualMachine("c2")
    comps = (c1, c2)

    test = [
        ([(1, 2), (2, 3), (3, 4), (3, 1)], 4),
        ([(1, 2), (2, 3), (3, 4), (1, 3)], 4),
        ([(1, 2), (2, 3)], 3),
        ([(1, 2), (1, 5), (5, 6), (6, 1), (2, 3), (3, 4)], 4),
        ([(1, 2), (2, 3), (3, 4), (4, 5)], 5),
        ([(1, 2), (2, 3), (3, 4), (4, 5), (1, 3)], 5),
        ([(1, 2), (2, 3), (3, 4), (4, 5), (3, 1)], 5),
       ]
    answers = (True, False, False, True, False, False, True)

    print(test_alg(secure_bfs, test, answers))

    private_test = create_private_test(test, numbers)
    shared_test = create_shared_test(private_test, comps)


    print(test_alg(secure_bfs, shared_test, answers))

    modified_shared_test = decrypt_destination_nodes(shared_test, test)

    print(test_alg(secure_bfs_with_decrypted_destination_nodes, modified_shared_test, answers))

