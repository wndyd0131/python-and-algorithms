#음수, 양수
#인덱스 스택
import sys
T = int(sys.stdin.readline())
balloons = list(map(int, sys.stdin.readline().split()))
index = [x for x in range(1, T+1)]
result = []
idx = 0

temp = balloons.pop(idx)
result.append(index.pop(idx))

while(balloons):
  if temp < 0:
    idx = (idx + temp) % len(balloons)
    temp = balloons.pop(idx)
    result.append(index.pop(idx))
  else:
    idx = (idx + temp - 1) % len(balloons)
    temp = balloons.pop(idx)
    result.append(index.pop(idx))
    
for x in result:
  print(x, end=" ")