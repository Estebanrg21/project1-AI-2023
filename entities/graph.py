from entities.node import Node
import copy

START_REPRESENTATION = 2
END_REPRESENTATION = 3
OBSTACLES_REPRESENTATION = 1


class Graph:
    def __init__(self, matrix):
        """
        :param matrix: list of int lists
        """
        self.nodes, self.node_matrix, self.n, self.m = convert_matrix_to_node_representation(matrix)
        self.start = None
        self.end = None
        self.get_start()
        self.get_end()
        self.length = len(self.nodes)

    def get_start(self):
        if self.start is None:
            for node in self.nodes:
                if node.representation == START_REPRESENTATION:
                    self.start = node
                    break
        return self.start

    def get_end(self):
        if self.end is None:
            for node in self.nodes:
                if node.representation == END_REPRESENTATION:
                    self.end = node
                    break
        return self.end

    def __repr__(self):
        string = ""
        for node_row in self.node_matrix:
            for node in node_row:
                string += f" {self.nodes.index(node) if node else '@'} "
            string += "\n"
        return string


def convert_matrix_to_node_representation(matrix):
    n = len(matrix)
    m = len(matrix[0])
    non_util_representations = [OBSTACLES_REPRESENTATION]
    node_matrix = copy.deepcopy(matrix)
    # filling node_matrix
    for i in range(n):
        for j in range(m):
            representation = matrix[i][j]
            if representation not in non_util_representations:
                node_matrix[i][j] = Node(representation, i, j)
            else:
                node_matrix[i][j] = None
    # assigning near nodes to each node
    for i in range(n):
        for j in range(m):
            node = node_matrix[i][j]
            if node is not None:
                find_close_nodes(n, m, node_matrix, node)

    node_list = []
    for i in range(n):
        for j in range(m):
            node = node_matrix[i][j]
            if node is not None:
                node_list.append(node)
    return node_list, node_matrix, n, m


def find_close_nodes(matrix_rows, matrix_cols, matrix, current_node: Node):
    row = current_node.position_x
    col = current_node.position_y
    if col - 1 >= 0:
        current_node.left = matrix[row][col - 1]
        current_node.left_weight = 1
    if col + 1 <= matrix_cols - 1:
        current_node.right = matrix[row][col + 1]
        current_node.right_weight = 1
    if row - 1 >= 0:
        current_node.up = matrix[row - 1][col]
        current_node.up_weight = 1
    if row + 1 <= matrix_rows - 1:
        current_node.down = matrix[row + 1][col]
        current_node.down_weight = 1
