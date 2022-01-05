import numpy as np


class Graph:
    def __init__(self):
        '''
        initializes fields
        '''
        self.vert_list = []
        self.adj_matrix = np.empty((0, 0))

    def add_vertex(self, key):
        '''
        adds a vertex to the list if it does not exist already
        :param key: vertex to add
        :return:
        '''
        if key not in self.vert_list:
            self.vert_list.append(key)

    def add_edge(self, v1, v2):
        '''
        adds an edge between two vertices
        if given vertex/vertices doesn't/don't exist already, they're added to the list
        :param v1: vertex 1
        :param v2: vertex 2
        :return:
        '''
        if v1 not in self.vert_list:
            self.add_vertex(v1)
        if v2 not in self.vert_list:
            self.add_vertex(v2)

        if max(v1, v2) >= len(self.adj_matrix):
            padding_index = max(v1, v2) - len(self.adj_matrix) + 1
            self.adj_matrix = np.pad(self.adj_matrix, ((0, padding_index), (0, padding_index)), constant_values=(0, 0))

        row_index = self.vert_list.index(v1)
        col_index = self.vert_list.index(v2)
        self.adj_matrix[row_index][col_index] = 1
        self.adj_matrix[col_index][row_index] = 1

    def __str__(self):
        '''
        returns a string representation of the graph
        :return: string representation of the graph
        '''
        edges = ""
        for i in range(0, len(self.vert_list)):
            for j in range(0, len(self.vert_list)):
                if self.adj_matrix[i][j] == 1:
                    edges += "(%s, %s)\n" % (self.vert_list[i], self.vert_list[j])
        return edges


def main():
    graph = Graph()

    # graph.add_vertex(1)
    # graph.add_vertex(2)
    # graph.add_vertex(3)
    # graph.add_vertex(4)
    # graph.add_vertex(5)
    # graph.add_vertex(6)

    graph.add_edge(1, 2)
    graph.add_edge(1, 5)
    graph.add_edge(5, 2)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    graph.add_edge(4, 6)
    graph.add_edge(4, 5)

    print(graph)


main()
