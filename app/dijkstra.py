import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
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
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    
    #Define maximum distance EV can drive in miles
    max_ev_driving_dist = 150 #in miles
    
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    #Reverse the path to be from start to finish
    proper_path = list(reversed(path))
    
    #Define the distance EV drives after last charge
    running_dist = 0 #in miles
    
    #Define the emptry array to hold cities and charging locations
    path_with_charging = []
    
    #Iterate over cities to determine where to charge the EV
    #based on the running driving distance
    for ii, city in enumerate(proper_path):
        #First city
        if ii == 0:
            #Define start city, end city, and find distances between them
            start_city = proper_path[ii]
            end_city = proper_path[ii+1]
            path_with_charging.append(start_city)
            dist = init_graph[start_city][end_city]
            #Add distance to running distance
            running_dist += dist
        #All other cities
        elif ii + 1 <= len(proper_path) and ii != 0:
            #Define start city, end city, and find distances between them
            start_city = proper_path[ii-1]
            end_city = proper_path[ii]
            dist = init_graph[start_city][end_city]
            #Add distance to running distance
            running_dist += dist
            #If the running distance is higher than
            #maximum EV driving distance charge the car
            if running_dist >=  max_ev_driving_dist:
                path_with_charging.append(end_city)
                path_with_charging.append('Charge Car')
                running_dist = 0
            #If the running distance is not higher than
            #maximum EV driving distance do not charge yet
            else:
                path_with_charging.append(end_city)
                running_dist += dist
    
    return path_with_charging

cities_location = {
    'Portsmouth' : {'lat': 50.798908, 'lon': -1.091160},
    'Brighton' : {'lat': 50.822529, 'lon': -0.137163},
    'Southampton' : {'lat': 50.904968, 'lon': -1.403230},
    'Cardiff' : {'lat': 51.481312, 'lon': -3.1833},
    'Bristol' : {'lat': 51.4500, 'lon': -2.5833},
    'London' : {'lat': 51.5072, 'lon': -0.1275},
    'Oxford' : {'lat': 51.7519, 'lon': -1.2578},
    'Cambridge' : {'lat': 52.205276, 'lon': 0.119167},
    'Birmingham' : {'lat': 52.48, 'lon': -1.9025},
    'Leicester' : {'lat': 52.6333, 'lon': -1.1333},
    'Sheffield' : {'lat': 53.3833, 'lon': -1.4667},
    'Manchester' : {'lat': 53.4794, 'lon': -2.2453},
    'Liverpool' : {'lat': 53.4, 'lon': -2.9833},
    'Leeds' : {'lat': 53.7997, 'lon': -1.5492},
    'Norwich' : {'lat': 52.63, 'lon': 1.297},
    'Hull' : {'lat': 53.767750, 'lon': -0.335827},
    'Nottingham' : {'lat': 52.95, 'lon': -1.15},
}

cities = list(cities_location.keys())

init_graph = {}
for city in cities:
    init_graph[city] = {}
    
#All distances in miles    
init_graph['Portsmouth']['Southampton'] = 19.5
init_graph['Southampton']['Portsmouth'] = 19.5

init_graph['Portsmouth']['Brighton'] = 51.5
init_graph['Brighton']['Portsmouth'] = 51.5

init_graph['Portsmouth']['London'] = 73.7
init_graph['London']['Portsmouth'] = 73.7

init_graph['Southampton']['London'] = 76.2
init_graph['London']['Southampton'] = 76.2

init_graph['Brighton']['London'] = 53.4
init_graph['London']['Brighton'] = 53.4

init_graph['Bristol']['London'] = 126
init_graph['London']['Bristol'] = 126

init_graph['Oxford']['London'] = 56.4
init_graph['London']['Oxford'] = 56.4

init_graph['Oxford']['Birmingham'] = 77.9
init_graph['Birmingham']['Oxford'] = 77.9

init_graph['Cambridge']['London'] = 58
init_graph['London']['Cambridge'] = 58

init_graph['Cambridge']['Norwich'] = 64.1
init_graph['Norwich']['Cambridge'] = 64.1

init_graph['Cambridge']['Leicester'] = 71.7
init_graph['Leicester']['Cambridge'] = 71.7

init_graph['Nottingham']['Leicester'] = 27.3
init_graph['Leicester']['Nottingham'] = 27.3

init_graph['Nottingham']['Sheffield'] = 38.8
init_graph['Sheffield']['Nottingham'] = 38.8

init_graph['Leeds']['Sheffield'] = 35.5
init_graph['Sheffield']['Leeds'] = 35.5

init_graph['Leeds']['Hull'] = 62.2
init_graph['Hull']['Leeds'] = 62.3

init_graph['Leeds']['Manchester'] = 42.2
init_graph['Manchester']['Leeds'] = 42.2

init_graph['Sheffield']['Manchester'] = 38
init_graph['Manchester']['Sheffield'] = 38

init_graph['Liverpool']['Manchester'] = 34.3
init_graph['Manchester']['Liverpool'] = 34.3

init_graph['Birmingham']['Cardiff'] = 116
init_graph['Cardiff']['Birmingham'] = 116

init_graph['Birmingham']['Nottingham'] = 52
init_graph['Nottingham']['Birmingham'] = 52

init_graph['Birmingham']['Liverpool'] = 99
init_graph['Liverpool']['Birmingham'] = 99

graph = Graph(cities, init_graph)
    