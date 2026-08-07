class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        final = [None] * len(arr)
        i = len(arr) - 1
        maxi = arr[-1]
        while i >= 0:
            cur = arr[i]
            final[i] = maxi
            maxi = max(maxi, cur)
            
            i-=1
        final[-1] = -1

        return final