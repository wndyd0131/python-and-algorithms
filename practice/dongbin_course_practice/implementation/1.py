import sys

x,y = 1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
direction = ['L','R','U','D']
#direction 배열 생성

N = int(sys.stdin.readline().strip())
plans = sys.stdin.readline().split()

for plan in plans:
  for i in range(len(direction)):
    if plan == direction[i]: #plan과 direction배열과 비교해서 dx와 dy가 i에 따라 작동하도록 함
      nx = x + dx[i]
      ny = y + dy[i]
    
  if nx < 1 or ny < 1 or nx > N or ny > N: #배열을 초과하면 무시
    continue
  
  x,y = nx, ny
  
print(x,y)