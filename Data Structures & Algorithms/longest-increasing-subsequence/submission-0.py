class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # Stores the longest jump sequence starting at each index.
        memo = [1] * len(nums)

        # Start from the second-to-last number and work backward.
        i = len(nums) - 2

        while i >= 0:
            # Check every number after the current number.
            for j in range(i + 1, len(nums)):
                # The current number can jump to this later number.
                if nums[i] < nums[j]:
                    memo[i] = max(
                        memo[i],
                        memo[j] + 1
                    )

            i -= 1

        return max(memo)