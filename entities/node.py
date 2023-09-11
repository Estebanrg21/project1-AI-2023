class Node:
    def __init__(self, representation: int, position_x: int, position_y: int):
        self.representation = representation
        self.position_x = position_x
        self.position_y = position_y
        self.up = None
        self.up_weight = float('inf')
        self.down = None
        self.down_weight = float('inf')
        self.left = None
        self.left_weight = float('inf')
        self.right = None
        self.right_weight = float('inf')

    def get_neighbors(self):
        return [self.up, self.left, self.right, self.down]

    def is_neighbor(self, node):
        return node is self.up \
               or node is self.down \
               or node is self.left \
               or node is self.right

    def get_distance(self, node):
        if node is self.up:
            return self.up_weight
        if node is self.down:
            return self.down_weight
        if node is self.left:
            return self.left_weight
        if node is self.right:
            return self.right_weight

    def __repr__(self):
        return f"{self.representation}"
