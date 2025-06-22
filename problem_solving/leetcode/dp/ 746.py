class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = min(cost[0], cost[1])
        for i in range(2, n):
            # min(current_minimum + cur_idx, current_minimum + cur_idx+1, previous_minimum + [1])
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-1] + cost[i], dp[i-2] + cost[i-1])
        return dp[n - 1]