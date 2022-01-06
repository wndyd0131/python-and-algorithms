def selection_sort(arr):
  for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if(arr[j] < arr[min_idx]):
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr[:i+1])
    
selection_sort([1,2,5,3,6,0,6,7])