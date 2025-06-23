class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = min(cost[0], cost[1])
        for i in range(2, n):
            # min(current_minimum + cur_idx, current_minimum + cur_idx+1, previous_minimum + [1])
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-1] + cost[i], dp[i-2] + cost[i-1])
        return dp[n - 1]

# Cleaner and more efficient solution
class Solution:
    '''
    Time complexity: O(n)
    Space complexity: O(n), can improve it to O(1) by only using array of length 2
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2]) # or cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

# Subproblems: solution to idx 0 needs solution to idx 1, 2...
# Brute force (Decision Tree) O(2^n)
# DP
    # since left idx depends on right idx to solve a problem, it could be easier to start from right to left
        # [10, 15, 20] for instance, min of problem when [0] is chosen depends on min of when [1] or [2] is chosen
            # 20's min -> 15's min -> 10's min