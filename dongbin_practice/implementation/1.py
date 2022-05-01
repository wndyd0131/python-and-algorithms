import sys
matrix = []
x = 0
y = 0

N = int(sys.stdin.readline().strip())
direction = sys.stdin.readline().split()

for i in direction:
  if i == 'R':
    if y == N-1:
      continue
    else:
      y += 1
  elif i == 'L':
    if y == 0:
      continue
    else:
      y -= 1
  elif i == 'U':
    if x == 0:
      continue
    else:
      x -= 1
  elif i == 'D':
    if x == N-1:
      continue
    else:
      x += 1
  else:
    print("제대로 입력하세요")
    break

print(x+1, y+1)