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
                grid[i][j] = grid[i-1][j] + grid[i][j-1] + grid[i][j]
        return grid[m][n]