class Solution:
    def tribonacci(self, n: int) -> int:
        prefix = [0,1,1]
        p = 3
        while p<=n:
            prefix.append(prefix[-1]+prefix[-2]+prefix[-3])
            p+=1
        return prefix[n]
        