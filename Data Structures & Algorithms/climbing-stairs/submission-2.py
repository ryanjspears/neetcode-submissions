class Solution:
    def climbStairs(self, n: int) -> int:
        mapy = {}
        i = 0
        while i < n:
            i+=1
            if i == 1:
                mapy[1] = 1
            elif i == 2:
                mapy[2] = 2
            else:
                mapy[i] = mapy[i-1] + mapy[i-2]

        return mapy[n]
        