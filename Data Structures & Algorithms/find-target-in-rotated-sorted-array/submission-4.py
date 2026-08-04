class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return 0

        while True:
            if r - 1 == l:
                if nums[l] < nums[r]:
                    return l
                else:
                    return r
            mid = ((r - l)//2) + l
            print(mid)

            if nums[mid] > nums[mid + 1]:
                return mid+1
            elif nums[l] > nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid
            else:
                return l

    def bs(self, nums,l, r, t):
        while l<r-1:
            mid = ((r-l)//2)+l

            if nums[mid] == t:
                return mid
            
            if nums[mid] > t:
                r = mid - 1
            else:
                l = mid + 1
        
        if nums[l] == t:
            return l
        
        if nums[r] == t:
            return r

        return -1

    def search(self, nums: List[int], target: int) -> int:
        min_index = self.findMinIndex(nums)
        print(f"min index: {min_index}")
        if min_index == 0:
            return self.bs(nums, 0, len(nums) - 1, target)
        
        if target <= nums[min_index-1] and target >=nums[0]:
            return self.bs(nums, 0, min_index-1, target)

        return self.bs(nums, min_index, len(nums)- 1, target)
        