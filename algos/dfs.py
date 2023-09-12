from entities.graph import Graph
from util.util import interpret_result


# pseudocode: https://www.cs.toronto.edu/~heap/270F02/node36.html
def dfs(graph: Graph, start_index: int, end_index: int):
    stack = []
    visited = [False for _ in range(graph.length)]
    predecessor = [None for i in range(graph.length)]
    stack.append(start_index)
    while len(stack) > 0:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            node = graph.nodes[u]
            for neighbor in node.get_neighbors():
                if neighbor:
                    neighbor_index = graph.nodes.index(neighbor)
                    if not visited[neighbor_index]:
                        stack.append(neighbor_index)
                        predecessor[neighbor_index] = u
    print(predecessor)
    interpret_result(predecessor, start_index, end_index, graph)
