from queue import PriorityQueue

from entities.graph import Graph
from util.util import interpret_result


def dijkstra(graph: Graph, start_index: int, end_index: int):
    dist = [float('inf') for i in range(graph.length)]
    predecessor = [None for i in range(graph.length)]
    pq = PriorityQueue()
    pq.put((0, start_index))
    dist[start_index] = 0

    while not pq.empty():
        (_, current_vertex_index) = pq.get()
        current_vertex = graph.nodes[current_vertex_index]
        for neighbor in current_vertex.get_neighbors():
            if neighbor:
                neighbor_index = graph.nodes.index(neighbor)
                alt = dist[current_vertex_index] + current_vertex.get_distance(neighbor)
                if alt < dist[neighbor_index]:
                    dist[neighbor_index] = alt
                    predecessor[neighbor_index] = current_vertex_index
                    pq.put((alt, neighbor_index))
    return interpret_result(predecessor, start_index, end_index, graph)
