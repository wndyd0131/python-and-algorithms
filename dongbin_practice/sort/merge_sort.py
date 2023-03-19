import sys
sys.setrecursionlimit(10 ** 6)
def merge_sort(arr):
  ##분할
  if len(arr) < 2:
    return arr
  
  mid = len(arr) // 2 
  low_arr = merge_sort(arr[:mid])
  high_arr = merge_sort(arr[mid:])
  ##
  
  ##정복
  merged_arr = []
  l = h = 0
  
  while l < len(low_arr) and h < len(high_arr):
    if low_arr[l] < high_arr[h]:
      merged_arr.append(low_arr[l])
      l += 1
    else:
      merged_arr.append(high_arr[h])
      h += 1
  merged_arr += low_arr[l:]
  merged_arr += high_arr[h:]
  return merged_arr
  ##



arr = [56, 24, 9, 7, 0, 2, 3, 4, 3, 57, 9, 1]
n_arr = merge_sort(arr)
print(n_arr)