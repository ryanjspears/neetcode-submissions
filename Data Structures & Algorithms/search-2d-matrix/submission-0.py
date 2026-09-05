class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_m = []

        for row in matrix:
            for item in row:
                new_m.append(item)

        l, r = 0, len(new_m) - 1

        while l<=r:
            mid = l + (r-l)//2

            if new_m[mid] == target:
                return True
            elif new_m[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False