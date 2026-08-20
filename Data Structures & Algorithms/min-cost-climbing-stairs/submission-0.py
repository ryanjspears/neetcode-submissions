class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prefix = [None] * len(cost)
        prefix.append(0)
        prefix.append(0)
        p = len(prefix) -2
        print(prefix)
        while p > 0:
            p-=1
            print(prefix)
            mini = min(prefix[p+1], prefix[p+2])
            prefix[p] = mini + cost[p]
        
        return min(prefix[0], prefix[1])
            

        