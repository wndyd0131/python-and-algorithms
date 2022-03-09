import sys
result = 0
cmd = list(map(int, sys.stdin.readline().split()))
N, M = cmd[0], cmd[1]
card = list(map(int, sys.stdin.readline().split()))
for i in range(N):
  for j in range(i+1, N): # 수정[N -> i+1, N]
    for k in range(j+1, N): # 수정[N -> j+1, N ]
      # if i == j or j == k or i == k:
      #   continue 수정[주석처리]
      s = card[i] + card[j] + card[k]
      if s > M:
        continue
      else:
        result = max(result, s)
      # if s > max:
      #   max = s 수정[max()로 변경]
print(result)