class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.inf = float('inf')
        self.graph = [[self.inf] * num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            self.graph[i][i] = 0

    def add_edge(self, start, end, weight):
        self.graph[start][end] = weight

    def floyd_warshall(self):
        dist = [row[:] for row in self.graph]
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist

num_vertices = 4
graph = Graph(num_vertices)

graph.add_edge(0, 1, 1)
graph.add_edge(0, 3, 7)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 0, 2)
graph.add_edge(2, 3, 4)
graph.add_edge(3, 2, 1)

shortest_paths = graph.floyd_warshall()

print("Shortest paths between all pairs of vertices:")
for i in range(num_vertices):
    for j in range(num_vertices):
        print(f"From vertex {i} to vertex {j}: {shortest_paths[i][j]}")



'''OUTPUT----
Shortest paths between all pairs of vertices:
From vertex 0 to vertex 0: 0
From vertex 0 to vertex 1: 1
From vertex 0 to vertex 2: 2
From vertex 0 to vertex 3: 6
From vertex 1 to vertex 0: 3
From vertex 1 to vertex 1: 0
From vertex 1 to vertex 2: 1
From vertex 1 to vertex 3: 5
From vertex 2 to vertex 0: 2
From vertex 2 to vertex 1: 3
From vertex 2 to vertex 2: 0
From vertex 2 to vertex 3: 4
From vertex 3 to vertex 0: 3
From vertex 3 to vertex 1: 4
From vertex 3 to vertex 2: 1
From vertex 3 to vertex 3: 0 '''