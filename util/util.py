import csv


def maze_csv_to_matrix(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return [[int(num) for num in row] for row in reader]


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
