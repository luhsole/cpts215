class Vertex:
    '''
    keep track of the vertices to which it is connected, and the weight of each edge
    '''
    def __init__(self, key):
        '''

        '''
        self.ID = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        '''
        add a connection from this vertex to another
        '''
        self.connected_to[neighbor] = weight

    def __str__(self):
        '''
        returns all of the vertices in the adjacency list, as represented by the connectedTo instance variable
        '''
        return str(self.ID) + ' connected to: ' + str([x.ID for x in self.connected_to])

    def get_connections(self):
        '''

        '''
        return self.connected_to.keys()

    def get_ID(self):
        '''

        '''
        return self.ID

    def get_weight(self, neighbor):
        '''
        returns the weight of the edge from this vertex to the vertex passed as a parameter
        '''
        return self.connected_to[neighbor]

