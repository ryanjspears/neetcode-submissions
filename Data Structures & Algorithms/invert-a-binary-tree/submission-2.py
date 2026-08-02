# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def switch(self, node):
        if node is None:
            return
        
        r = node.right
        node.right = node.left
        node.left = r

        #continue
        self.switch(node.right)
        self.switch(node.left)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.switch(root)
        return root
        
        