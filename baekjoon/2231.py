import sys
T = int(sys.stdin.readline().strip())
for i in range(10, T+1):
    arr = list(map(int, str(i)))
    result = i + sum(arr)
    if result == T:
      print(i)
      break
    if i == T:
      print(0)