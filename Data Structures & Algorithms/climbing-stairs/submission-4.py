class Solution:
    def climbStairs(self, n: int) -> int:
        prefix = [1,2,3]
        p = 3
        while p<n:
            prefix.append(prefix[-1] + prefix[-2])
            p+=1
        return prefix[n-1]