import sys
    
N,M = sys.stdin.readline().split()
N,M = int(N), int(M)
s = set()
cnt = 0
for i in range(N):
  s.add(input())
for i in range(M):
  if input() in s:
    cnt += 1
print(cnt)

#set 사용