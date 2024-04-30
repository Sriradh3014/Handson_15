class Vertex:
    def __init__(self, label):
        self.label = label
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
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

def bellman_ford(graph, start):
    start.distance = 0

    for _ in range(len(graph.vertices) - 1):
        for edge in graph.edges:
            if edge.start.distance + edge.weight < edge.end.distance:
                edge.end.distance = edge.start.distance + edge.weight
                edge.end.previous = edge.start

    for edge in graph.edges:
        if edge.start.distance + edge.weight < edge.end.distance:
            raise ValueError("Graph contains a negative-weight cycle")

    distances = {vertex.label: vertex.distance for vertex in graph.vertices}
    return distances

vertices = [Vertex(i) for i in range(5)]
edges = [Edge(vertices[0], vertices[1], 6),
         Edge(vertices[0], vertices[3], 7),
         Edge(vertices[1], vertices[2], 5),
         Edge(vertices[1], vertices[3], 8),
         Edge(vertices[1], vertices[4], 2),  
         Edge(vertices[2], vertices[1], -2),
         Edge(vertices[3], vertices[2], -3),
         Edge(vertices[3], vertices[4], 9),
         Edge(vertices[4], vertices[0], 2),
         Edge(vertices[4], vertices[2], 7)]

graph = Graph(vertices)
for edge in edges:
    graph.add_edge(edge)

start_vertex = vertices[0]
print("Shortest distances from vertex", start_vertex.label)
print(bellman_ford(graph, start_vertex))


'''OUTPUT---Shortest distances from vertex 0
{0: 0, 1: 2, 2: 4, 3: 7, 4: 4}'''



