

def DFG_iterative(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        s = stack.pop()
        if s not in visited:
            visited.append(s)
            stack += [x for x in graph[s][::-1] if x not in visited]
    return visited


def DFG_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for x in graph[node]:
        if x not in visited:
            visited = DFG_recursive(graph, x, visited)
    return visited


def BFG_iterative(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        s = stack.pop(0)
        if s not in visited:
            visited.append(s)
            stack += [x for x in graph[s] if x not in visited][::1]
    return visited


G = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

H = {
    '1': ['5', '6'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['2', '3', '5', '9'],
    '5': ['1', '4', '6', '9'],
    '6': ['1', '5', '9'],
    '7': ['8', '9'],
    '8': ['7', '9', '12'],
    '9': ['4', '5', '6', '7', '8', '10', '11', '13'],
    '10': ['9', '13'],
    '11': ['9', '12', '13'],
    '12': ['8', '11'],
    '13': ['9', '10', '11']
}

print(DFG_iterative(G, 'A'))
print(DFG_recursive(G, 'A'))

print(BFG_iterative(G, 'A'))

print(DFG_iterative(H, '1'))
print(DFG_recursive(H, '1'))
