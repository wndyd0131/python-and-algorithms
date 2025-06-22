class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n == 3:
            return 2
        dp = [()] * (n + 1)
        dp[3] = (1, 1, 2)
        for i in range(3, n): # from T = a + b + c, keep forwarding (b, c, a + b + c)
            dp[i+1] = (dp[i][1], dp[i][2], dp[i][0] + dp[i][1] + dp[i][2])
        return dp[n][2]