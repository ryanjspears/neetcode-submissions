class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = defaultdict(int)

        for num in arr:
            m[num] += 1

        maxi = -1
        for key, value in m.items():
            if key == value:
                maxi = max(key, maxi)
        return maxi
                    

        

        