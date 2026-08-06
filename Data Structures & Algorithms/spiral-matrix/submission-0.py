from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        visited = [[False] * cols for _ in range(rows)]
        final = []

        row = 0
        col = 0
        count = 0
        total_cells = rows * cols

        def move(row, col, x_direction, y_direction, count):
            final.append(matrix[row][col])
            visited[row][col] = True
            count += 1

            new_row = row + y_direction
            new_col = col + x_direction

            return new_row, new_col, count

        def canVisit(row, col):
            return (
                0 <= row < rows
                and 0 <= col < cols
                and not visited[row][col]
            )

        while count < total_cells:
            # Right
            while canVisit(row, col):
                row, col, count = move(row, col, 1, 0, count)

            # Undo right movement, then move down
            col -= 1
            row += 1

            # Down
            while canVisit(row, col):
                row, col, count = move(row, col, 0, 1, count)

            # Undo down movement, then move left
            row -= 1
            col -= 1

            # Left
            while canVisit(row, col):
                row, col, count = move(row, col, -1, 0, count)

            # Undo left movement, then move up
            col += 1
            row -= 1

            # Up
            while canVisit(row, col):
                row, col, count = move(row, col, 0, -1, count)

            # Undo up movement, then move right
            row += 1
            col += 1

        return final