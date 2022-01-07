"""
Graph ADT implementation using Adjecency Matrix
"""

class Graph:
    __slots__  = '_n_verticies', '_adj_matrix'
    def __init__(self, n_verticies=1):
        self._n_verticies = n_verticies
        self._adj_matrix = [[0] * self._n_verticies for _ in range(self._n_verticies)]
    
    def insert_edge(self, vert1, vert2, weight=1):
        self._adj_matrix[vert1][vert2] = weight
    
    def remove_edge(self, vert1, vert2):
        self._adj_matrix[vert1][vert2] = 0
    
    def edge_exist(self, vert1, vert2):
        return self._adj_matrix[vert1][vert2] != 0

    def count_vertiticies(self):
        return self._n_verticies
    
    def count_edges(self):
        n_edges = 0
        for i in range(self._n_verticies):
            for j in range(self._n_verticies):
                if self._adj_matrix[i][j] != 0:
                    n_edges += 1
        return n_edges

    def get_verticies(self):
        return list(range(self._n_verticies))
    
    def get_edges(self):
        for i in range(self._n_verticies):
            for j in range(self._n_verticies):
                weight = self._adj_matrix[i][j]
                if weight != 0:
                    print(f"{i} -> {j} with weight {weight}")
        print()
    
    def outdegree(self, vertex):
        degree = 0
        for i in range(self._n_verticies):
            if self._adj_matrix[vertex][i] != 0:
                degree += 1
        return degree
    
    def indegree(self, vertex):
        degree = 0
        for i in range(self._n_verticies):
            if self._adj_matrix[i][vertex] != 0:
                degree += 1
        return degree
    
    def display_adj_matrix(self):
        print("Adjecency Matrix:")
        for i in range(self._n_verticies):
            for j in range(self._n_verticies):
                print(f"{self._adj_matrix[i][j]}\t", end='') 
            else:
                print()


g = Graph(3)
print(g.count_vertiticies())
print(g.get_verticies())
g.display_adj_matrix()

g.insert_edge(0, 1)
g.insert_edge(1, 1)
g.insert_edge(0, 2)
g.insert_edge(1, 2)

g.display_adj_matrix()

print(g.count_edges())

print(g.edge_exist(2, 0))

print(g.outdegree(0))
print(g.indegree(2))

g.remove_edge(1, 1)
g.remove_edge(0, 2)

g.display_adj_matrix()

print(g.count_edges())

print(g.edge_exist(1, 1))

print(g.outdegree(0))
print(g.indegree(2))
