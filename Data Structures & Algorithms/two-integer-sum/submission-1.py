class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        i = 0
        for num in nums:
            n[num]=i
            i+=1
        i = 0
        for num in nums:
            comp = target - num
            if n.get(comp) and n[comp] != i:
                return [i, n[comp]]
            i+=1
