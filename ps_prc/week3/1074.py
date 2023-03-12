import sys
sys.setrecursionlimit(10 ** 6)

def func(x, y, n):
  global cnt
  if x > r or x+n <= r or y > c or y+n <= c:
    cnt += n**2
    return
  
  if n > 2:
    n //= 2  
    func(x,y,n)
    func(x,y+n,n)
    func(x+n,y,n)
    func(x+n,y+n,n)
  else:
    if x==r and y==c:
      print(cnt)
    elif x==r and y+1==c:
      print(cnt+1)
    elif x+1==r and y==c:
      print(cnt+2)
    else:
      print(cnt+3)
    sys.exit()

N, r, c = list(map(int, sys.stdin.readline().split()))
cnt = 0
# arr = [[0] * 2**N for _ in range(2**N)]
if r == 0 and c == 0:
  print(0)
else:
  func(0,0,2**N)
  print(cnt)