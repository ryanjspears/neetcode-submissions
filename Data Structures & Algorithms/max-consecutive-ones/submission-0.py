class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        tmp = 0
        for num in nums:
            if num == 1:
                tmp +=1
            else:
                maxi = max(tmp, maxi)
                tmp = 0

        maxi = max(tmp, maxi)
        return maxi
