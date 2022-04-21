import sys
num = int(sys.stdin.readline())
data = sys.stdin.readline().split()
result = 0
cnt = 0
MAX = int(data[0])
prev = 0

for i in range(1, len(data)):
  d = int(data[i])
  if d <= prev:
    if cnt == MAX:
      cnt = 0
      result += 1
      MAX = d
    else:
      cnt += 1
  else:
    MAX = d
    cnt += 1
  prev = d