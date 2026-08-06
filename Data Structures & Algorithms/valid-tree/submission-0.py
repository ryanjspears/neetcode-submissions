from typing import List


class Node:
    def __init__(self, val):
        # Value of this node.
        self.val = val

        # Other nodes connected to this node.
        self.nodes = []

        # Whether this node was already visited.
        self.isVisited = False


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Maps each node value to its Node object.
        node_map = {}

        # Create all nodes.
        for value in range(n):
            node_map[value] = Node(value)

        # Connect the nodes using the edges.
        for edge in edges:
            start_value = edge[0]
            end_value = edge[1]

            start_node = node_map[start_value]
            end_node = node_map[end_value]

            # The graph edges connect in both directions.
            start_node.nodes.append(end_node)
            end_node.nodes.append(start_node)

        # Start at any one node.
        if len(node_map) == 0:
            return True

        queue = [node_map[0]]
        count = 0

        # Search outward through the graph.
        while len(queue) > 0:
            current_node = queue.pop(0)

            # If we visit something again, return false.
            if current_node.isVisited:
                return False

            current_node.isVisited = True
            count += 1

            # Add all connected nodes to the queue.
            for next_node in current_node.nodes:
                if not next_node.isVisited:
                    queue.append(next_node)

        # If we did not visit every node, the graph is disconnected.
        if count < len(node_map):
            return False

        return True