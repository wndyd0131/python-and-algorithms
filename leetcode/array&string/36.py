# 36. Valid Sudoku
class Solution:
    '''
    Status: Success
    Algorithms: Hash map, Set
    Step:
        1. create rowMap, colMap, matrixMap that uses row, col, and matrix as key
        2. assign set to each map of row, col, and matrix
        3. iterate through whole matrix
            1. if curVal already in rowMap[row] or colMap[col] or matrixMap[row // 3, col // 3]
                # duplicate, so return False
            2. else add curVal to rowMap[row], colMap[col], and matrixMap[row // 3, col // 3]
        4. return True if loop ends successfully
    Time complexity: O(1) = O(N^2) if NxN
    Space complexity: O(1) = O(N) if NxN
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {}
        colMap = {}
        matrixMap = {}
        for i in range(len(board)):
            rowMap[i] = set()
            for j in range(len(board[i])):
                value = board[i][j]
                if j not in colMap:
                    colMap[j] = set()
                if (i // 3, j // 3) not in matrixMap:
                    matrixMap[(i // 3, j // 3)] = set()
                if value == '.':
                    continue
                value = int(value)
                if value in rowMap[i] or value in colMap[j] or value in matrixMap[(i // 3, j // 3)]:
                    return False
                rowMap[i].add(value)
                colMap[j].add(value)
                matrixMap[(i // 3, j // 3)].add(value)

        return True