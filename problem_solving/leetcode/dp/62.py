# 62. Unique Paths

# Approach
    # possible paths to left and top indicates that current grid has possible path of left + top
    # reference left and top, sum them up and record to current grid

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Time complexity: O(mn)
        Space complexity: O(mn)
        '''
        grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
        grid[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m][n]

# Cleaner and more efficient solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Time complexity: O(mn)
        Space complexity: O(n)
        '''
        row = [1] * n # row below newRow

        for i in range(m - 1):
            newRow = [1] * n # a row over the old row
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j] # right + down
            row = newRow
        return row[0]

        # this approach reuses the row by substituting old row to new row instead of making whole grid at once
            # therefore use of memory space is smaller
        # number of loop is relatively smaller
