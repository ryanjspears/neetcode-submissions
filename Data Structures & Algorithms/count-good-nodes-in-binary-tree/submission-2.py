# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque()
        q.append((root, -111))

        while q:
            node, path = q.pop()
            new_path = max(node.val, path)

            #add next nodes to queue
            if node.right:
                q.appendleft((node.right, new_path))
            if node.left:
                q.appendleft((node.left, new_path))

            #count cond
            
            if not path > node.val:
                count+=1

        return count
        