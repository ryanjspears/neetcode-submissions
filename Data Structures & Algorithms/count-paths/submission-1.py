class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Stores the number of paths from each coordinate
        # to the bottom-right coordinate.
        memo = {}

        def dfs(row: int, col: int) -> int:
            # Stop if we move outside the grid.
            if row >= m or col >= n:
                return 0

            # We reached the bottom-right coordinate.
            if row == m - 1 and col == n - 1:
                return 1

            # This coordinate was already calculated.
            if (row, col) in memo:
                return memo[(row, col)]

            # Search by moving down or right.
            down_paths = dfs(row + 1, col)
            right_paths = dfs(row, col + 1)

            # Store all paths from this coordinate.
            memo[(row, col)] = down_paths + right_paths

            return memo[(row, col)]

        return dfs(0, 0)