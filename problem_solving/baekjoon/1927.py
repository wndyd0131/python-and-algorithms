import heapq, sys
N = int(sys.stdin.readline())
heap = []
for i in range(N):
  input = int(sys.stdin.readline())
  if input == 0:
    if heap:
      print(heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap, input)