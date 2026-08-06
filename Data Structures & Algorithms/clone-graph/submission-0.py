from collections import deque
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # If node is None, return None
        if node is None:
            return None

        # Hash map:
        # original node -> copied node
        visited = {}

        # Initialize the copy of the starting node
        copy = Node(node.val)
        visited[node] = copy

        # Initialize queue with the original node
        queue = deque([node])

        while queue:
            current = queue.popleft()
            current_copy = visited[current]

            for neighbor in current.neighbors:
                # If the neighbor has not been copied yet,
                # create its copy and add the original to the queue
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Connect the copied current node
                # to the copied neighbor node
                current_copy.neighbors.append(visited[neighbor])

        return copy