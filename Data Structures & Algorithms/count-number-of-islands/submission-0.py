from typing import List


class Node:
    def __init__(self, isLand):
        self.isLand = isLand
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.visited = False


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Hash map:
        # (row, col) -> Node
        node_map = {}

        # First iterate through the matrix and create every node
        for row in range(rows):
            for col in range(cols):
                node_map[(row, col)] = Node(grid[row][col] == "1")

        # Iterate again and connect neighboring nodes
        for row in range(rows):
            for col in range(cols):
                current = node_map[(row, col)]

                if row > 0:
                    current.up = node_map[(row - 1, col)]

                if row < rows - 1:
                    current.down = node_map[(row + 1, col)]

                if col > 0:
                    current.left = node_map[(row, col - 1)]

                if col < cols - 1:
                    current.right = node_map[(row, col + 1)]

        island_count = 0

        def outwardTraversal(node):
            # Ignore water or nodes we already visited
            if node is None or not node.isLand or node.visited:
                return

            node.visited = True

            outwardTraversal(node.up)
            outwardTraversal(node.down)
            outwardTraversal(node.left)
            outwardTraversal(node.right)

        # Find every unvisited piece of land
        for row in range(rows):
            for col in range(cols):
                current = node_map[(row, col)]

                if current.isLand and not current.visited:
                    island_count += 1
                    outwardTraversal(current)

        return island_count