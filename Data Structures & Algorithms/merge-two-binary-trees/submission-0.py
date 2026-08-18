class Solution:
    def mergeTrees(
        self,
        root1: Optional[TreeNode],
        root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        if not root1:
            return root2
        if not root2:
            return root1

        q = [(root1, root2)]

        while q:
            n1, n2 = q.pop()

            n1.val += n2.val

            # LEFT
            if n1.left and n2.left:
                q.append((n1.left, n2.left))
            elif not n1.left and n2.left:
                n1.left = n2.left

            # RIGHT
            if n1.right and n2.right:
                q.append((n1.right, n2.right))
            elif not n1.right and n2.right:
                n1.right = n2.right

        return root1