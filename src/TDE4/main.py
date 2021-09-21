from os import path
from grafo import Graph
from glob import glob
from tqdm import tqdm


def main():
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
    print(G.number_of_vertexes())
    print(G.number_of_edges())
    print(G.find_20_highest_in_degree())
    print(G.find_20_highest_out_degree())


if __name__ == '__main__':
    main()
