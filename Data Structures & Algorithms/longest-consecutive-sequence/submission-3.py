class Node:
    def __init__(self, x: int):
        self.val = x
        self.prev = None
        self.post = None
    
    def set_prev(self, node: Node):
        self.prev = node
    
    def set_post(self, node: Node):
        self.post = node




class Solution:
    def search_node(self, node, nums):
        count = 1
        nums[node.val] = True

        r = node.post
        l = node.prev
        #go left
        while l is not None:

            count+=1
            nums[l.val] = True
            l = l.prev

        #go right
        while r is not None:

            count+=1
            nums[r.val] = True
            r = r.post
        
        return count



    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        mappy = {}

        for num in nums:
            if num in mappy:
                continue

            temp = Node(num)
            mappy[num] = temp

            if num - 1 in mappy:
                previous = mappy[num - 1]
                previous.post = temp
                temp.prev = previous

            if num + 1 in mappy:
                next_node = mappy[num + 1]
                temp.post = next_node
                next_node.prev = temp

        max_l = 0


        visited_nums = {}
        for key, value in mappy.items():
            if visited_nums.get(key) is None:
                # search nodes counts
                max_l = max(self.search_node(mappy[key], visited_nums), max_l)

        return max_l
