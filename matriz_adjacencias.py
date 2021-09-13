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
        # print(f'Grau de entrada do vértice {vertice} é: {contador}')
        return contador

    def grau_saida(self, vertice):
        contador = 0
        for i in range(len(self.matriz_adjacencias)):
            if self.tem_aresta(i, vertice):
                contador += 1
        # print(f'Grau de saída do vértice {vertice} é: {contador}')
        return contador

    def grau(self, vertice):
        contador = 0
        for i in range(len(self.matriz_adjacencias)):
            if self.tem_aresta(i, vertice) or self.tem_aresta(vertice, i):
                contador += 1
        # print(f'Grau do vértice {vertice} é: {contador}')
        return contador

    def imprimir(self):
        print(self.matriz_adjacencias)

    def warshall(self):
        matriz_alcancabilidade = self.matriz_adjacencias

        for i in range(self.ordem):
            for j in range(self.ordem):
                matriz_alcancabilidade[i, j] = int(matriz_alcancabilidade[i, j] != np.inf)

        for k in range(self.ordem):
            for i in range(self.ordem):
                for j in range(self.ordem):
                    matriz_alcancabilidade[i, j] = matriz_alcancabilidade[i, j] or (matriz_alcancabilidade[i, k] and matriz_alcancabilidade[k, j])

        return matriz_alcancabilidade

    def obter_adjacente(self, v):
        return [[i, self.matriz_adjacencias[v][i]] for i in range(self.ordem) if self.matriz_adjacencias[v][i] != np.inf]

    def dijkstra(self, rot_vt_origem, rot_vt_destino):
        visitados = []
        custos = [[np.inf, 0] for i in range(self.ordem)]
        custos[rot_vt_origem][0] = 0
        rot_vt_corrente = rot_vt_origem

        while len(visitados) < self.ordem:
            for adj in self.obter_adjacente(rot_vt_corrente):
                rotulo_adj, valor_adj = adj
                if rotulo_adj not in visitados:
                    acumulado = valor_adj + custos[rot_vt_corrente][0]
                    if acumulado < custos[rotulo_adj][0]:
                        custos[rotulo_adj] = acumulado, rot_vt_corrente
            visitados.append(rot_vt_corrente)
            rot_vt_corrente = self.obter_rotulo_menor_VA(visitados, custos)
        return self.obter_menor_caminho(custos, rot_vt_origem, rot_vt_destino)

    @staticmethod
    def obter_menor_caminho(custos, rot_vt_origem, rot_vt_destino):
        caminho = [rot_vt_destino]

        anterior = custos[rot_vt_destino][1]

        while anterior != rot_vt_origem:
            caminho.append(anterior)
            anterior = custos[anterior][1]

        caminho.append(rot_vt_origem)

        return caminho[::-1], custos[rot_vt_destino][0]

    def obter_rotulo_menor_VA(self, visitados, custos):
        rotulo_menor = None
        valor_menor = np.inf

        for i in range(self.ordem):
            if i not in visitados:
                if valor_menor == np.inf or custos[i][0] < valor_menor:
                    rotulo_menor = i
                    valor_menor = custos[i][0]

        return rotulo_menor

    def existe_caminho(self, u, v):
        if self.matriz_adjacencias[u, v]:
            return True
        matriz_alcancabilidade = self.warshall()
        return True if matriz_alcancabilidade[u, v] else False

# metodo para validar se cada o grafo eh fortemente conectado
    def strong_conected(self):
        matriz_alcancabilidade = self.warshall()
        for row in matriz_alcancabilidade:
            if False in row:
                return False
        return True

# metodo para validar se cada node possuem a mesma ordem para grau de entrada e saida
    def equal_degrees(self):
        for node in range(self.ordem):
            if self.grau_saida(node) != self.grau_entrada(node):
                return False
        return True

    def eulerian_circuit(self):
        return self.strong_conected() and self.equal_degrees()

    def eulerian_path(self):
        odd_degree_nodes_with_diff1 = 0
        even_degree_nodes = 0
        for node in range(self.ordem):
            outdegree = self.grau_saida(node)
            indegree = self.grau_entrada(node)
            degree = self.grau(node)
            diff = (outdegree - indegree) if (0 <= (outdegree - indegree)) else (indegree - outdegree)
            if (1 == degree % 2) and (1 == diff):
                odd_degree_nodes_with_diff1 += 1
            elif 0 == degree % 2:
                even_degree_nodes += 1
        return self.strong_conected() and (2 == odd_degree_nodes_with_diff1) and (self.ordem == (odd_degree_nodes_with_diff1+even_degree_nodes))

    def is_Eulerian(self):
        # validacao se o grafo possui um circuito euleriano
        if self.eulerian_circuit():
            return 1
        # validacao se o grafo possui um caminho euleriano
        elif self.eulerian_path():
            return 2
        return 0


###########################################
def teste():
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

    print('\nChamada Metodo is_euleriano, retorno: ', end='')
    print(f'{g.is_Eulerian()}\n')


def teste_warshall_dijkstra():
    g = Grafo(7)
    g.adiciona_aresta(0, 1, 3)
    g.adiciona_aresta(1, 4, 4)
    g.adiciona_aresta(4, 5, 3)
    g.adiciona_aresta(5, 6, 2)
    g.adiciona_aresta(2, 0, 2)
    g.adiciona_aresta(2, 0, 1)
    g.adiciona_aresta(3, 2, 1)
    g.adiciona_aresta(3, 4, 150)
    g.adiciona_aresta(6, 4, 4)
    g.adiciona_aresta(6, 5, 7)
    g.adiciona_aresta(3, 6, 25)
    g.adiciona_aresta(0, 3, 5)
    g.imprimir()
    dijkstra = g.dijkstra(3, 6)
    warshall = g.warshall()
    print(dijkstra)
    print(warshall)


teste()
teste_warshall_dijkstra()
