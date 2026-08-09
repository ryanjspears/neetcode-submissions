class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        secs = 0
        prev = None
        while fresh > 0 and prev != fresh:
            prev = fresh
            secs += 1

            #copy for working table
            copy = []
            for row in grid:
                r = []
                for fruit in row:
                    r.append(fruit)

                copy.append(r)

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        #check if can be infected
                        c1 =  c2 = c3 = c4 = False
                        if j + 1 < m and grid[i][j + 1] == 2:
                            c1 = True
                        if j > 0 and grid[i][j - 1] == 2:
                            c2 = True
                        if i + 1 < n and grid[i+1][j] == 2:
                            c4 = True
                        if i > 0 and grid[i - 1][j] == 2:
                            c4 = True

                        if c1 or c2 or c3 or c4:
                            copy[i][j] = 2 
                            fresh -= 1
            print(copy)
            print(fresh)
            print(prev)
            grid = copy

        if fresh > 0:
            return - 1
        return secs
            



        


        

        