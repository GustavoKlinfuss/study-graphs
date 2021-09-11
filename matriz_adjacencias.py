import numpy as np


class Grafo:
    def __init__(self, vertices_number):
        self.ordem = vertices_number
        self.tamanho = 0
        self.matriz_adjacencias = np.ones((vertices_number, vertices_number)) * np.inf

    def adiciona_aresta(self, v_origem, v_destino, peso):
        if not self.tem_aresta(v_origem, v_destino):
            self.matriz_adjacencias[v_origem][v_destino] = peso
            self.tamanho += 1
        print(f'Aresta adicionada: [{v_origem}, {v_destino}] - Peso {peso}')

    def remove_aresta(self, v_origem, v_destino):
        if self.tem_aresta(v_origem, v_destino):
            self.matriz_adjacencias[v_origem][v_destino] = np.inf
            self.tamanho -= 1

    def tem_aresta(self, v_origem, v_destino):
        return self.matriz_adjacencias[v_origem][v_destino] != np.inf

    def grau_entrada(self, vertice):
        contador = 0

        for linha in self.matriz_adjacencias[vertice]:
            if linha != np.inf:
                contador += 1

        print(f'Grau de entrada do vértice {vertice} é: {contador}')

    def grau_saida(self, vertice):
        contador = 0

        for i in range(len(self.matriz_adjacencias)):
            if self.tem_aresta(i, vertice):
                contador += 1

        print(f'Grau de saída do vértice {vertice} é: {contador}')

    def grau(self, vertice):
        contador = 0

        for i in range(len(self.matriz_adjacencias)):
            if self.tem_aresta(i, vertice) or self.tem_aresta(vertice, i):
                contador += 1

        print(f'Grau do vértice {vertice} é: {contador}')

    def imprimir(self):
        print(self.matriz_adjacencias)

    def warshall(self):
        matriz_alcancabilidade = self.matriz_adjacencias

        for i in range(self.ordem):
            for j in range(self.ordem):
                if matriz_alcancabilidade[i, j] != np.inf:
                    matriz_alcancabilidade[i, j] = 1
                else:
                    matriz_alcancabilidade[i, j] = 0

        for k in range(self.ordem):
            for i in range(self.ordem):
                for j in range(self.ordem):
                    matriz_alcancabilidade[i, j] = matriz_alcancabilidade[i, j] or (matriz_alcancabilidade[i, k] and matriz_alcancabilidade[k, j])

        return matriz_alcancabilidade

    def dijkstra(self, vertice_origem):
        visitados = []
        custos = [[np.inf, 0] for i in range(self.ordem)]
        custos[vertice_origem][0] = 0

        print(f"dijkstra: {custos}")

    def existe_caminho(self, u, v):
        if self.matriz_adjacencias[u, v]:
            return True

        matriz_alcancebilidade = self.warshall()

        return True if matriz_alcancebilidade[u, v] else False


###########################################

g = Grafo(4)
g.adiciona_aresta(0, 3, 10)
g.imprimir()
g.remove_aresta(0, 3)
g.imprimir()

g.adiciona_aresta(1, 0, 40)
g.adiciona_aresta(0, 1, 10)
g.adiciona_aresta(1, 2, 10)
g.adiciona_aresta(3, 0, 10)

g.imprimir()

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
print(f'Matriz de alcançabilidade:\n{g.warshall()}')
