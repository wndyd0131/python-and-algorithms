def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    l_list = arr[:mid]
    r_list = arr[mid:]
    left = merge_sort(l_list)
    right = merge_sort(r_list)
    merged = merge(left, right)
    return merged
  else:
    return arr
  
def merge(list1, list2):
  merged = []
  while len(list1) > 0 and len(list2) > 0:
    if list1[0] <= list2[0]:
      merged.append(list1.pop(0))
    else:
      merged.append(list2.pop(0))
  if len(list1) > 0:
    merged += list1
  if len(list2) > 0:
    merged += list2
    
  return merged

sorted = merge_sort([4,1,2,6,7,3])
print(sorted)