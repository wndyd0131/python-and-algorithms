import sys    
N = int(sys.stdin.readline())
arr = list()
for i in range(N):
  [a, b] = map(int, input().split())
  arr.append([a, b])

new_arr = sorted(arr)
for i in range(N):
  print(new_arr[i][0], new_arr[i][1])