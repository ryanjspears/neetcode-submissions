# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insert_sorted(self, num):
        i = len(self.arr) - 1
        self.arr.append(num)  # make space

        while i >= 0 and self.arr[i] > num:
            self.arr[i + 1] = self.arr[i]
            i -= 1

        self.arr[i + 1] = num
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        def dfs(node):
            if node is None:
                return
            self.insert_sorted(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(self.arr)

        return self.arr[k-1]


        