# Hansol Lee, Anthony Chelf
# PA 6: KB Game
# Version: 1.0
# Date: December 11, 2021
#
# This program plays the Kevin Bacon game, finding the shortest path to Kevin Bacon.

from Graph import Graph
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class KBGame:
    def __init__(self):
        '''
        Constructor initializing global variables
        '''
        self.g = Graph()
        self.actorID = {}
        self.movieID = {}
        self.maID = {}
        self.T = Graph()
        self.paths = Graph()
        self.summary_list = {}

    def create_graph(self):
        '''
        Creates graph of actors as vertices and movies as edges
        :return:
        '''
        # create dictionaries for each file
        self.create_dict("actors.txt", self.actorID)
        self.create_dict("movies.txt", self.movieID)
        self.create_dict("movie-actors.txt", self.maID)

        # using movie-actor dictionary, add edges
        for key in self.maID:
            edge_name = self.movieID[key]
            value = self.maID[key]
            # if movie has more than one actors, add edge between actors
            if len(value) >= 2:
                i = 0
                while i < len(value) - 1:
                    j = i + 1
                    while j < len(value):
                        self.g.add_edge(self.actorID[value[i]], self.actorID[value[j]], label_name=edge_name)
                        self.g.add_edge(self.actorID[value[j]], self.actorID[value[i]], label_name=edge_name)
                        j += 1
                    i += 1

    def create_dict(self, filename, IDlist):
        '''
        Creates dictionary for the given file
        :param filename: name of file to read
        :param IDlist: the dictionary to fill
        :return:
        '''
        try:
            r_file = open(r"%s" % filename, "r", encoding="latin-1")
        except FileNotFoundError:
            print("File does not exist")
            return None

        for line in r_file:
            s = line.split("|")
            ID = s[0]
            name = s[1].replace("\n", "")
            if IDlist == self.actorID:
                # add vertices if looking at actors list
                IDlist[ID] = name
                self.g.add_vertex(name)
            elif IDlist == self.movieID:
                IDlist[ID] = name
            elif IDlist == self.maID:
                # append actors if in the same movie
                if ID in IDlist:
                    IDlist[ID].append(name)
                else:
                    IDlist[ID] = [name]

    def bfs(self, root):
        '''
        Performs breadth-first search (BFS) to build a tree of shortest path from every vertex that can reach the root back to the root
        :param root: the root of tree
        :return: BFS generated shortest-path tree
        '''
        q = deque()
        q.appendleft(root)
        self.T.add_vertex(root)
        while len(q) > 0:
            v_des = q.pop()
            for edge in self.g.get_edges(v_des):
                v_src = edge[1]
                if v_src not in self.T:
                    self.T.add_vertex(v_src)
                    edge_name = self.g.edge_name[(v_des.get_ID(), v_src.get_ID())]
                    self.T.add_edge(v_src.get_ID(), v_des.get_ID(), label_name=edge_name)
                    q.appendleft(v_src)
        return self.T

    def find_bacon(self, actor, summary=False):
        '''
        Implements the Bacon game and visualizes graph if actor is connected to Kevin Bacon
        :param summary: the usage of method -- False if playing game, True if generating summary
        :param actor: the actor to start from
        :return:
        '''
        bacon_number = 0
        if actor == "Kevin Bacon":
            if summary == False:
                print("Kevin Bacon met Kevin Bacon!\n")
            return bacon_number
        v = self.T.get_vertex(actor)
        paths = ""
        connected = False
        # error checking for lack of connection or validity of input
        try:
            v.get_connections()
        except (TypeError, AttributeError):
            if summary == False:
                print("Actor is either not connected to Kevin Bacon or does not exist in the database. Please enter a different actor.\n")
        else:
            bacon_vertices = [v.ID]
            bacon_edges = []
            bacon_labels = {}
            while not connected:
                for vertex in v.get_connections():
                    temp = v
                    bacon_number += 1
                    root = vertex.ID
                    v = self.T.get_vertex(root)
                    movie_name = self.T.edge_name[(temp.ID, root)]
                    paths += "%s appeared in %s with %s.\n" % (temp.ID, movie_name, root)
                    bacon_vertices.append(root)
                    bacon_edges.append((temp.ID, root))
                    bacon_labels[(temp.ID, root)] = movie_name

                    if root == "Kevin Bacon":
                        connected = True
            if connected and summary == False:
                print("%s's number is %s" % (actor, bacon_number))
                print(paths)
                vis = nx.Graph()
                vis.add_nodes_from(bacon_vertices)
                vis.add_edges_from(bacon_edges)
                pos = nx.shell_layout(vis)
                nx.draw_networkx(vis, pos=pos, node_color="tab:red", node_size=100, font_weight="bold", font_size=7, width=2, edge_color="tab:gray")
                nx.draw_networkx_edge_labels(vis, pos=pos, edge_labels=bacon_labels, font_size=7)
                plt.show()
        return bacon_number

    def bacon_summary(self, gen=False):
        '''
        This additional functionality will calculate bacon numbers for all actors and store them in a dictionary
        :param gen: True if generating a txt file of the summary
        :return:
        '''
        for key in self.actorID:
            value = self.actorID[key]
            bn = self.find_bacon(value, summary=True)
            self.summary_list[value] = bn
        if gen:
            w_summary = open("bacon_number_summary.txt", mode="w+", encoding="latin-1")
            w_summary.write("ActorID\tActor\tBacon Number\n")
            for key in self.actorID:
                value = self.actorID[key]
                bn = self.summary_list.get(value)
                if bn != 0:
                    w_summary.write("%s\t%s\t%s\n" % (key, value, bn))
                else:
                    w_summary.write("%s\t%s\t0\n" % (key, value))
            w_summary.close()

    def find_statistic(self):
        '''
        Additional functionality to calculate some statistics about the dataset
        :return:
        '''
        sum = 0
        max = 0
        min = 1
        furthest_actor = []
        closest_actor = []
        no_relation = []
        for actor in self.summary_list:
            bn = self.summary_list.get(actor)
            # find sum of bacon numbers for actors with finite Bacon numbers
            if bn > 0:
                sum += bn
            # find the maximum bacon number
            if bn > max:
                max = bn
            if 0 < bn < min:
                min = bn
        average = sum / len(self.summary_list)
        # finds the actors with minimum/maximum bacon numbers
        for actor in self.summary_list:
            bn = self.summary_list.get(actor)
            if bn == max:
                furthest_actor.append(actor)
            if bn == min:
                closest_actor.append(actor)
            # find the actors with no relation
            if bn == 0:
                no_relation.append(actor)

        print("The average Bacon number for actors with finite Bacon numbers: %.2f" % average)
        print("The actor(s) with the largest Bacon number %s: %s" % (max, furthest_actor))
        print("The actor(s) with the smallest Bacon number %s: %s" % (min, closest_actor))
        print("The actor(s) with no relation to Kevin Bacon in this dataset are: %s" % no_relation)


def main():
    game = KBGame()
    game.create_graph()
    game.bfs(game.g.get_vertex('Kevin Bacon'))
    print("To quit the program, type return (enter) in answer to a question.\n")
    quit = False
    while not quit:
        actor = input("Enter the name of an actor: ")
        if actor == "":
            quit = True
        else:
            game.find_bacon(actor)

    print("\nSome interesting statistics about the dataset: \n")
    game.bacon_summary()
    game.find_statistic()

    # uncomment the line below to generate txt file of the summary
    # game.bacon_summary(gen=True)


main()
