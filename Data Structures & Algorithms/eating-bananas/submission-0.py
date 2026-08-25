class Solution:
    def calcHours(self, piles, bph):
        count = 0
        for pile in piles:
            count+=int(math.ceil(pile/bph))
        return count
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bps = max(piles)
        l, r = 1, max_bps
        mini = None
        while l<=r:
            mid = l + (r-l)//2 #mid= 2, mid=1
            print(mid)

            tmp = self.calcHours(piles,mid)
            if tmp > h:
                l  = mid + 1
            elif tmp <= h and mini is None:
                mini = mid # 2
                r = mid - 1
            else:
                mini = min(mid, mini)
                r = mid -1
        
        return mini
                
