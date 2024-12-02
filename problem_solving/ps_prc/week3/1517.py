arr_dict = {}
def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1):
      if arr[j] > arr[j+1]:
        if arr[j] in arr_dict:
          arr_dict[arr[j]] += 1
        else:
          arr_dict[arr[j]] = 1
        arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [24,9,3,1,3]
bubble_sort(arr)
print(arr)
print(arr_dict)