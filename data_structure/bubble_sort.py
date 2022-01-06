# def bubble_sort(arr):
#   for i in range(len(arr)):
#     for j in range(0, (len(arr) -1) - i):
#       if arr[j] > arr[j+1]:
#         arr[j], arr[j+1] = arr[j+1], arr[j]

#better one
def bubble_sort(arr):
  for i in range(len(arr) - 1, 0, -1):
    for j in range(i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  

arr = [5,3,8,1,2,7] 
bubble_sort(arr)
print(arr)