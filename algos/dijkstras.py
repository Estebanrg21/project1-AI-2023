from queue import PriorityQueue

from entities.graph import Graph


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


def interpret_result(prev, start_index, end_index, graph):
    path = []
    node_index = end_index
    while node_index != start_index:
        if node_index is None:
            return None
        path.append(node_index)
        node_index = prev[node_index]
    path.append(start_index)
    return path
