from os import path
from grafo import Graph
from glob import glob
from tqdm import tqdm


def main():
    execute(1500)


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
                line = line[6:]
                sender = line.strip('\n')
            elif line.startswith('To'):
                line = line[4:]
                aux = line.strip('\n ')
                emails = [e.strip() for e in aux.split(',')]
            elif line.startswith('\t'):
                aux = line.strip('\n\t ')
                emails.extend([e.strip() for e in aux.split(',')])
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
    print(f'Deep Search - {origin_mail} to {dest_mail}:')
    print(f'\tExist path: {deep_search_result[0]}')
    print(f'\tPath: {deep_search_result[1]}')
    print(f'\tCost: {len(deep_search_result[1])}')

    breath_search_result = G.breadth_search(origin_mail, dest_mail)
    print(f'Breath Search - {origin_mail} to {dest_mail}:')
    print(f'\tExist path between {origin_mail} and {dest_mail}: {breath_search_result[0]}')
    print(f'\tPath: {breath_search_result[1]}')
    print(f'\tCost: {len(breath_search_result[1])}')


if __name__ == '__main__':
    main()
