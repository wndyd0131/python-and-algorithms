def merge_sort(low, high):
  if high - low < 2:
    return
  mid = (low + high) // 2
  merge_sort(low, mid)
  merge_sort(mid, high)
  merge(low, mid, high)
  # index를 재귀적으로 자름
  
def merge(low, mid, high):
  temp = []
  l, h = low, mid #low_arr과 high_arr의 시작인덱스
  
  # 투포인터
  while l < mid and h < high:
    if arr[l] < arr[h]:
      temp.append(arr[l])
      l += 1
    else:
      temp.append(arr[h])
      h += 1
  
  #나머지
  while l < mid:
    temp.append(arr[l])
    l += 1
  while h < high:
    temp.append(arr[h])
    h += 1
  
  for i in range(low, high):
    arr[i] = temp[i-low]
  
arr = [56, 24, 9, 7, 0, 2, 3, 4, 3, 57, 9, 1]
merge_sort(0, len(arr))
print(arr)