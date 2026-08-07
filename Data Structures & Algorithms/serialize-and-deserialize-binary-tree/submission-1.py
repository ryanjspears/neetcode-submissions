from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"

        queue = deque([root])
        values = []

        while queue:
            node = queue.popleft()

            if node is None:
                values.append("null")
                continue

            values.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        # Remove unnecessary null values from the end.
        while values and values[-1] == "null":
            values.pop()

        return "[" + ",".join(values) + "]"

    # Decodes the encoded data back into a tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            return None

        values = data[1:-1].split(",")

        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            parent = queue.popleft()

            # Build the left child.
            if index < len(values) and values[index] != "null":
                parent.left = TreeNode(int(values[index]))
                queue.append(parent.left)

            index += 1

            # Build the right child.
            if index < len(values) and values[index] != "null":
                parent.right = TreeNode(int(values[index]))
                queue.append(parent.right)

            index += 1

        return root