import sys
N = int(sys.stdin.readline().strip())
for i in range(1, N+1):
  num_list = list(map(int, str(i)))
  result = i + sum(num_list)
  if result == N:
    print(i)
    break
  if i == N:
    print(0)