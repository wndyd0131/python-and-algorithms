# 피보나치 수 2
import sys
dp = [0] * 101
n = int(sys.stdin.readline())

dp[1], dp[2] = 1, 1

for i in range(2, n+1):
    if n == 0:
        print(0)
        break
    if n == 1:
        print(1)
        break
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])