# 절댓값이 같은 경우 실제값이 작은 애부터
# 절댓값이 작은 애
import sys, heapq
heap = []
value = 0
N = int(sys.stdin.readline())
for i in range(N):
  input = -(int(sys.stdin.readline()))
  if input == 0:
    if heap:
      print(heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap, input)