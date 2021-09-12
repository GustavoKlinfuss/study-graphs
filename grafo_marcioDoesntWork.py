class Vertice(object):
    nome: str
    grauEntrada: int
    grauSaida: int

    def __init__(self, nomeVertice: str):
        self.nome = nomeVertice
        self.grauEntrada = 0
        self.grauSaida = 0

    def GetNome(self):
        return self.nome

class Graph(object):
    ListaVertices: list
    ListaAdjacencia: list
    nome: str

    def __init__(self,nomeGrafo):
        self.nome = nomeGrafo
        self.ListaVertices = []
        self.ListaAdjacencia = []

    def AdicionaVertice(self, objVertice: str):
        self.ListaVertices.append(Vertice(objVertice))
        self.ListaAdjacencia.append({
            'vertice': objVertice,
            'conexoes': []
        })

    def ImprimeVertices(self):
        for v in self.ListaVertices:
            print(f'Nome do vertice: {v.GetNome()}')

    def ProcurarVertice(self, vertice: str):
        for v in self.ListaVertices:
            if vertice == v.GetNome():
                return v

    def SelecionaListaAdjacencia(self, nomeVerticeSaida: str):
        for element in self.ListaAdjacencia:
            if element['vertice'].GetNome() == nomeVerticeSaida:
                return element
        return None

    def ArestaExistente(self, vertice_saida: str, vertice_entrada: str):
        vertice_principal = self.SelecionaListaAdjacencia(vertice_saida)
        for conexao in vertice_principal['conexoes']:
            if conexao['vertice'].GetNome() == vertice_entrada:
                return True
        return False

    def AdicionaAresta(self, nome_vertice_saida: str, nome_vertice_entrada: str, peso: int):
        vertice_saida = self.ProcurarVertice(nome_vertice_saida)
        vertice_entrada = self.ProcurarVertice(nome_vertice_entrada)
        if (None != vertice_saida) and (None != vertice_entrada):
            if (not self.ArestaExistente(vertice_saida, vertice_entrada)):
                meuObjeto = self.SelecionaListaAdjacencia(vertice_saida)
                meuObjeto['conexoes'].append({'vertice': vertice_entrada, 'peso': peso})
                vertice_saida.grauEntrada += 1
                vertice_entrada.grauSaida += 1
            else:
                print('Objeto já existente em listaAdjacencia')
        else:
            print('Um um mais objetos passados nao foram encontrados em seu grafo!')

    def SelecionaConexao(self,arrayOfDict, nomeVertice: str):
        for element in arrayOfDict:
            if element['vertice'].GetNome() == nomeVertice:
                return element
        return None

    def RemoveVertice(self,verticeRemovido: str):
        verticeRemovido = self.ProcurarVertice(verticeRemovido)
        self.ListaAdjacencia.remove(self.SelecionaListaAdjacencia(verticeRemovido.GetNome()))
        listasQueContemVerticeRemovido = []
        for obj in self.ListaAdjacencia:
            for element in obj['conexoes']:
                if element['vertuce'].GetNome() == verticeRemovido.GetNome():
                    listasQueContemVerticeRemovido.append(obj)
        for obj in listasQueContemVerticeRemovido:
            v = self.ProcurarVertice(obj['vertice'])
            v.grauSaida -= 1
            obj['conexoes'].remove(self.SelecionaConexao(verticeRemovido.GetNome()))
        self.ListaVertices.remove(verticeRemovido)

meuGrafo = Graph("meuNovoGrafo")
for nome in ['pedro', 'maria', 'antonio', 'clara', 'joao', 'gustavo', 'anderson', 'marcio']:
    meuGrafo.AdicionaVertice(nome)

meuGrafo.ImprimeVertices()
print('\n\n\n')
meuGrafo.RemoveVertice('antonio')
meuGrafo.ImprimeVertices()
