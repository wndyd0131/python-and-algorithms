# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        visited = [[False] * len(matrix[0]) for row in range(len(matrix))]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # direction matrix (R, D, L, U )
        r, c, d = 0, 0, 0

        # loop until result is filled
        while len(result) != len(matrix[0]) * len(matrix):
            # append current value
            result.append(matrix[r][c])
            visited[r][c] = True
            
            # pre-assign next move
            nr, nc = r + dirs[d][0], c + dirs[d][1]

            # if next move is not valid, then swith to next direction
            if nr < 0 or nr >= len(matrix) or nc < 0 or nc >= len(matrix[0]) or visited[nr][nc]:
                d = (d + 1) % 4
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]

            # assign next move to the pointer
            r = nr
            c = nc
        return result
    
# Thought
  # At first, I tried to break loop when an element faces boundary or visited
    # Sometimes condition for loop is simpler than you see.