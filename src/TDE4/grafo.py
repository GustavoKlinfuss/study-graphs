import bisect
from binarySearch import b_search
from edge import Edge


class Graph:

    def __init__(self):
        self.vlist = []
        self.edges = []
        self.degrees = {}

    def check_vlist(self, v):
        if v not in self.vlist:
            return False
        else:
            return True

    def number_of_vertexes(self):
        return len(self.vlist)

    def number_of_edges(self):
        return len(self.edges)

    def add_vertex(self, vname):
        if b_search(self.vlist, vname) == -1:
            bisect.insort(self.vlist, vname)
            self.degrees[vname] = {'in': 0, 'out': 0}
        else:
            return

    def add_edge(self, v1, v2, weight):
        if self.check_vlist(v1) == False:
            print('Vertex {} does not belong to graph!'.format(v1))
            return
        elif self.check_vlist(v2) == False:
            print('Vertex {} does not belong to graph!'.format(v2))
            return
        else:
            new_edge = Edge(v1, v2, weight)
            search = b_search(self.edges, new_edge)
            if search == -1:
                bisect.insort(self.edges, new_edge)
                self.degrees[v1]['out'] += 1
                self.degrees[v2]['in'] += 1
            else:
                self.edges[search].add_weight(1)
                             

    def remove_edge(self, v1, v2):
        if self.check_vlist(v1) == False:
            print('Vertex {} does not belong to graph!'.format(v1))
            return
        elif self.check_vlist(v2) == False:
            print('Vertex {} does not belong to graph!'.format(v2))
            return
        else:
            index = b_search(self.edges, Edge(v1, v2, 0))
            if index != -1:
                self.degrees[v1]['out'] -= 1
                self.degrees[v2]['in'] -= 1
                del self.edges[index]
            else:
                return
            
    def remove_vertex(self, v):
        if self.check_vlist(v) == False:
            print('Vertex {} does not belong to graph!'.format(v))
            return
        else:
            for vertex in self.vlist:
                self.remove_edge(vertex, v)
                self.remove_edge(v, vertex)
            self.vlist.remove(v)
            del self.degrees[v]

    def edge_exists(self, v1, v2):
        if self.check_vlist(v1) == False:
            print('Vertex {} does not belong to graph!'.format(v1))
            return False
        elif self.check_vlist(v2) == False:
            print('Vertex {} does not belong to graph!'.format(v2))
            return False
        else:
            edge = Edge(v1, v2, 0)
            index = b_search(self.edges, edge)
            if index != -1:
                return True, index 
            else:
                return False, index

    def vertex_degree(self, v):
        return self.degrees[v]['in'] + self.degrees[v]['out']

    def vertex_out_degree(self, v):
        return self.degrees[v]['out']
    
    def vertex_in_degree(self, v):
        return self.degrees[v]['in']

    def edge_weight(self, v1, v2):
        if self.check_vlist(v1) == False:
            print('Vertex {} does not belong to graph!'.format(v1))
            return
        elif self.check_vlist(v2) == False:
            print('Vertex {} does not belong to graph!'.format(v2))
            return
        else:
            exists, index = self.edge_exists(v1, v2)
            if exists == True: 
                return self.edges[index].get_weight()
            else:
                print('Edge does note exist!')

    def find_20_highest_in_degree(self):
        high20 = []
        keys = list(self.degrees.keys())
        values = [value['in'] for value in self.degrees.values()]
        for i in range(20):
            highest = max(values)
            index = values.index(highest)
            high20.append({keys[index]: values[index]})
            del keys[index]
            del values[index]        
        return high20

    def find_20_highest_out_degree(self):
        high20 = []
        keys = list(self.degrees.keys())
        values = [value['out'] for value in self.degrees.values()]
        for i in range(20):
            highest = max(values)
            index = values.index(highest)
            high20.append({keys[index]: values[index]})
            del keys[index]
            del values[index]        
        return high20

    def deep_search(self, origin_vertex, dest_vertex):
        if origin_vertex not in self.vlist:
            print(f'Vertex {origin_vertex} does not belong to graph!')
            return False, []
        if dest_vertex not in self.vlist:
            print(f'Vertex {dest_vertex} does not belong to graph!')
            return False, []

        visited = []
        stack = [origin_vertex]

        while stack:
            verified_vertex = stack.pop()
            if verified_vertex not in visited:
                visited.append(verified_vertex)
                if verified_vertex == dest_vertex:
                    return True, visited
                adjacent = self.get_adjacent_vertexes(verified_vertex)[::-1]
                not_visited_adjacent = [vertex for vertex in adjacent if vertex not in visited]
                stack += not_visited_adjacent

        return False, []

    def breadth_search(self, origin_vertex, dest_vertex):
        if origin_vertex not in self.vlist:
            print(f'Vertex {origin_vertex} does not belong to graph!')
            return False, []
        if dest_vertex not in self.vlist:
            print(f'Vertex {dest_vertex} does not belong to graph!')
            return False, []

        visited = []
        queue = [origin_vertex]

        while queue:
            verified_vertex = queue.pop(0)
            if verified_vertex not in visited:
                visited.append(verified_vertex)
                if verified_vertex == dest_vertex:
                    return True, visited
                adjacent = self.get_adjacent_vertexes(verified_vertex)
                not_visited_adjacent = [vertex for vertex in adjacent if vertex not in visited]
                queue += not_visited_adjacent

        return False, []

    # def find_v_within_d(self, origin_vertex, distance):
    #     if origin_vertex not in self.vlist:
    #         print(f'Vertex {origin_vertex} does not belong to graph!')
    #         return False, []
    #
    #     v_in_distance = []
    #     for v in self.vlist:
    #         found, steps = self.breadth_search(origin_vertex, v)
    #         if found and len(steps) - 1 == distance:
    #             v_in_distance.append(v)
    #     return v_in_distance

    def find_v_within_d(self, origin_vertex, distance):
        if origin_vertex not in self.vlist:
            print(f'Vertex {origin_vertex} does not belong to graph!')
            return False, []

        visited = []
        queue = [origin_vertex]

        for i in range(distance):
            new_queue = []

            for element in queue:
                if element not in visited:
                    visited.append(element)
                    adjacent = self.get_adjacent_vertexes(element)
                    not_visited_adjacent = [vertex for vertex in adjacent if vertex not in visited]
                    new_queue += not_visited_adjacent

            queue = new_queue

        return queue


    def get_adjacent_vertexes(self, vertex):
        return [i.dest for i in self.edges if i.origin == vertex]

    # def print_adjacency_list(self):
    #     for key, vlist in self.edges.items():
    #         print(key + ' : ', end='')
    #         for item in vlist:
    #             for key2, w in item.items():
    #                 print('(' + key2 + ', ' + str(w) + ')->', end='')
    #         print('\n')
