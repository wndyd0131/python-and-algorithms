# T = 상담을 완료하기 까지 걸리는 시간
# P = 상담으로 받는 금액
# N = 일하는 기간

# 초과되는 시간
# N + 1일 이전 

# 돈의 합계가 최대
# 기간은 넘기면 안되고

import sys
mx = 0
planner = dict()
N = int(sys.stdin.readline())
dp = [0] * (N + 1) # 마지막에 있는 인덱스까지 7 dp table 0~7
planner[N] = [0, 0]
for i in range(0, N):
  cmd = list(map(int, sys.stdin.readline().split()))
  planner[i] = cmd
  
for i in range(0, N+1):
  t = planner[i][0]
  p = planner[i][1]
  dp[i] = max(dp[i], mx)
  print(i)
  if (i + t) <= N:
    dp[i+t] = max(dp[i+t], dp[i] + p)
  mx = max(dp[i], mx)
print(mx)

# 왜 안됨
# 각 날짜까지의 최대이익을 저장해서 그 최대이익을 더하여 max값을 도출해내는 문제