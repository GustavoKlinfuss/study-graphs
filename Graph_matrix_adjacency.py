import numpy as np


class Graph:
    def __init__(self, vertices_number):
        self.order = vertices_number
        self.structure = AdjacencyMatrix(vertices_number)

    def add_edge(self, u, v, peso):
        self.structure.add_edge(u, v, peso)

    def remove_edge(self, u, v):
        self.structure.remove_edge(u, v)

    def has_edge(self, u, v):
        self.structure.has_edge(u, v)

    def indegree(self, u):
        self.structure.indegree(u)

    def outdegree(self, u):
        self.structure.outdegree(u)

    def degree(self, u):
        self.structure.degree(u)

    def print_adjacency_matrix(self):
        self.structure.print()

    def print_reachability_matrix(self):
        self.structure.print_reachability_matrix();


class AdjacencyMatrix:
    def __init__(self, vertices_number):
        self.order = vertices_number
        self.size = 0
        self.adjacency_matrix = np.ones((vertices_number, vertices_number)) * np.inf
        print('Matriz de adjacencia criada')

    def add_edge(self, u, v, weight):
        if not self.has_edge(u, v):
            self.adjacency_matrix[u][v] = weight
            self.size += 1
        print(f'Aresta adicionada: [{u}, {v}] - Peso {weight}')

    def remove_edge(self, u, v):
        if self.has_edge(u, v):
            self.adjacency_matrix[u][v] = np.inf
            self.size -= 1

    def has_edge(self, u, v):
        return self.adjacency_matrix[u][v] != np.inf

    def indegree(self, u):
        count = 0

        for val in self.adjacency_matrix[u]:
            if val != np.inf:
                count += 1

        print(f'Grau de entrada do vértice {u} é: {count}')

    def outdegree(self, u):
        count = 0

        for i in range(len(self.adjacency_matrix)):
            if self.adjacency_matrix[i][u] != np.inf:
                count += 1

        print(f'Grau de saída do vértice {u} é: {count}')

    def degree(self, u):
        count = 0

        for i in range(len(self.adjacency_matrix)):
            if (self.adjacency_matrix[i][u] != np.inf) or (self.adjacency_matrix[u][i] != np.inf):
                count += 1

        print(f'Grau do vértice {u} é: {count}')

    def print(self):
        print(self.adjacency_matrix)

    def print_reachability_matrix(self):
        rc_matrix = self.adjacency_matrix

        for i in range(self.order):
            for j in range(self.order):
                if rc_matrix[i, j] != np.inf:
                    rc_matrix[i, j] = 1
                else:
                    rc_matrix[i, j] = 0

        for k in range(self.order):
            for i in range(self.order):
                for j in range(self.order):
                    rc_matrix[i, j] = rc_matrix[i, j] or (rc_matrix[i, k] and rc_matrix[k, j])

        print(rc_matrix)

    def exist_path(self, u, v):
        rc_matrix = self.adjacency_matrix

        if rc_matrix[u, v]:
            return True

        for i in range(self.order):
            for j in range(self.order):
                rc_matrix[i, j] = bool(rc_matrix[i, j] != np.inf)

        for k in range(self.order):
            for i in range(self.order):
                for j in range(self.order):
                    rc_matrix[i, j] = rc_matrix[i, j] or (rc_matrix[i, k] and rc_matrix[k, j])

        return rc_matrix[u, v]


###########################################

g = Graph(4)
# g.add_edge(0, 3, 10)
# g.add_edge(0, 1, 40)
# g.add_edge(1, 2, 15)
# g.add_edge(0, 2, 15)
# g.add_edge(3, 0, 40)
# g.add_edge(3, 2, 50)
# g.remove_edge(0, 3)

g.add_edge(0, 1, 10)
g.add_edge(1, 2, 10)
g.add_edge(3, 0, 10)

g.indegree(0)
g.indegree(1)
g.indegree(2)

g.outdegree(0)
g.outdegree(1)
g.outdegree(2)

g.degree(0)
g.degree(1)
g.degree(2)
g.print_adjacency_matrix()
g.print_reachability_matrix()
