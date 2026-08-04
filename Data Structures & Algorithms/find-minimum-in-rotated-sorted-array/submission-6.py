class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]

        while True:
            print("mid")
            if r - 1 == l:
                return min(nums[l], nums[r])
            mid = ((r - l)//2) + l
            print(mid)

            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            elif nums[l] > nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid
            else:
                return nums[l]
