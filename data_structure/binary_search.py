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