def two_pointers(arr):
  new_arr = []
  target = 27
  s, e = 0, len(arr) - 1
  while s <= e:
    value = arr[s] + arr[e]
    if value > target:
      e -= 1
    elif value < target:
      s += 1
    else:
      new_arr.append([arr[s], arr[e]])
      s += 1
      e -= 1
  return new_arr

arr = [1, 3, 5, 6, 9, 11, 12, 16, 17, 19, 22, 25, 28]
print(two_pointers(arr))