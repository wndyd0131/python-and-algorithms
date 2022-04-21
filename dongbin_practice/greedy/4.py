#모험가 길드 (공포도에 해당하는 그룹을 결성시켜 그룹의 최댓값을 찾는 문제)
import sys
num = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

result = 0
cnt = 0

for i in data:
  cnt += 1
  if cnt >= i:
    result += 1
    cnt = 0
  
print(result)

#정렬해서 오름차순으로 접해야 쉽게 풀 수 있는 문제