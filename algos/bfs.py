from collections import deque

from entities.graph import Graph
from util.util import interpret_result


def bfs(graph: Graph, start_index: int, end_index: int):
    dist = [float('inf') for i in range(graph.length)]
    predecessor = [None for i in range(graph.length)]
    q = deque()
    q.append(start_index)
    dist[start_index] = 0
    while q:
        current_vertex_index = q[0]
        q.popleft()
        current_vertex = graph.nodes[current_vertex_index]
        for neighbor in current_vertex.get_neighbors():
            if neighbor:
                neighbor_index = graph.nodes.index(neighbor)
                weight = current_vertex.get_distance(neighbor)
                val = dist[current_vertex_index] + weight
                if dist[neighbor_index] > val:
                    dist[neighbor_index] = val
                    predecessor[neighbor_index] = current_vertex_index
                    # if 0 weight edge, store at front of deque
                    # else if 1 weight edge, store at back of deque
                    # so that vertices will be processed in a sorted increasing weight order
                    q.appendleft(neighbor_index) if weight == 0 else q.append(neighbor_index)
    return interpret_result(predecessor, start_index, end_index, graph)
