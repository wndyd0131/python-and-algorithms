class Solution:
    '''
    Algorithm: Nested Binary Search
      1. Binary search row-wise
        a. set top, mid, bottom pointer
        b. if target is in between first and last element of the row, then proceed '#2'
        c. else if target is less than first element, move the bottom pointer to mid - 1
        d. else if target is greater than last element, move the top pointer to mid + 1
      2. Binary search column-wise
        a. set left, mid, right pointer
        b. if target equals to mid, then return true
        c. else if target is less than mid, move right pointer to mid - 1
        d. else if target is greater than mid, move left pointer to mid + 1
    Time Complexity: O(log(n * m))
    Space Complexity: O(1)
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            row_mid = (top + bottom) // 2
            left = 0
            right = len(matrix[row_mid]) - 1
            if target >= matrix[row_mid][left] and target <= matrix[row_mid][right]:
                while left <= right:
                    col_mid = (left + right) // 2
                    if target == matrix[row_mid][col_mid]:
                        return True
                    elif target < matrix[row_mid][col_mid]:
                        right = col_mid - 1
                    elif target > matrix[row_mid][col_mid]:
                        left = col_mid + 1
                return False
            elif target < matrix[row_mid][left]:
                bottom = row_mid - 1
            elif target > matrix[row_mid][right]:
                top = row_mid + 1
        return False