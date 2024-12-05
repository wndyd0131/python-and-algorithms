def quick_sort(arr, start, end):
  if start >= end: return # 원소의 개수 1이면 정렬 완료
  pivot = start
  low = start + 1
  high = end
  
  while low <= high:
    while low <= end and arr[low] <= arr[pivot]:
      low += 1
    while high > start and arr[high] >= arr[pivot]:
      high -= 1
    if low > high:
      arr[high], arr[pivot] = arr[pivot], arr[high]
    else:
      arr[low], arr[high] = arr[high], arr[low]
  quick_sort(arr, start, high - 1)
  quick_sort(arr, high + 1, end)

  
arr = [10,2,3,4,5,6,7,8,9,1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)