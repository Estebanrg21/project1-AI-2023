from queue import PriorityQueue

from entities.graph import Graph


def a_star(graph: Graph, start_index: int, end_index: int, heuristic_function):
    pq = PriorityQueue()
    pq.put((0, start_index))

    came_from = {}
    g_score = {index: float('inf') for index in range(graph.length)}
    g_score[start_index] = 0

    f_score = {start_index: heuristic_function(start_index, end_index)}

    while not pq.empty():
        (_, current_vertex_index) = pq.get()
        if current_vertex_index == end_index:
            return reconstruct_path(came_from, current_vertex_index) + [start_index]
        current_vertex = graph.nodes[current_vertex_index]
        for neighbor in current_vertex.get_neighbors():
            if neighbor:
                neighbor_index = graph.nodes.index(neighbor)
                tentative_g_score = g_score[current_vertex_index] + current_vertex.get_distance(neighbor)
                if tentative_g_score < g_score[neighbor_index]:
                    came_from[neighbor_index] = current_vertex_index
                    g_score[neighbor_index] = tentative_g_score
                    f_score[neighbor_index] = tentative_g_score + \
                                              heuristic_function(current_vertex_index, neighbor_index)
                    pq.put((g_score, neighbor_index))


def reconstruct_path(predecessor: dict, current_vertex_index: int):
    total_path = []
    while current_vertex_index in predecessor.keys():
        total_path.append(current_vertex_index)
        current_vertex_index = predecessor[current_vertex_index]
    return total_path
