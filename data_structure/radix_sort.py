def radix_sort(arr):
  queue = [[],[],[],[],[],[],[],[],[],[]]
  length = len(arr[0])
  for r in range(length-1, -1, -1):
    for i in range(len(arr)):
      digit = arr[i][r]
      queue[int(digit)].append(arr[i])
    arr = []
    for i in range(len(queue)):
      for _ in range(len(queue[i])):
        arr.append(queue[i].pop(0))
  return arr

arr= []
N = int(input())
for i in range(N):
  arr.append(input())
print(radix_sort(arr))