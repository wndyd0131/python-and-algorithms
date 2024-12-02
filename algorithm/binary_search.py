def binary_search(arr, key, left, right):
  if left <= right:
    mid = (left + right) // 2
    if key == arr[mid]:
      return mid
    elif key < arr[mid]:
      return binary_search(arr, key, left, mid - 1)
    else:
      return binary_search(arr, key, mid + 1, right)
  return -1

arr = [2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47]
print(binary_search(arr, 34, 0, len(arr) - 1))

# 자료가 이미 정렬된 상태여야 함
# 시간복잡도 O(log₂n)

# def seq_search(arr, key, low, high):
#   i = low
#   arr.append(key)
#   while(arr[i] != key):
#     i += 1
#   if i == high:
#     return -1
#   else: return i
  
# arr = [4,2,1,6,7,5,9,40,21]
# print(seq_search(arr, 23, 0, len(arr)))

#시간복잡도 O(n)