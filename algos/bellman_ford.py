# from entities.graph import Graph
#
#
# def bellman_ford(graph: Graph, source):
#     # Step 1: Prepare the distance and predecessor for each node
#     distance, predecessor = dict(), dict()
#     for i, node in enumerate(graph.nodes):
#         distance[i], predecessor[i] = float('inf'), None
#     distance[source] = 0
#
#     # Step 2: Relax the edges
#     for i, node in enumerate(graph.nodes):
#
#         # If the distance between the node and the neighbour is lower than the current, store it
#         if distance[neighbour] > distance[node] + graph[node][neighbour]:
#             distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node
#
#     # Step 3: Check for negative weight cycles
#     for node in graph:
#         for neighbour in graph[node]:
#             assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."
#
#     return distance, predecessor
