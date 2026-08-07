class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapy = {}
        for i, num in enumerate(nums):
            if num not in mapy:
                mapy[num] = i
                continue
            
            if i - mapy[num] <= k:
                return True

            mapy[num] = i

        return False
        