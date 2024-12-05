def shell_sort(arr):
  #shell sort
  gap = len(arr) // 2
  cnt = 0
  while gap >= 1: #gap이 1될 때까지 돌림
    if(gap % 2 == 0): #gap 짝수면 +1
      gap += 1
    for i in range(gap): #매번 줄어드는 gap만큼 돌림
      #insertion sort
      for j in range(gap + i, len(arr), gap): #5씩 올리면서 끝까지
        for k in range(j, i, -gap): #자신부터 시작해서 i까지 gap끼리 비교 (삽입 정렬)
          if arr[k - gap] > arr[k]:
            arr[k - gap], arr[k] = arr[k], arr[k - gap]
    gap = gap // 2 #gap 2로 나눔
  return

arr = [10,8,6,20,4,3,22,1,0,15,16]
shell_sort(arr)
print(arr)