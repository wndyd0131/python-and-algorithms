import sys
age = [int(sys.stdin.readline().strip()) for _ in range(9)]
for i in range(9):
  for j in range(i+1, 9):
    arr = [x for x in age if x != age[i] and x != age[j]]
    if sum(arr) == 100:
      result = sorted(arr)
for i in result:
  print(i)