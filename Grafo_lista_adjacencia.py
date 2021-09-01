class Grafo:
    """
    self.lista_adjacencias é um dicionário de vértices, sendo:
        Key: Nome do vértice
        Value: Lista de conexões de saída do vértice

    Exemplo:
        self.lista_adjacencias = {
            'Maria':[(...),(...),(...)],
            'João':[(...),(...),(...)]
        }

    As conexões do vértice é uma lista de tuplas. Cada tupla possui:
        [0] - Nome do vértice da relação
        [1] - Peso da relação

    Exemplo:
        self.lista_adjacencias = {
            'Maria':[('Joao', 8),('Marcos', 2),('Ana', 3)],
            'João':[]
            'Marcos':[('Joao', 4)]
            'Ana':[('Marcos', 5)]
        }
    """

    def __init__(self):
        self.lista_adjacencias = {}

    def adiciona_vertice(self, nome_do_vt):
        if self.vertice_existe(nome_do_vt):
            print(f"O vértice {nome_do_vt} já existe - Não adicionado")
        else:
            self.lista_adjacencias[nome_do_vt] = []

    def adiciona_aresta(self, nome_vt_origem, nome_vt_destino, peso):
        if not self.vertice_existe(nome_vt_origem) or not self.vertice_existe(nome_vt_destino):
            print(f"Conexão {nome_vt_origem} - {nome_vt_destino} - Um dos vértices não existe")
        else:
            if self.tem_aresta(nome_vt_origem, nome_vt_destino):
                print(f"Conexão {nome_vt_origem} - {nome_vt_destino} impossível - Essa conexão já existe")
            else:
                self.lista_adjacencias[nome_vt_origem].append((nome_vt_destino, peso))

    def remove_aresta(self, nome_vt_origem, nome_vt_destino):
        if not self.vertice_existe(nome_vt_origem) or not self.vertice_existe(nome_vt_destino):
            print(f"Conexão {nome_vt_origem} - {nome_vt_destino} impossível - Um dos vértices não existe")
        if not self.tem_aresta(nome_vt_origem, nome_vt_destino):
            print(f"Conexão {nome_vt_origem} - {nome_vt_destino} impossível - Essa conexão não existe")
        else:
            for relacao in self.lista_adjacencias[nome_vt_origem]:
                if relacao[0] == nome_vt_destino:
                    self.lista_adjacencias[nome_vt_origem].remove(relacao)
                    break

    def remove_vertice(self, nome_vt):
        if not self.vertice_existe(nome_vt):
            print(f"O vértice {nome_vt} não existe para ser removido")
        else:
            del self.lista_adjacencias[nome_vt]

    def vertice_existe(self, vertice):
        return vertice in self.lista_adjacencias

    def tem_aresta(self, nome_vt_origem, nome_vt_destino):
        if not self.vertice_existe(nome_vt_origem) or not self.vertice_existe(nome_vt_destino):
            return False

        for relacao in self.lista_adjacencias[nome_vt_origem]:
            if relacao[0] == nome_vt_destino:
                return True

        return False

    def grau(self, nome_vt):
        if not self.vertice_existe(nome_vt):
            print(f"O vértice {nome_vt} não existe - Sem grau")
        else:
            count = 0
            for vertice in self.lista_adjacencias.items():
                # Lembrando que || vertice[0] == nome || vertice[1] == relacoes
                if vertice[0] == nome_vt:
                    count += len(vertice[1])
                else:
                    for relacao in vertice[1]:
                        count += relacao[0] == nome_vt
            return count

    def peso(self, nome_vt_origem, nome_vt_destino):
        if not self.vertice_existe(nome_vt_origem) or not self.vertice_existe(nome_vt_destino):
            print(f"Impossivel obter peso, {nome_vt_origem} ou {nome_vt_destino} não existe")
        elif not self.tem_aresta(nome_vt_origem, nome_vt_destino):
            print(f'A aresta {nome_vt_origem}, {nome_vt_destino} não existe - Sem peso')
        else:
            for relacao in self.lista_adjacencias[nome_vt_origem]:
                if relacao[0] == nome_vt_destino:
                    return relacao[1]

    def imprime_lista_adjacencias(self):
        print('\n-- LISTA DE ADJACENCIAS')
        for vertice in self.lista_adjacencias.items():
            nome_do_vertice = vertice[0]
            relacoes = vertice[1]
            print(f'{nome_do_vertice}: ', end='')
            self.imprimir_relacoes_vertice(relacoes)
        print('--\n')

    @staticmethod
    def imprimir_relacoes_vertice(relacoes_vertice):
        for relacao in relacoes_vertice:
            print(f'{relacao} -> ', end='')
        print()


g = Grafo()
g.adiciona_vertice('Maria')
g.adiciona_vertice('Maria')
g.adiciona_vertice('Joao')
g.adiciona_vertice('Anderson')
g.adiciona_vertice('Marcio')
g.adiciona_vertice('Gustavo')
g.adiciona_aresta('Maria', 'Marcio', 5)
g.adiciona_aresta('Maria', 'Joao', 6)
g.adiciona_aresta('Joao', 'Maria', 2)
g.imprime_lista_adjacencias()
# g.remove_vertice('Marcio')
# g.remove_aresta('Joao', 'Maria')
# g.remove_aresta('Maria', 'Joao')
g.imprime_lista_adjacencias()

nomes_das_pessoas = ['Maria', 'Joao', 'Anderson', 'Marcio', 'Gustavo']

for nome in nomes_das_pessoas:
    print(f'O grau de {nome} é: {g.grau(nome)}')

peso = g.peso('Maria', 'Marcio')
print(f'\nO peso da relação é: {peso}')
