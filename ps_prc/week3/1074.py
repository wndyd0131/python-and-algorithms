import sys
sys.setrecursionlimit(10 ** 6)
# 3 (0,0) (0,4) (4,0) (4,4)
# 2 (0,0) (0,2) (2,0) (2,2)
# 1 (0,0) (0,1) (1,0) (1,1)
# 0

def func(x, y, n):
  global cnt
  if arr[r][c] == 1:
    return
  if n == 0:
    arr[x][y] = 1
    cnt += 1
    return
  num = 2**n // 2
  func(x,y,n-1)
  func(x,y+num,n-1)
  func(x+num,y,n-1)
  func(x+num,y+num,n-1)
    

N, r, c = list(map(int, sys.stdin.readline().split()))
cnt = -1
arr = [[0] * 2**N for _ in range(2**N)]
if r == 0 and c == 0:
  print(0)
else:
  func(0,0,N)
  print(cnt)