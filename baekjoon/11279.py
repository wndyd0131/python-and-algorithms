import sys, heapq
heap = []
N = int(sys.stdin.readline())
for i in range(N):
  input = -(int(sys.stdin.readline()))
  if input == 0:
    if heap:
      print (-(heapq.heappop(heap)))
    else:
      print(0)
  else:
    heapq.heappush(heap, input)
    
# 최대힙:
# - 파이썬에서 제공하는 heapq모듈은 최소힙만 제공한다
# - 트릭: 입력받은 수를 음수로 변경시켜 최소힙을 사용하면 최대힙이 된다