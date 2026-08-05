# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []

        if root is None:
            return final

        stack = [root]
        pointer = root

        while pointer is not None:
            temp = stack
            stack = []
            level = []

            for node in temp:
                level.append(node.val)

                if node.left is not None:
                    stack.append(node.left)

                if node.right is not None:
                    stack.append(node.right)

            final.append(level)

            if len(stack) == 0:
                break

            pointer = stack[0]

        return final