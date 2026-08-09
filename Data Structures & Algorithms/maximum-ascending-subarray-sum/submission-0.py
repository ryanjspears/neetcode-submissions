class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi = nums[0]
        tmp = 0
        prev = 0

        for num in nums:
            if num > prev:
                tmp += num
                prev = num
            else:
                maxi = max(maxi, tmp)
                tmp = num
                prev = num
        
        maxi = max(maxi, tmp)
        return maxi