n, s = map(int, input().split())
arr = list(map(int, input().split()))

cur_sum = 0
min_len = float('inf')
i = 0
for j in range(len(arr)):
  cur_sum += arr[j]
  while cur_sum >= s:
    min_len = min(min_len, len(arr[i:j+1]))
    cur_sum -= arr[i]
    i += 1
  

if min_len == float('inf'):
  print(0)
else:
  print(min_len)

'''
Change
'''
n, s = map(int, input().split())
arr = list(map(int, input().split()))

cur_sum = 0
min_len = float('inf')
i = 0
for j in range(len(arr)):
  cur_sum += arr[j]
  while cur_sum >= s:
    min_len = min(min_len, j - 1 + 1)
    cur_sum -= arr[i]
    i += 1
  

if min_len == float('inf'):
  print(0)
else:
  print(min_len)