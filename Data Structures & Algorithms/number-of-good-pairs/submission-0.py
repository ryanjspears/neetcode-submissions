class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = {}
        count = 0
        for i, num in enumerate(nums):
            if num in m:
                count+=m[num]
                m[num] += 1
            else:
                m[num] = 1

        return count