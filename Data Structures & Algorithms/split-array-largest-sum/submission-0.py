class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
        # Check if we can split array with max subarray sum <= largest
            splits = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > largest:
                    splits += 1
                    current_sum = num
                else:
                    current_sum += num
                    
            return splits <= k
    
        # Binary search on the answer
        left = max(nums)  # At least the largest element
        right = sum(nums)  # At most the entire array sum
        
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid  # Try to minimize further
            else:
                left = mid + 1  # Need larger maximum sum
        
        return left