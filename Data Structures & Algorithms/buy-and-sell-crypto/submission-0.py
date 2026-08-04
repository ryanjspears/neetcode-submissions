class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        b, s = len(prices) - 2, len(prices) - 1
        total = 0
        maxi = prices[s]
        while b >= 0:
            price = maxi - prices[b]

            if price > 0 and price > total:
                total = price

            maxi = max(prices[b], maxi)

            b-=1
            
        return total 
