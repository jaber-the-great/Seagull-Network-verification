import random

def generate_edge_list(num_nodes, num_edges):
    edges = set()

    # Generate random edges until the desired number of edges is reached
    while len(edges) < num_edges:
        node1 = random.randint(1, num_nodes)
        node2 = random.randint(1, num_nodes)

        # Ensure the edge is unique and not a self-loop
        if node1 != node2 and (node1, node2) not in edges and (node2, node1) not in edges:
            edges.add((node1, node2))

    return edges

def write_edge_list_to_file(edge_list, filename):
    with open(filename, 'w') as file:
        for edge in edge_list:
            file.write(f"{edge[0]} {edge[1]}\n")

# Generate edge list for approximately 300 nodes and 200 edges
num_nodes = 300
num_edges = 400
edge_list = generate_edge_list(num_nodes, num_edges)

# Write the edge list to an output file
output_file_name = "data/test_edge_list1.txt"
write_edge_list_to_file(edge_list, output_file_name)

print(f"Edge list data written to the file '{output_file_name}'.")


# Generate edge list for approximately 300 nodes and 200 edges
num_nodes = 800
num_edges = 1200
edge_list = generate_edge_list(num_nodes, num_edges)

# Write the edge list to an output file
output_file_name = "data/test_edge_list2.txt"
write_edge_list_to_file(edge_list, output_file_name)

print(f"Edge list data written to the file '{output_file_name}'.")
