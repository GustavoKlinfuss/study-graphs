import numpy as np
from functools import reduce


class Grafo:
    def __init__(self, vertices_number):
        self.order = vertices_number
        self.size = 0
        self.matriz_adjacencias = np.ones((vertices_number, vertices_number)) * np.inf

    def adiciona_aresta(self, u, v, weight):
        if not self.tem_aresta(u, v):
            self.matriz_adjacencias[u][v] = weight
            self.size += 1
        print(f'Aresta adicionada: [{u}, {v}] - Peso {weight}')

    def remove_aresta(self, u, v):
        if self.tem_aresta(u, v):
            self.matriz_adjacencias[u][v] = np.inf
            self.size -= 1

    def tem_aresta(self, u, v):
        return self.matriz_adjacencias[u][v] != np.inf

    def grau_entrada(self, u):
        contador = 0

        for linha in self.matriz_adjacencias[u]:
            if linha != np.inf:
                contador += 1

        print(f'Grau de entrada do vértice {u} é: {contador}')

    def grau_saida(self, u):
        contador = 0

        for index in range(len(self.matriz_adjacencias)):
            if self.matriz_adjacencias[index][u] != np.inf:
                contador += 1

        print(f'Grau de saída do vértice {u} é: {contador}')

    def grau(self, u):
        contador = 0

        for i in range(len(self.matriz_adjacencias)):
            if (self.matriz_adjacencias[i][u] != np.inf) or (self.matriz_adjacencias[u][i] != np.inf):
                contador += 1

        print(f'Grau do vértice {u} é: {contador}')

    def imprimir(self):
        print(self.matriz_adjacencias)

    def construir_matriz_alcancabilidade(self):
        matriz_alcancabilidade = self.matriz_adjacencias

        for i in range(self.order):
            for j in range(self.order):
                if matriz_alcancabilidade[i, j] != np.inf:
                    matriz_alcancabilidade[i, j] = 1
                else:
                    matriz_alcancabilidade[i, j] = 0

        for k in range(self.order):
            for i in range(self.order):
                for j in range(self.order):
                    matriz_alcancabilidade[i, j] = matriz_alcancabilidade[i, j] or (matriz_alcancabilidade[i, k] and matriz_alcancabilidade[k, j])

        return matriz_alcancabilidade

    def imprimir_matriz_alcancabilidade(self):
        print(self.construir_matriz_alcancabilidade())

    def existe_caminho(self, u, v):
        if self.matriz_adjacencias[u, v]:
            return True

        matriz_alcancebilidade = self.construir_matriz_alcancabilidade()

        return True if matriz_alcancebilidade[u, v] else False


###########################################

g = Grafo(4)
# g.add_edge(0, 3, 10)
# g.add_edge(0, 1, 40)
# g.add_edge(1, 2, 15)
# g.add_edge(0, 2, 15)
# g.add_edge(3, 0, 40)
# g.add_edge(3, 2, 50)
# g.remove_edge(0, 3)

g.adiciona_aresta(0, 1, 10)
g.adiciona_aresta(1, 2, 10)
g.adiciona_aresta(3, 0, 10)

g.grau_entrada(0)
g.grau_entrada(1)
g.grau_entrada(2)

g.grau_saida(0)
g.grau_saida(1)
g.grau_saida(2)

g.grau(0)
g.grau(1)
g.grau(2)
g.imprimir()
g.imprimir_matriz_alcancabilidade()
