# 54. Spiral Matrix

# First
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = ['R', 'D', 'L', 'U']
        dir_idx = 0
        result = []
        i, j = 0, 0

        # Boundary Setting
        l_bound, r_bound, t_bound, b_bound = 0, len(matrix[0]), 0, len(matrix)
        print(l_bound, r_bound, t_bound, b_bound)

        while l_bound < r_bound and t_bound < b_bound:
            match direction[dir_idx % 4]:
                case 'R':
                    i, j = t_bound, l_bound
                    while j < r_bound:
                        result.append(matrix[i][j])
                        j += 1
                    t_bound += 1
                case 'D':
                    i, j = t_bound, r_bound - 1
                    while i < b_bound:
                        result.append(matrix[i][j])
                        i += 1
                    r_bound -= 1
                case 'L':
                    i, j = b_bound - 1, r_bound - 1
                    while j >= l_bound:
                        result.append(matrix[i][j])
                        j -= 1
                    b_bound -= 1
                case 'U':
                    i, j = b_bound - 1, l_bound
                    while i >= t_bound:
                        result.append(matrix[i][j])
                        i -= 1
                    l_bound += 1
            dir_idx += 1
        return result
      
# Cleaner
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        # Boundary Setting
        l_bound, r_bound, t_bound, b_bound = 0, len(matrix[0]), 0, len(matrix)
        print(l_bound, r_bound, t_bound, b_bound)

        while l_bound < r_bound and t_bound < b_bound:
            
            # right
            for j in range(l_bound, r_bound):
                result.append(matrix[t_bound][j])
            t_bound += 1
            
            # down
            for i in range(t_bound, b_bound):
                result.append(matrix[i][r_bound - 1])
            r_bound -= 1

            # Check if any valid rectangle remains 
            if not (l_bound < r_bound and t_bound < b_bound):
                break

            # left
            for j in range(r_bound - 1, l_bound - 1, -1):
                result.append(matrix[b_bound - 1][j])
            b_bound -= 1

            # up
            for i in range(b_bound - 1, t_bound - 1, -1):
                result.append(matrix[i][l_bound])
            l_bound += 1
        return result
