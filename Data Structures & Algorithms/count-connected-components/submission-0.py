from typing import List


class Node:
    def __init__(self, val):
        # Value represented by this node.
        self.val = val

        # Other nodes connected to this node.
        self.nodes = []

        # Tracks whether this node has been visited.
        self.isVisited = False


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Maps each node value to its Node object.
        node_map = {}

        # Create every node.
        for value in range(n):
            node_map[value] = Node(value)

        # Connect the nodes using the edges.
        for edge in edges:
            start_value = edge[0]
            end_value = edge[1]

            start_node = node_map[start_value]
            end_node = node_map[end_value]

            # The graph is undirected, so connect both directions.
            start_node.nodes.append(end_node)
            end_node.nodes.append(start_node)

        output = 0

        # Look through every node in the graph.
        for node in node_map.values():
            # Skip nodes that were already reached by another search.
            if node.isVisited:
                continue

            queue = [node]

            # Search outward until there are no more connected nodes.
            while len(queue) > 0:
                current_node = queue.pop(0)

                if current_node.isVisited:
                    continue

                current_node.isVisited = True

                # Add all unvisited connected nodes to the queue.
                for next_node in current_node.nodes:
                    if not next_node.isVisited:
                        queue.append(next_node)

            # One complete connected component was searched.
            output += 1

        return output