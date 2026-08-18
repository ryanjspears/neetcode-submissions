class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(nums, t, l, r):
            while l<=r:
                mid = ((r-l)//2) + l

                if nums[mid] == t:
                    return mid
                
                if nums[mid] < t:
                    l= mid+1
                else:
                    r= mid - 1
            
            return None

        p = 0
        while p < len(numbers) -1:
            cur = numbers[p]
            comp = target - cur
            find = bin_search(numbers, comp, p+1, len(numbers)-1)
            if find:
                return [p+1, find+1]
            p+=1

        return []
        