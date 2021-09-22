from os import path
from grafo import Graph
from glob import glob
from tqdm import tqdm


def main():
    execute(1000)


def execute(vertex_limit=None):
    G = Graph()
    sender = ''
    emails = []
    for filename in tqdm(glob('Amostra Enron - 2016/**/*', recursive=True)):
        if path.isdir(filename):
            continue
        file = open(filename, 'r')
        for line in file:
            if line.startswith('From'):
                sender = line[6:].strip('\n')
            elif line.startswith('To'):
                line = line[4:]
                aux = line.strip('\n ')
                emails = aux.split(',')
            elif line.startswith('\t'):
                aux = line.strip('\n\t ')
                emails.extend(aux.split(','))
            elif line.startswith('Subject'):
                break
            else:
                continue
            if '' in emails:
                emails.remove('')
            G.add_vertex(sender)
            for email in emails:
                G.add_vertex(email)
                G.add_edge(sender, email, 1)
        file.close()
        if vertex_limit and len(G.vlist) > vertex_limit:
            break

    origin_mail = '40enron@enron.com'
    dest_mail = 'sandra.f.brawner@enron.com'

    deep_search_result = G.deep_search(origin_mail, dest_mail)
    print('Busca em profundidade:')
    print(f'\tExist path between {origin_mail} and {dest_mail}: {deep_search_result[0]}')
    print(f'\tPath: {deep_search_result[1]}')


if __name__ == '__main__':
    main()
