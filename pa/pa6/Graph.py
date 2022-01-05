from Vertex import Vertex


class Graph:
    '''
    contains a dictionary that maps vertex names to vertex objects.
    '''
    def __init__(self):
        '''

        '''
        self.vert_list = {}
        self.num_vertices = 0
        self.edge_name = {}

    def __str__(self):
        '''

        '''
        edges = ""
        for vert in self.vert_list.values():
            for vert2 in vert.get_connections():
                edges += "(%s, %s, %s)\n" % (vert.get_ID(), vert2.get_ID(), self.edge_name[(vert.get_ID(), vert2.get_ID())])
        return edges

    def add_vertex(self, key):
        '''
        adding vertices to a graph
        '''
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        '''

        '''
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        '''
        in operator
        '''
        return n in self.vert_list

    def add_edge(self, f, t, cost=0, label_name=""):
        '''
        connecting one vertex to another
        '''
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)
        self.edge_name[(f, t)] = label_name

    def get_vertices(self):
        '''
        returns the names of all of the vertices in the graph
        '''
        return self.vert_list.keys()

    def __iter__(self):
        '''
        for functionality
        '''
        return iter(self.vert_list.values())

    def get_edges(self, v):
        edges = []
        for vert in v.get_connections():
            edges.append([v, vert])
        return edges

    def get_all_edges(self):
        edges = []
        for vert in self.vert_list.values():
            for vert2 in vert.get_connections():
                edges.append([vert.get_ID(), vert2.get_ID()])
        return edges
