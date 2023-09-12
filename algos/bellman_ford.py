from entities.graph import Graph
from util.util import interpret_result


def bellman_ford(graph: Graph, start_index: int, end_index: int):
    dist = [float('inf') for i in range(graph.length)]
    predecessor = [None for i in range(graph.length)]
    dist[start_index] = 0

    # Relax edges repeatedly
    for _ in range(graph.length - 1):
        for current_vertex_index in range(graph.length):
            current_vertex = graph.nodes[current_vertex_index]
            for neighbor in current_vertex.get_neighbors():
                if neighbor:
                    neighbor_index = graph.nodes.index(neighbor)
                    val = dist[current_vertex_index] + current_vertex.get_distance(neighbor)
                    if val < dist[neighbor_index]:
                        dist[neighbor_index] = val
                        predecessor[neighbor_index] = current_vertex_index

    # Check for negative-weight cycles
    for current_vertex_index in range(graph.length):
        current_vertex = graph.nodes[current_vertex_index]
        for neighbor in current_vertex.get_neighbors():
            if neighbor:
                neighbor_index = graph.nodes.index(neighbor)
                val = dist[neighbor_index] + current_vertex.get_distance(neighbor)
                if val < dist[current_vertex_index]:
                    predecessor[current_vertex_index] = neighbor_index
                    # A negative cycle exist; find a vertex on the cycle
                    visited = [False for i in range(graph.length)]
                    visited[current_vertex_index] = True
                    __neighbor_index = neighbor_index
                    __current_vertex = current_vertex
                    while not visited[__neighbor_index]:
                        visited[__neighbor_index] = True
                        __neighbor_index = graph.nodes.index(predecessor[__neighbor_index])
                    ncycle = [graph.nodes[__neighbor_index]]
                    __current_vertex = predecessor[__neighbor_index]
                    while __current_vertex != __neighbor_index:
                        ncycle = [__current_vertex] + ncycle
                        __current_vertex = predecessor[graph.nodes.index(__current_vertex)]
                    return None
    return interpret_result(predecessor, start_index, end_index, graph)

