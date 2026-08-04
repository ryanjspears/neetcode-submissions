# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        #XOR
        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        test = self.traverse(node1.left, node2.left)
        test2 = self.traverse(node1.right, node2.right)
        return test and test2

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p,q)