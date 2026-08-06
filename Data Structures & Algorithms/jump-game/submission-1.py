from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [False] * n
        memo[-1] = True

        for i in range(n - 2, -1, -1):
            max_jump = min(i + nums[i], n - 1)

            for next_index in range(i + 1, max_jump + 1):
                if memo[next_index]:
                    memo[i] = True
                    break

        return memo[0]