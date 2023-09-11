import os

from entities.graph import Graph
from util.util import maze_csv_to_matrix
from algos.dijkstras import dijkstra

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    matrix = maze_csv_to_matrix(BASE_DIR + "/" + "test/test1.csv")
    graph = Graph(matrix)
    print(graph)
    print(dijkstra(graph, graph.nodes.index(graph.start), graph.nodes.index(graph.end)))

