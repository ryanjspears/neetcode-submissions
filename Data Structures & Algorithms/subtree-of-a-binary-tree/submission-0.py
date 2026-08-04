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

    def search(self, target, node, can):
        if node is None:
            return
        
        if node.val == target:
            can.append(node)

        self.search(target, node.left, can)
        self.search(target, node.right, can)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        t = subRoot.val

        #traverse and find all canadites
        can = []
        self.search(t, root, can)

        for node in can:
            if self.isSameTree(node, subRoot):
                return True

        return False

        