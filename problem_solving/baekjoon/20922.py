# count map 만듦
# count가 K를 넘을 경우 그 수의 count가 K가 아닐 때까지, i를 한 칸씩 올림

n, k = map(int, input().split())
arr = list(map(int, input().split()))


cur_max = float('-inf')

freq_map = {item: 0 for item in arr}

i = 0
for j in range(len(arr)):
  if freq_map[arr[j]] == k:
    cur_max = max(cur_max, j - i)
    while freq_map[arr[j]] == k:
      freq_map[arr[i]] -= 1
      i += 1
  else:
    cur_max = max(cur_max, j - i + 1)
  freq_map[arr[j]] += 1

print(cur_max)

'''
Change
'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

i = 0
for j in range(len(arr)):

  freq_map[arr[j]] = freq_map.get(arr[j], 0) + 1
  
  while freq_map[arr[j]] > k:
    freq_map[arr[i]] -= 1
    i += 1
    
  answer = max(answer, j - 1 + 1)

print(answer)