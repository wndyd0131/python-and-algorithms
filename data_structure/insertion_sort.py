def insertion_sort(arr):
  for i in range(1, len(arr)): #1부터 시작
    for j in range(i, 0, -1):
      if arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
  return
      
arr = [5,3,8,1,2,7,9,10,1,3,5,2]
insertion_sort(arr)
print(arr)