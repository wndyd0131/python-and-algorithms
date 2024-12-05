def heapify(arr, idx, last_idx):
  l = idx * 2
  r = idx * 2 + 1
  smallest = idx
  if(l <= last_idx and arr[l] < arr[smallest]):
    smallest = l
  if(r <= last_idx and arr[r] < arr[smallest]):
    smallest = r
  if smallest != idx:
    arr[idx], arr[smallest] = arr[smallest], arr[idx] 
    return heapify(arr, smallest, last_idx)
  
def heap_sort(arr):
  length = len(arr)
  arr = [0]+arr
  
  for i in range(length, 0, -1):
    heapify(arr, i, length)
    
  for i in range(length, 0, -1):
    print(arr[1])
    arr[1], arr[i] = arr[i], arr[1]
    heapify(arr, 1, i-1)
  
arr = [0,5,3,4,2,1]
heap_sort(arr)

# 내가 구현한 힙
# def insert(data):
#   heap.append(data)
#   print(heap)
#   if len(heap) - 1 <= 1:
#     return
#   else:
#     last = len(heap) - 1
#     while(last // 2 != 0):
#       if heap[last] > heap[last//2]:
#         heap[last], heap[last//2] = heap[last//2], heap[last]
#         print(heap)
#         last //= 2
#       else:
#         print(heap)
#         break
#     return
  
# heap = []
# heap.append(None)
# insert(9)
# insert(8)
# insert(3)
# insert(10)
# insert(15)
# insert(4)
# print(heap)