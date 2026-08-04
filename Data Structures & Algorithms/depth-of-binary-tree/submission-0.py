# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countDep(self, node, count):
        if node is None:
            return count

        return max(self.countDep(node.left, count + 1),self.countDep(node.right, count + 1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.countDep(root, 0)

        