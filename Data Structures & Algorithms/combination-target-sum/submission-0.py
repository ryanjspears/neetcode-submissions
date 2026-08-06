from collections import deque
from typing import List


class Node:
    def __init__(self, val, total=0):
        self.val = val
        self.total = total
        self.nodes = {}

    def addNode(self, node):
        self.nodes[node.val] = node


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Build a unique, sorted list of numbers
        nums = sorted(set(nums))

        # Root represents an empty combination with a total of 0
        root = Node(0, 0)

        # Queue stores:
        # current node, current total, and the minimum index we can use
        queue = deque()
        queue.append((root, 0, 0))

        # Build the tree level by level
        while queue:
            current_node, current_total, start_index = queue.popleft()

            for i in range(start_index, len(nums)):
                num = nums[i]
                new_total = current_total + num

                # Do not add numbers that push us past the target
                if new_total > target:
                    break

                new_node = Node(num, new_total)
                current_node.addNode(new_node)

                # Only continue expanding if we have not reached target
                if new_total < target:
                    # Pass i again because the same number may be reused
                    queue.append((new_node, new_total, i))

        final = []

        # DFS through the tree to collect paths that reach target
        def dfs(node, path):
            if node is not root:
                path.append(node.val)

            if node.total == target:
                final.append(path.copy())
            else:
                for child in node.nodes.values():
                    dfs(child, path)

            if node is not root:
                path.pop()

        dfs(root, [])

        return final