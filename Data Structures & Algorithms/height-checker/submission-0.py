class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        old = []
        for num in heights:
            old.append(num)
        heights.sort()

        count = 0
        for i, num in enumerate(heights):
            if num != old[i]:
                count+=1

        return count
    