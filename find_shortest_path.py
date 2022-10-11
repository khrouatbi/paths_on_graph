import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):

        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # Use this dict to save the cost of visiting each node    
    shortest_path = {}
 
    # Shortest known path to a node found so far stored here
    previous_nodes = {}
 
    # max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        # Finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: 
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # the current node's neighbors and update their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))



nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}
    
init_graph["B"]["C"] = 1
init_graph["B"]["D"] = 1
init_graph["B"]["A"] = 1

init_graph["A"]["B"] = 1
init_graph["A"]["D"] = 1
init_graph["A"]["H"] = 1

init_graph["C"]["B"] = 1
init_graph["C"]["D"] = 1
init_graph["C"]["F"] = 1

init_graph["D"]["A"] = 1
init_graph["D"]["E"] = 1
init_graph["D"]["C"] = 1
init_graph["D"]["B"] = 1

init_graph["F"]["C"] = 1
init_graph["F"]["E"] = 1
init_graph["F"]["G"] = 1

init_graph["E"]["F"] = 1
init_graph["E"]["D"] = 1
init_graph["E"]["H"] = 1

init_graph["G"]["F"] = 1
init_graph["G"]["H"] = 1

init_graph["H"]["E"] = 1
init_graph["H"]["A"] = 1
init_graph["H"]["G"] = 1

graph = Graph(nodes, init_graph)

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="A")


#modify start node and target node in function here
print_result(previous_nodes, shortest_path, start_node="A", target_node="H")
