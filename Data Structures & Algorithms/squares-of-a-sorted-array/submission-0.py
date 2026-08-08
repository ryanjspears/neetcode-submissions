class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        tmp = [num**2 for num in nums] 
        tmp.sort()

        return tmp