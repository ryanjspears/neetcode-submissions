class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        n = None
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

            if m[num] > count:
                count = m[num]
                n = num

        return n
        