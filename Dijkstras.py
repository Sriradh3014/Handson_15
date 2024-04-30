import heapq

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.distance = float('inf')
        self.previous = None

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}

    def add_edge(self, edge):
        self.adjacency_list[edge.start].append((edge.end, edge.weight))

def dijkstra(graph, start):
    start.distance = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > current_vertex.distance:
            continue
        
        for neighbor, weight in graph.adjacency_list[current_vertex]:
            distance = current_distance + weight
            if distance < neighbor.distance:
                neighbor.distance = distance
                neighbor.previous = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    distances = {vertex.label: vertex.distance for vertex in graph.vertices}
    sorted_distances = sorted(distances.items(), key=lambda item: item[1])
    
    print(f"Shortest distances from vertex {start.label}:")
    [print(f"Vertex {vertex}: Distance {distance}") for vertex, distance in sorted_distances]

vertices = [Vertex(i) for i in range(5)]
edges = [Edge(vertices[0], vertices[1], 10),
         Edge(vertices[0], vertices[3], 5),
         Edge(vertices[1], vertices[2], 1),
         Edge(vertices[1], vertices[3], 2),
         Edge(vertices[2], vertices[4], 4),
         Edge(vertices[3], vertices[1], 3),
         Edge(vertices[3], vertices[2], 9),
         Edge(vertices[3], vertices[4], 2),
         Edge(vertices[4], vertices[0], 7),
         Edge(vertices[4], vertices[2], 6)]

graph = Graph(vertices)
[graph.add_edge(edge) for edge in edges]

start_vertex = vertices[0]
dijkstra(graph, start_vertex)

'''OUTPUT-----
Shortest distances from vertex 0:
Vertex 0: Distance 0
Vertex 3: Distance 5
Vertex 4: Distance 7
Vertex 1: Distance 8
Vertex 2: Distance 9'''